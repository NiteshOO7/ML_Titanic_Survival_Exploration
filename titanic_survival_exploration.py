# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 12:38:18 2018

@author: nitesh.yadav
"""
import pandas as pd

def DataLoad():
    """ loads data from CSV file """
    try:
        full_data = pd.read_csv(r"C:\Users\nitesh.yadav\Desktop\titanic_survival_exploration\titanic_data.csv")
        features = full_data.drop('Survived', axis = 1)
        labels = full_data['Survived']
        print("Titanic Servival dataset has {} data points with {} variables each.".format(*full_data.shape))
    except FileNotFoundError:
        print("File 'titanic_survival_exploration.csv' does not exist, please check the provided path.")
    return full_data, features, labels

def Accuracy_score(truth, prediction):
    """ Returns accuracy score for input truth and predictions. """
    if len(truth) == len(prediction):
        return "Predictions have an accuracy of {:.2f}%.".format((truth == prediction).mean() * 100)
    else:
        return "Number of predictions don't match with outcomes!"
    
def Predicton_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """
    predictions = []
    for _, passenger in data.iterrows():
        predictions.append(0)
    return pd.Series(predictions)

def Prediction_1(data):
    """ Model with one feature:
        - Predict a passenger survived if they are female. """
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':     
            predictions.append(1)
        else:
            predictions.append(0)
    return pd.Series(predictions)

def Prediction_2(data):
    """ Model with two features: 
        - Predict a passenger survived if they are female.
        - Predict a passenger survived if they are male and younger than 10. """
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger['Age'] <= 10:
            predictions.append(1)
        else:
            predictions.append(0)
    return pd.Series(predictions)

def Prediction_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger['Age'] <= 18:
            predictions.append(1)
        else:
            predictions.append(0)
    return pd.Series(predictions)

    

    
