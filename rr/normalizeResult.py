'''
make the clicked to 1 with the highest propability ad_id in the same display_id

author: sun
date: 2017-7-7
'''
import csv

import ipdb

resultFile = "/data/pythonsolution/trunoutput/sub_proba_test.csv"
resultFile2 = "/data/pythonsolution/trunoutput/sub_proba_test_flip_0.5.csv"
newResultFile = "/data/pythonsolution/trunoutput/new_test.csv"
newResultFile2 = "/data/pythonsolution/trunoutput/new_test_flip.csv"

def normalize(resultFile, newResultFile):
    f = open(resultFile)
    lines = len(f.readlines())
    print lines
    f.close()

    fout = open(newResultFile, 'w')
    with open (resultFile) as infile:
        tmpdict = []
        content = csv.reader(infile)
        header = next(content)
        fout.write(str(header[0])+"," + str(header[1])+","+str(header[2])+"\n")
        tmp = next(content)
        tmpdict.append(tmp)

        for ind, row in enumerate(content):
            if ind%100000 == 0:
                print "normalize data ", ind
            if int(tmp[0]) == int(row[0]):
                tmpdict.append(row)
                tmp = row
#                if ind == 27:
#                    ipdb.set_trace() 
                if ind == lines - 3:
                    compare(tmpdict, fout)
                    del tmpdict
                    fout.close()
                    print "done!"
            else:
                compare(tmpdict, fout)
                tmp = row
                del(tmpdict)
                tmpdict = []
                tmpdict.append(tmp)
                
def compare(tmpdict, fout):
    max = tmpdict[0][2]    
    maxIndex = 0
    for i in range(1, len(tmpdict)):
        if tmpdict[i][2] > max:
            max = tmpdict[i][2]
            maxIndex = i
    
    for i in range(len(tmpdict)):
        if i == maxIndex:
            tmpdict[i][2] = 1
        else:
            tmpdict[i][2] = 0
    
        fout.write(str(tmpdict[i][0]) + "," + str(tmpdict[i][1]) + "," + str(tmpdict[i][2]) + "\n")
            
if __name__ == '__main__':
    normalize(resultFile, newResultFile)
    normalize(resultFile2, newResultFile2)
