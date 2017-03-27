
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 21:01:20 2016

@author: nancynan
"""
import numpy as np
import pandas as pd
#import stats
#import scipy
import matplotlib.pyplot as plt
import networkx as nx
#import csv
from scipy.stats import linregress
from pylab import *
#from pylab import plot, title, show , legend

df1= pd.read_csv("unemployment.csv")
df2= pd.read_csv("cc.csv")
df3= pd.read_csv("recession.csv")
df4= pd.read_csv("NPEmployment.csv")


#mat[mat<4]=0
#del mat['2.5']
#ele2 = ele[numpy.isfinite(ele['0'])]
#ele2=ele.dropna() 
recession=df3['Recession'].tolist()
unemployment=df1['UnempRate'].tolist()
cc=df2['ConsConf'].tolist()
NPEmployment=df4['NPEmployment'].tolist()

#un2=list(un.values)
#cc2=list(cc.values)
#recession2=list(recession.values)


#plt.plot(closeness_no_NaN,election_data_no_NaN,'o')

#p31 = numpy.asarray(mat1)
#za = (p31 <3).sum()
#slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)


scatter(recession,unemployment)
show()
(m,b)=polyfit(recession,unemployment,1)
print (m)
print (b)

yp=polyval([m,b],recession)
plot(recession,yp)
grid(True)
xlabel('recession')
ylabel('unemployment rate')
plt.title('$y=%3.7sx+%3.7s$'%(slope, intercept) )
show()
#b2=linregress(cc,unemployment)

#print (b1)
b2=linregress(recession,unemployment)
print (b2)
#b3=linregress(recession,NPEmployment)
#print (b3)
#b4=linregress(cc,NPEmployment)
#print (b4)

#title('Linear Regression Example')
#plot(cc,unemployment,'g.--')
#plot(recession,unemployment,'k.')
#plot(recession,NPEmployment,'r.-')
#legend(['original','plus noise', 'regression'])

#show()
#
#a3=linregress(degree_no_NaN,election_data_no_NaN)
#print (a3)