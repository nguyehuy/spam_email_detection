# -*- coding: utf-8 -*-
"""vectorize.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NYiLoz27DYtRAB62IbYjlcgmHWX-fLWP
"""

# Vetorize the data :
# Xi = 1 is the i-th word (in vocabulary list) is in email and Xi=0 is the i-th word is not present in the email
class vectoreize(object):
    
    def __init__(self):
        pass
    def vectorize_feature(self, data, vocalList):
        import numpy as np
        X=[]
        for j in data:
            a=[]
            for i in range(len(vocalList)):
                if vocalList[i] in j:
                    a.append(1)
                else : a.append(0)
            X.append(a)
        return np.asarray(X)