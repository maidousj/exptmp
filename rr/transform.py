'''
Change column 'clicked' to be random response
by a flip method
'''

import numpy as np
import pdb
import sys
from random import SystemRandom

p = 0.5
fileName = "/data/pythonsolution/truncate/train.csv"
prob_f = 0.5
fileChangedName = "/data/pythonsolution/truncate/train_flip_0.5.csv"

def trans():
    changedCount = 0
    f = open(fileName, 'r')
    fChanged = open(fileChangedName, 'w')
    #fChanged.write(f.readline)
    #sizehint = 209715200
    #arr = f.readlines()
    #fChanged.write(arr[0]) 
    #lines = arr[1:]
    title = True
    try:
        for line in f:
            if title:
                fChanged.write(line)
                title = False
                continue
#            print 'orign', line
            l = line.split(',')
            #print 'before',l
            before = int(l[2])

            secureRandom(prob_f, l)
            #print 'after random', l
            after = int(l[2])
            if before != after:
                changedCount = changedCount + 1
            
            delimiter = ','
            s = delimiter.join(l)
#            print 'final', s
            fChanged.write(s)
    except:
        print "can't conver to integer"
    finally:
        f.close()
        fChanged.close()
    return changedCount

# num is list

def secureRandom(prob, num):
    if not isinstance(num, list):
        return None
    rand = SystemRandom()
    randValue = rand.random()

    if randValue < (prob * p): 
        #print 'set 1', randValue
        num[2] = '1\n'
    elif (randValue > (prob * p)) and (randValue < (1 - prob)):
        #print 'set 0', randValue
        num[2] = '0\n'
    elif randValue > (1 - prob):
        #print 'stay unchange', randValue
        pass
    else:
        print 'It can not happen!'
    return randValue

if __name__ == '__main__':
    print trans()
