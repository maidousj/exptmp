import numpy as np
from sklearn.metrics import roc_curve,auc
from sklearn.metrics import roc_auc_score
from sklearn.metrics import average_precision_score
from sklearn import metrics

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
import ipdb

#actualFileName = "/data/pythonsolution/output/test.csv"
#predictFileName = "/data/pythonsolution/output/sub_proba_test.csv"
#predictFileFlipName = "/data/pythonsolution/output/sub_proba_test_flip.csv"
#actualFileName = "/data/pythonsolution/trunoutput/test.csv"
#predictFileName = "/data/pythonsolution/trunoutput/sub_proba_test.csv"
#predictFileFlipName = "/data/pythonsolution/trunoutput/sub_proba_test_flip_0.5.csv"
actualFileName = "/data/pythonsolution/trunoutput/test.csv"
predictFileName = "/data/pythonsolution/trunoutput/new_test.csv"
predictFileFlipName = "/data/pythonsolution/trunoutput/new_test_flip.csv"


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

def drawPic(picName, title, xlabel, ylabel, x1, y1, x2, y2):
    plt.title(title)

#    length = len(xy)
#    cruve_color = ['b', 'g']
#    for i in range(length):
#        if i%2==0:
#            plt.plot(xy[i], xy[i+1], color=cruve_color[0])

#    plt.plot(x1, y1, 'b', label='AUC = %0.2f APS = %0.2f'% (roc_auc_orign,aps_orign))
#    plt.plot(x2, y2, 'g', label='AUC_FLIP = %0.2f APS = %0.2f'% (roc_auc_flip, aps_flip))
    
    plt.plot(x1, y1, 'bx--', label = 'normal')
    plt.plot(x2, y2, 'g', label = 'flip')

    plt.legend(loc='lower right')
    plt.plot([0,1],[0,1],'r--')
    plt.xlim([0.,1.])
    plt.ylim([0.,1.])
    plt.ylabel(xlabel)
    plt.xlabel(ylabel)

    plt.savefig(picName)


if __name__ == '__main__':
    actual = loadFile(actualFileName) 
    predictions = loadFile(predictFileName)
    predictionsByFlip = loadFile(predictFileFlipName)

#    false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
#    print "thresholds = ", thresholds, len(thresholds)
#    fpr, tpr, thd = roc_curve(actual, predictionsByFlip)
#    print "thd = ", thd, len(thd)

    picName = "roc_with_order_data.png"
    #drawPic(picName, 'Receiver Operating Characteristic', 'True Positive Rate', 'False Positive Rate', false_positive_rate, true_postive_rate, fpr, tpr)

    precision, recall, thresholds = metrics.precision_recall_curve(actual, predictions)
    print "thresholds = ", thresholds, len(thresholds)
    precision_flip, recall_flip, thresholds_flip = metrics.precision_recall_curve(actual, predictionsByFlip)
    print "thresholds_flip = ", thresholds_flip, len(thresholds_flip)
    drawPic('PRcruve.png', 'Precision recall cruve', 'Precision', 'Recall', precision, recall, precision_flip, recall_flip)

#roc_auc_orign = auc(false_positive_rate, true_positive_rate)
#roc_auc_flip = auc(fpr, tpr)

#ras_orign = roc_auc_score(actual, predictions)
#ras_flip = roc_auc_score(actual, predictionsByFlip)

#aps_orign = average_precision_score(actual, predictions)
#aps_flip = average_precision_score(actual, predictionsByFlip)
#print aps_orign, aps_flip

