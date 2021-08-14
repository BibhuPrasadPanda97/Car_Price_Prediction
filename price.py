import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def price_prediction(pPrice, kmsDriven, noOfOwners, carAge, diesel, petrol, individual, manual):
    X = pd.read_csv('X_train.csv')
    y = pd.read_csv('y_train.csv')

    lgr = LinearRegression()
    lgr.fit(X,y)

    data_lst = [pPrice, kmsDriven, noOfOwners, carAge, diesel, petrol, individual, manual]
    dic = {}
    for i in range(len(X.columns)):
        dic[X.columns[i]] = data_lst[i]

    testing_df = pd.DataFrame(dic, index=[0])

    return round(lgr.predict(testing_df)[0][0],2)


'''
pPrice = float(input("Present Price:"))
kmsDriven = int(input("Kms Driven:"))
noOfOwners = int(input("No of Owners:"))
carAge = int(input("Car Age in Years:"))
diesel = int(input("Diesel(1/0):"))
petrol = int(input("Petrol(1/0):"))
individual = int(input("Individual(1/0):"))
manual = int(input("Manual(1/0):"))
'''

# output = price_prediction(pPrice, kmsDriven, noOfOwners, carAge, diesel, petrol, individual, manual)
# print("Selling Price of car:",output)
