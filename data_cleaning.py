# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:26:00 2020

@author: Cody Smith
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df =  pd.read_csv('DataAnalyst.csv')

# Salary Parsing

df = df[df['Salary Estimate'] != '-1']
        
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['min_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[1]))
df['avg salary'] = (df.min_salary + df.max_salary)/2 


# Get company name text only

df['company text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

# State field

df['state'] = df['Location'].apply(lambda x: x.split(',')[1]) 

# Used to show which State has the most offerings
df.state.value_counts()

# Result: California with 626

df['state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis =1)



# Company Rating (Cleaned)
 

        