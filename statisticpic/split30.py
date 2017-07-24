'''
make index for train file so that we can split it fast
Date: 2017-07-24 20:37
'''

import pandas as pd
import csv
import random
import ipdb

def random_without_same(min_v, max_v, num):
    temp = range(min_v, max_v)
    random.shuffle(temp)
    return temp[0:num], temp[num:]

### extract data from df(a dataframe) and construct a list
def extract(key, start, end, df):
    arr = []
    for i in range(start, end): 
        if int(df['display_id'][i]) == int(key):
            arr.append(list(df.loc[i]))  
        else:
            break
    return arr, i

def df2dic(df, maxValue):
    dic = {}
    end = len(df) 
    start = 0

    for key in range(1, maxValue):
        arr, start = extract(key, start, end, df)
        dic[key] = arr
    return dic
    
def writeFile(outfile, dic):
    for line in dic:
        outfile.write(",".join(str(e) for e in line) + '\n')

if __name__ == '__main__':
    maxValue = 16874594 # max value in file +1
#    maxValue = 11
    num = 11820618
    infile = '/data/input/clicks_train.csv'
    outTrain = '/data/pythonsolution/input/train.csv'
    outTest = '/data/pythonsolution/input/test.csv'

    df = pd.read_csv(infile)
    dic = df2dic(df, maxValue)
#    print dic

    tmp1, tmp2 = random_without_same(1, maxValue, num)

    with open (outTrain, 'w') as outfile:
        outfile.write('display_id,ad_id,clicked\n')
        for i in tmp1:
            print("write displayid = {} in {}".format(i, outTrain))
            writeFile(outfile, dic[i])

    with open (outTest, 'w') as outfile:
        outfile.write('display_id,ad_id,clicked\n')
        for i in tmp2:
            print("write displayid = {} in {}".format(i, outTest))
            writeFile(outfile, dic[i])
