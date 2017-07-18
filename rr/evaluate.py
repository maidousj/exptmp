'''
Usage: to evaluate the prediction result
        precision_score, recall_score, f1_score

Author: Sun
Date: 2017-7-14
'''

import csv
from sklearn import metrics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

def loadFile(fileName):
    ret = []
    with open(fileName) as infile:
        content = csv.reader(infile)
        header = next(content)
        
        for ind, row in enumerate(content):
            if ind%100000 == 0:
                print ("load {} {} rows".format(fileName, ind))
            if len(row[2]) == 1:
                ret.append(int(row[2]))
            else:
                ret.append(float(row[2]))

    return ret

def evaluate(actual, predictFileName):
    predict = loadFile(predictFileName)
    
    print ("precision_score:\n for {} = {}".format(predictFileName, metrics.precision_score(actual, predict)))
    print ("recall_score:\n for {} = {}".format(predictFileName, metrics.recall_score(actual, predict)))
    print ("f1_score:\n for {} = {}".format(predictFileName, metrics.f1_score(actual, predict)))

def reliabilityCruve(actual, predictions, predictionsFlip, picName):
    fig = plt.figure(1, figsize=(10, 10))
    ax1 = plt.subplot2grid((3, 1), (0, 0), rowspan=2)

    clf_score = metrics.brier_score_loss(actual, predictions, pos_label=1)
    clf_score_flip = metrics.brier_score_loss(actual, predictionsFlip, pos_label=1)

    fraction_of_positives, mean_predicted_value = calibration_curve(actual, predictions, n_bins=10)
    fraction_of_positives_flip, mean_predicted_value_flip = calibration_curve(actual, predictionsFlip, n_bins=10)

    ax1.plot(mean_predicted_value, fraction_of_positives, "s-", label="clf_score (%1.3f)" % (clf_score))
    ax1.plot(mean_predicted_value_flip, fraction_of_positives_flip, "r-", label="clf_score (%1.3f)" % (clf_score_flip))

    ax1.set_ylabel("Fraction of positives")
    ax1.set_ylim([-0.05, 1.05])
    ax1.legend(loc="lower right")
    ax1.set_title('Calibration plots  (reliability curve)')
    plt.savefig(picName)

def calKappa(actual, predictions):
    return metrics.cohen_kappa_score(actual, predictions)

def calConMatrix(actual, predictions):
    return metrics.confusion_matrix(actual, predictions)

if __name__ == '__main__':
    actFileName = "/data/pythonsolution/trunoutput/test.csv"
    preFileName = "/data/pythonsolution/trunoutput/new_test.csv"
    preFlipFileName = "/data/pythonsolution/trunoutput/new_test_flip.csv"
#    preFileName = "/data/pythonsolution/trunoutput/sub_proba_test.csv"
#    preFlipFileName = "/data/pythonsolution/trunoutput/sub_proba_test_flip_0.5.csv"

    actual = loadFile(actFileName)
    predictions = loadFile(preFileName)
    predictionsFlip = loadFile(preFlipFileName)

#    evaluate(actual, preFileName)
#    evaluate(actual, preFlipFileName)

#    reliabilityCruve(actual, predictions, predictionsFlip, "relCruve.png")

#print ("Kappa for {} is {}".format("normal predictions", calKappa(actual, predictions)))
#print ("Kappa for {} is {}".format("flip predictions", calKappa(actual, predictionsFlip)))

print ("Confusion Matrix for {} is {}".format("normal predictions", calConMatrix(actual, predictions)))
print ("Confusion Matrix for {} is {}".format("flip predictions", calConMatrix(actual, predictionsFlip)))
