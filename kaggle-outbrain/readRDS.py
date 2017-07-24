import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

import ipdb

fileName = '/data/rds/baseline_1/test/000.rds'
#fileName = '/data/rds/clicks.rds'

pandas2ri.activate()

readRDS = robjects.r['readRDS']
df = readRDS(fileName)
df = pandas2ri.ri2py(df)

ipdb.set_trace()

print df[1]
print df[2][0]
print df[2][5]
print df[2][6]

#for x in df:
#    ipdb.set_trace(context=5)
#    print x
# do something with the dataframe
