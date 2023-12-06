import pandas as pd
import numpy as np
import json
beta=[]
burr=[]
norm=[]
lognorm=[]
gamma=[]
excel = pd.read_excel('wind_distribution.xlsx')
for i in range(0,len(excel)):
    c = excel['fitting_distr'][i][2:6]
    if c == 'burr':
        burr.append(c)
    elif c== 'beta':
        beta.append(c)
    elif c== 'norm':
        norm.append(c)
    elif c== 'logn':
        lognorm.append(c)
    else:
        gamma.append(c)
wind_dist_percentage={}
wind_dist_percentage['beta']=beta
wind_dist_percentage['gamma']=gamma
wind_dist_percentage['norm']=norm
wind_dist_percentage['lognorm']=lognorm
wind_dist_percentage['burr']=burr

import json
with open('wind_dist_percentage.txt','w') as fp:
    json.dump(wind_dist_percentage,fp)