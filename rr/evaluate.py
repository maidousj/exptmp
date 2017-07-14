'''
Usage: to evaluate the prediction result
        precision_score, recall_score, f1_score

Author: Sun
Date: 2017-7-14
'''

import csv
from sklearn import metrics

def loadFile(fileName):
    ret = []
    with open(fileName) as infile:
        content = csv.reader(infile)
        header = next(content)
        
        for ind, row in enumerate(content):
            if ind%100000 == 0:
                print ("load {} {} rows".format(fileName, ind))
            ret.append(int(row[2]))

    return ret

def evaluate(actual, predictFileName):
    predict = loadFile(predictFileName)
    
    print ("precision_score:\n for {} = {}".format(predictFileName, metrics.precision_score(actual, predict)))
    print ("recall_score:\n for {} = {}".format(predictFileName, metrics.recall_score(actual, predict)))
    print ("f1_score:\n for {} = {}".format(predictFileName, metrics.f1_score(actual, predict)))

if __name__ == '__main__':
    actFileName = "/data/pythonsolution/trunoutput/test.csv"
    preFileName = "/data/pythonsolution/trunoutput/new_test.csv"
    preFlipFileName = "/data/pythonsolution/trunoutput/new_test_flip.csv"
    actual = loadFile(actFileName)
    evaluate(actual, preFileName)
    evaluate(actual, preFlipFileName)
