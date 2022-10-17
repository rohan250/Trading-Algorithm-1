# Setup: Libraries
from algorithm import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import mean_squared_error as MSE

import sklearn as sk
import xgboost as xgb
import pandas as pd
import numpy as np

import QuantConnect
from Execution.ImmediateExecutionModel import ImmediateExecutionModel



def Initialize(self):
    self.SetStartDate(2012, 10, 17)     #Setting the start Date
    self.SetCash (100000)    #Setting the cash balance at the beginning of the strategy
