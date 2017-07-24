import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

import ipdb

pandas2ri.activate()

readRDS = robjects.r['readRDS']
df = readRDS('~/Documents/clickPrediction/input/000.rds')
df = pandas2ri.ri2py(df)
for x in df:
    ipdb.set_trace(context=5)
    print x
# do something with the dataframe
