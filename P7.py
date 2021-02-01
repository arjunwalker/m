import numpy as np
import pandas as pd
import csv
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

lines = list(csv.reader(open('data7_names.csv', 'r')))
attributes = lines[0]

heartDisease = pd.read_csv('data7_heart.csv' , names=attributes)
heartDisease = heartDisease.replace('?' , np.nan)

print('few examples from the dataset are given below')
print(heartDisease.head())
print('\nAttributes and datatypes')
print(heartDisease.dtypes)

model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'),('sex', 'trestbps'), ('exang', 'trestbps'),('trestbps', 'heartdisease'), ('fbs', 'heartdisease'),('heartdisease', 'restecg'),('heartdisease', 'thalach'),('heartdisease', 'chol')])


print('\nlearning cpds using maximum likelihood estimators');
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)

print('\ninferencing with bayesian network')
HeartDisease_infer = VariableElimination(model)
print('\n1.probability of heartdisease given age=40')
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age':40})
print(q['heartdisease'])
print('\n2.probability of heartdisease given chol (cholestronal) =100')
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'chol': 50})
print(q['heartdisease'])