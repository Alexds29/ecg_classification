import pandas as pd
from sklearn.model_selection import train_test_split

def read_split():
    
    X = pd.read_csv('C:\\Users\\Alex_DS\\Datascientist\\ECG_new_forward\\Documents\\X.csv', index_col = 'Unnamed: 0')
    Y = pd.read_csv('C:\\Users\\Alex_DS\\Datascientist\\ECG_new_forward\\Documents\\Y.csv', index_col = 'Unnamed: 0')

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42, stratify = Y)
    
    return X_train, Y_train, X_test, Y_test