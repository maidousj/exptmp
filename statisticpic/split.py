from sklearn.cross_validation import train_test_split
import numpy as np
import ipdb
import pandas as pd
from datetime import datetime


df = pd.read_csv("../input/clicks_traintmp.csv")
x = df.iloc[:,:3].values
#y = df.iloc[:,2].values

trainFile = "/data/pythonsolution/input/train_sorted.csv"
testFile = "/data/pythonsolution/input/test_sorted.csv"
testWithLabelFile = "/data/pythonsolution/input/testWithLabel_sorted.csv"
outTrain = open(trainFile, 'w')
#outTest = open(testFile, 'w')
outTestWithLabel = open(testWithLabelFile, 'w')

outTrain.write("display_id,ad_id,clicked\n")
#outTest.write("display_id,ad_id\n")
outTestWithLabel.write("display_id,ad_id,clicked\n")

x_train, x_test = train_test_split(x, test_size = 0.3)
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)
x_train = x_train.tolist()
x_test = x_test.tolist()

x_train.sort()
x_test.sort()
print "train", len(x_train)
print "test", len(x_test)

#ipdb.set_trace()

for i in range(len(x_train)):
    if i%100000 == 0:
        print "write train data", i, datetime.now()
    outTrain.write(str(x_train[i][0]) + ',' + str(x_train[i][1]) + ',' + str(x_train[i][2])+'\n')
outTrain.close()

#for i in range(len(x_test)):
#    outTest.write(str(x_test[i][0]) + ',' + str(x_test[i][1]) + '\n')
#outTest.close()

for i in range(len(x_test)):
    if i%100000 == 0:
        print "write test data ", i, datetime.now()
    ipdb.set_trace()
    outTestWithLabel.write(str(x_test[i][0]) + ',' + str(x_test[i][1]) + ',' + str(x_test[i][2])+'\n')
outTestWithLabel.close()

#def trainTestSplit(X,test_size=0.3):
#    X_num=X.shape[0]
#    train_index=range(X_num)
#    test_index=[]
#    test_num=int(X_num*test_size)
#    for i in range(test_num):
#        randomIndex=int(np.random.uniform(0,len(train_index)))
#        test_index.append(train_index[randomIndex])
#        del train_index[randomIndex]
#    train=X.ix[train_index] 
#    test=X.ix[test_index]
#    return train,test

