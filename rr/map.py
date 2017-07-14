'''
calculate the mean average precision
MAP@12 =  $\frac{1}{|U|} \sum_{u=1}^{|U|} \sum_{k=1}^{min(12, n)} P(k)$
'''
import pandas as pd
import numpy as np

#resultFile = "/data/pythonsolution/trunoutput/sub_proba_test.csv"
#resultFlipFile = "/data/pythonsolution/trunoutput/sub_proba_test_flip_0.5.csv"
#resultFile = "/data/pythonsolution/trunoutput/new_test.csv"
#resultFlipFile = "/data/pythonsolution/trunoutput/new_test_flip.csv"
resultFile = "/data/pythonsolution/output/sub_proba_all.csv"

def calculateMAP(fileName):
    df = pd.read_csv(fileName)
    clicked = df['clicked'].groupby(df['display_id'])
    meanap = np.sum(clicked.mean())/len(clicked) 
    return meanap    

if __name__ == '__main__':
    print ("{} mean average precision = {}".format(resultFile, calculateMAP(resultFile)))
#    print ("{} mean average precision = {}".format(resultFlipFile, calculateMAP(resultFlipFile)))
