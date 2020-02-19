# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:44:14 2020

@author: Ellen Wang
"""
from sklearn import datasets
centers=[(-5,-5),(0,0),(5,5)]
X,y=datasets.make_blobs(n_samples=5000,n_features=2,cluster_std=1.0,\
                        centers=centers,shuffle=False,random_state=30)
n_samples=5000
y[:n_samples//2]=0