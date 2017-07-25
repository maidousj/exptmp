'''
make index for train file so that we can split it fast
Date: 2017-07-24 20:37
'''

import pandas as pd
import csv
import random
from datetime import datetime
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
        print "construct dict ", key
        arr, start = extract(key, start, end, df)
        dic[key] = arr
    return dic
    
def writeFile(outfile, dic):
    for line in dic:
        outfile.write(",".join(str(e) for e in line) + '\n')


if __name__ == '__main__':
#    maxValue = 16874594 # max value in file +1
    maxValue = 1932987+1 # max value in file +1
#    maxValue = 11
    num = int(maxValue*0.7)
    infile = './train.csv'
    outTrain = '/tmp/train.csv'
    outTest = '/tmp/test.csv'

    print "random shuffle array..."
    tmp1, tmp2 = random_without_same(1, maxValue, num)

    print "load file..."
    df = pd.read_csv(infile)

    outTrainfile = open (outTrain, 'w') 
    outTestfile = open (outTest, 'w') 
    outTrainfile.write('display_id,ad_id,clicked\n')
    outTestfile.write('display_id,ad_id,clicked\n')

    for i in range(len(df)):
        display_id = df['display_id'][i]

        if i%1000 == 0:
            print("Processed : ", i, datetime.now())

        line = list(df.loc[i])
        if display_id in tmp1:
            outTrainfile.write(",".join(str(e) for e in line) + '\n')
        elif display_id in tmp2:
            outTestfile.write(",".join(str(e) for e in line) + '\n')
        else:
            print("bullshit : line num = {}, line = {} ".format(i, line)) 

    outTrainfile.close()
    outTestfile.close()
