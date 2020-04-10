#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Here we want to generate a network into a json file
import pandas as pd 
from datetime import date  
import math
from Config.myConfigs import path
import numpy as np

# Path to file change where your clin data file is
clinFile = "bomiRNA-seq.csv"

# Read file with separator ;
clinData = pd.read_csv(path+clinFile,sep=';') 

# get a test dataframe from the 
testData = clinData[1:101].set_index('genes')
testData = testData.transpose().corr().abs()
testData[testData < .5] = 0
testData = testData.mask(np.tril(np.ones(testData.shape, dtype=np.bool_)))
testData = testData.fillna(0)


# If two genes correlates over some cutoff we want to store that connection in 
# a new dataframe
# |  gene1   |    gene2    |   correlationValue   |
# we then want to make:
# elements: [
#               # these we get from unique values of gene lists added together        
#               { data: { id: 'gene1' } },
#               { data: { id: 'gene2' } },
#               { data: { id: 'geneother' } },
#             {
                # these we get from the new dataframe
#               data: { id: 'someSmartId', source: 'gene1', target: 'gene2'}},
#               {data: { id: 'someOtherSmartId', source: 'gene2', target: 'geneOther' }
#             },
#           ]

