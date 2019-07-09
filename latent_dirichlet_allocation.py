# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 06:30:49 2019

@author: frankbb
"""
import os
import sys
import re
import pandas as pd
import sklearn
import numpy as np
basedir = os.path.abspath(os.path.dirname(__name__))
print(basedir)
print('The scikit-learn version is {}.'.format(sklearn.__version__))

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation




class LatentDirichletAllocationClass:
    
    def import_data(self, file_name):
        out = pd.read_csv(file_name)
        return out
        
    def display_features_from_components(self, lda_components):
        for i, topic in enumerate(LDA.components_):
            print('The top 15 words for topic:#', i)
            print([cv.get_feature_names()[index] for index in topic.argsort()[-15:]])
            print('*'*50)
            
        
        
if __name__ =='__main__':
#    nrows=500
    data = 'npr.csv'
    Session_lda = LatentDirichletAllocationClass()
#    data = Session_lda.import_data(data)
#    
#    cv = CountVectorizer(max_df=0.9, min_df=2, stop_words='english')
#    '''
#    -max_df argument for the CountVec object ignores words with really high frequencies
#    0.9 will discard words that are contained withing 90% of the documents
#    -min_df is the min-document frequency, words that show up a min amount of times, with 
#    the number in min_df being 2, this means that the word cant be totally unique to a single article
#    '''
#    document_term_matrix = cv.fit_transform(data['Article'])
#    
#    LDA = LatentDirichletAllocation(n_topics=7, random_state=42)
#    LDA.fit(document_term_matrix)
#    
#    '''Grab the vocab of words'''
#    vocab = len(cv.get_feature_names())
#    test_word = cv.get_feature_names()[5000]
#    '''Grab the topics'''
#    len_lda_components = len(LDA.components_)
#    type_lda_components = type(LDA.components_)
#    shape_lda_coponents = LDA.components_.shape
#    '''Grab the highest probability of words per topic'''
#    single_topic = LDA.components_[0]#grab the first topic
#    top_ten_words = single_topic.argsort()[-10:]#returns the index positions that would sort this array, it shows us the location of the larger values
#    top_20_words = single_topic.argsort()[-20:]
    #from least to greatest
#    arr = np.array([10, 200, 1])
#    arr.argsort()#argsort returns array([2, 0, 1], dtype=int64), 2nd position was 1
    # the 0 th position was 10, and the 1st postion was 200, argsort orders thd nums

    
