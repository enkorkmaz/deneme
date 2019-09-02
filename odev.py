# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:55:01 2019

@author: ekorkmaz
"""
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt 
from scipy import stats
import statsmodels.stats.api as sms
import scipy.stats as st
import statistics as ist
import math as mt

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

data = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])


anakitle = np.random.poisson(20,size=[10000]) # dagilimdan ornek al
#poisson dagilim da verinin ortalamasi ile dagilim grafigi cizilir 
#dagilima parametre olarak verinin ortalamasi verilir.

class veriAnalizi(object):
    
    def __init__(self,anakitle):
        
        self.anakitle=anakitle
        std=0
        medyan=0
        ortalama=0
        pdf=0
        cdf=0
        p1=0
        x=0
    
    def poisson(self,lambd,x):
#lambd, o olayın ortalama olarak ne kadar oldugudur
#x ,o olayın olmasını istedigimiz sayıdır.
#lambda ise o olayın x kadar olmasının olasılıgını verir.
        
        return (mt.exp(-lambd)*(lambd ** x)) /mt.factorial(x)
    
    
    
    def std(self):
        self.std=anakitle.std()
        print (self.std)
    
    def medyan(self):
        self.medyan=ist.median(anakitle)
        print( self.medyan)
    
    def ortalama(self):
        self.ortalama=anakitle.mean
        print(self.ortalama)
      
        
        
    def pdf(self,a):
        self.pdf=stats.norm(0,0.1).pdf(a)
        print(self.pdf)
 #pdf; bu dagilim üzerindeki bir noktanın dagılımdaki cıktısıdır yani y degeridir yani fonksiyon sonucudur.   
 #probobality p.. function 
 #normal dagılım fonksiyonuna ortalama,standart sapma ve istedigimiz x degerini verince pdf i elde ederiz.
    def cdf(self,ort):
        
        p1=poisson(10,3)
        n =10
        x = np.linspace(0,n,n+1)  #0dan n e kadar n+1 tane veri uretir
        cdf1=np.array([p1.cdf(i) for i in x ])
        print(cdf1)
        
#cdf(5) dedigimizde dagılımın x="5" degerine kadar olan alanın toplamıdır.
# o fonksiyonun o x noktasına kadar olan alanın (grafigin altında kalan alanın)toplamdırı
    def guvenAraligi(self):
        print(st.t.interval(alpha=0.95,df=len(anakitle)-1,loc=np.mean(anakitle),scale=st.sem(anakitle)))
        
        
        
        
        
        
        
        

