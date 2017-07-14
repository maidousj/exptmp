import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import ipdb

fileName = "sub_proba.csv"
fileNameFlip = "sub_proba_dp.csv"
mode = 'r'
resultName = "result"

def readFile(fileName, mode):
    arr = []
    with open(fileName, 'r') as inputfile:
        lines = inputfile.readlines()[1000:1100]
        for line in lines:
            try:
                clicked = float(line.split(',')[2]) 
                arr.append(clicked)
            except:
                print "can't conver to float"
    return arr

def drawTwo(y1, y2):
    if (len(y1) != len(y2)):
        return None    
    x = np.arange(len(y1))
#    plt.scatter(x, y1, marker="+")
#    plt.scatter(x, y2, marker="o")
    plt.plot(x, y1, color='r')
    plt.plot(x, y2, color='g')
    plt.savefig(resultName + "1000-1100_v1.png")
    #plt.show()

def draw(y):
    x = np.arange(len(y))
    plt.plot(x, y)
    plt.savefig("compare.png")

if __name__ == '__main__':
    y1 = readFile(fileName, mode)
    y2 = readFile(fileNameFlip, mode)
    v = list(map(lambda x: x[0]-x[1], zip(y2, y1)))  
    #print ("%s\n%s\n%s" %(y1, y2, v))
    #draw(v)
    drawTwo(y1, y2)
