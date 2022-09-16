import numpy as np
import csv
import pandas as pd


train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# data cleaning
def data_clean(data):
    # No use : 'PassengerId' 'Name' 'Ticket' 'Cabin'
	data = data.drop(['PassengerId'], axis=1)
	data = data.drop(['Name'], axis=1)
	data = data.drop(['Ticket'], axis=1)
	data = data.drop(['Cabin'], axis=1)

    # change sex to 0(female) or 1(male)
	data['Sex'] = pd.to_numeric(data['Sex'].str.replace("female", '0').replace("male", '1'))

    # Age 補 median
	data['Age'] = data['Age'].fillna(data['Age'].median())

    # Fare 補 mean
	data['Fare'] = data['Fare'].fillna(data['Fare'].mean())

    # Embarked: NaN S=1, C=2, Q=3
	data['Embarked'] = data['Embarked'].fillna("1")
	data['Embarked'] = pd.to_numeric(data['Embarked'].str.replace("S", '1').replace("C", '2').replace("Q", '3'))

	return data

Train = data_clean(train_data)
Test = data_clean(test_data)

# print(Test)

print(Train.isnull().sum())
# Train.info()
# print(Train.columns)
# print(Test.columns)