import csv
from math import exp, log, sqrt
from datetime import datetime
from csv import DictReader

f_w = {}
f_n = []
f_z = []

submission = '/data/pythonsolution/trunoutput/result_with_leak.csv'  # path of to be outputted submission file

with open("woutfile_with_new_parameters.txt") as infile:
    doc  = csv.reader(infile)
    for ind, row in enumerate(doc):
        if ind == 0:
            print("index = 0")
#            f_w = dict(row)
        elif ind == 2:
            f_z = list(row)
        elif ind == 4:
            f_n = list(row)
            

def data(path, D):
    ''' GENERATOR: Apply hash-trick to the original csv row
                   and for simplicity, we one-hot-encode everything

        INPUT:
            path: path to training or testing file
            D: the max index that we can hash to

        YIELDS:
            ID: id of the instance, mainly useless
            x: a list of hashed and one-hot-encoded 'indices'
               we only need the index since all values are either 0 or 1
            y: y = 1 if we have a click, else we have y = 0
    '''

    for t, row in enumerate(DictReader(open(path))):
        # process id
        disp_id = int(row['display_id'])
        ad_id = int(row['ad_id'])

        # process clicks
        y = 0.
        if 'clicked' in row:
            if row['clicked'] == '1':
                y = 1.
            del row['clicked']

        x = []
        for key in row:
            x.append(abs(hash(key + '_' + row[key])) % D)

        row = prcont_dict.get(ad_id, [])		
        # build x
        ad_doc_id = -1
        for ind, val in enumerate(row):
            if ind==0:
                ad_doc_id = int(val)
            x.append(abs(hash(prcont_header[ind] + '_' + val)) % D)

        row = event_dict.get(disp_id, [])
        ## build x
        disp_doc_id = -1
        for ind, val in enumerate(row):
            if ind==0:
                uuid_val = val
            if ind==1:
                disp_doc_id = int(val)
            x.append(abs(hash(event_header[ind] + '_' + val)) % D)

        if (ad_doc_id in leak_uuid_dict) and (uuid_val in leak_uuid_dict[ad_doc_id]):
            x.append(abs(hash('leakage_row_found_1'))%D)
        else:
            x.append(abs(hash('leakage_row_not_found'))%D)

#        x_scale = scale(x)
            
        yield t, disp_id, ad_id, x, y

def _indices(x):
    ''' A helper generator that yields the indices in x

        The purpose of this generator is to make the following
        code a bit cleaner when doing feature interaction.
    '''

    # first yield index of the bias term
    yield 0

    # then yield the normal indices
    for index in x:
        yield index

def predict(x):
    ''' Get probability estimation on x

        INPUT:
            x: features

        OUTPUT:
            probability of p(y = 1 | x; w)
    '''

    # parameters
    alpha = 0.05
    beta = 0.5
    L1 = 1.0
    L2 = 0.

    # model
    n = f_n
    z = f_z
    w = {}

    # wTx is the inner product of w and x
    wTx = 0.
    for i in _indices(x):
        sign = -1. if z[i] < 0 else 1.  # get sign of z[i]

        # build w on the fly using z and n, hence the name - lazy weights
        # we are doing this at prediction instead of update time is because
        # this allows us for not storing the complete w
        if sign * z[i] <= L1:
            # w[i] vanishes due to L1 regularization
            w[i] = 0.
        else:
            # apply prediction time L1, L2 regularization to z and get w
            w[i] = (sign * L1 - z[i]) / ((beta + sqrt(n[i])) / alpha + L2)

        wTx += w[i]

    # cache the current w for update stage
    f_w = w

    # bounded sigmoid function, this is the probability estimation
    return 1. / (1. + exp(-max(min(wTx, 35.), -35.)))


with open(submission, 'w') as outfile:
    outfile.write('display_id,ad_id,clicked\n')
    for t, disp_id, ad_id, x, y in data(test, D):
        p = learner.predict(x)
        outfile.write('%s,%s,%s\n' % (disp_id, ad_id, str(p)))
        if t%1000000 == 0:
            print("Processed : ", t, datetime.now())
        if t ==300000:
            break
