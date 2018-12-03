# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 12:37:08 2018

@author: nitesh.yadav
"""
import titanic_survival_exploration as tse
import pandas as pd
import numpy as np
import visuals as vs

def main():
    # load data from csv file
    full_data, features, labels = tse.DataLoad()
    # Test the 'accuracy_score' function
    predictions = pd.Series(np.ones(5, dtype = int))
    print(tse.Accuracy_score(labels[:5], predictions))
    # Make the predictions
    predictions = tse.Predicton_0(features)
    # whether the feature Sex has any indication of survival rates 
    vs.survival_stats(features, labels, 'Sex')
    # Make the predictions
    predictions = tse.Prediction_1(features)
    print(tse.Accuracy_score(labels, predictions))
    
    vs.survival_stats(features, labels, 'Age', ["Sex == 'male'"])
    # Make the predictions
    predictions = tse.Prediction_2(features)
    print(tse.Accuracy_score(labels, predictions))
    
    vs.survival_stats(features, labels, 'Age', ["Sex == 'male'", "Age <= 18"])
    # Make the predictions
    predictions = tse.Prediction_2(features)
    print(tse.Accuracy_score(labels, predictions))
      
if __name__ == "__main__":
    main()
    
