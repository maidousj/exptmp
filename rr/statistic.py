'''
Statistic 0s znd 1s
'''

import pdb

flipName = "/data/pythonsolution/truncate/train_flip_0.5.csv"
fileName = "/data/pythonsolution/truncate/train.csv"
testName = "/data/pythonsolution/truncate/test.csv"


def statistic(fileName):
    print "begin to statistic " + fileName
    title = True
    zeroCount = .0
    oneCount = .0
    f = open(fileName)
    
    try:
        for line in f:
            if title:
                title = False
                continue
            l = line.split(',')
            num = int(l[2])
            if num == 1:
                oneCount = oneCount + 1
            elif num == 0:
                zeroCount = zeroCount + 1
    
    except:
        print "can't convert to integer"
    finally:
        f.close
    
    print "zeros:", zeroCount, "ones:", oneCount, "all:", oneCount+zeroCount
    print oneCount/(oneCount+zeroCount)

if __name__ == '__main__':
    statistic(fileName)
#    statistic(testName)
#    statistic(flipName)
