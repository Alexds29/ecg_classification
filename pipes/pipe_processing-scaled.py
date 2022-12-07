import pandas as pd

from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# ***************************************************************

class FN (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = True):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        
        
        if self.remove_origin:
            X.drop(['FileName'], axis = 1, inplace = True)
        
        return X

#  ***************************************************************
    
class Bt (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = True):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        
        
        if self.remove_origin:
            X.drop(['Beat'], axis = 1, inplace = True)
        
        return X

#  ***************************************************************

class SmCl (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = True):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        
        
        if self.remove_origin:
            ind = X.loc[X['Rhythm'] == 'AVNRT'].index
            X = X.drop(ind, axis = 0)
            ind = X.loc[X['Rhythm'] == 'AVRT'].index
            X = X.drop(ind, axis = 0)
            ind = X.loc[X['Rhythm'] == 'SAAWR'].index
            X = X.drop(ind, axis = 0)
        
        return X    

#  ***************************************************************

class Gnd (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        X['Gender'] = X['Gender'].map({'FEMALE':0, 'MALE':1})
        
        
        if self.remove_origin:
            pass
            # Remove original fields
        
        return X  

#  ***************************************************************
    
class Rht (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        X['Rhythm'] = X['Rhythm'].map({'SB':0, 'SR':1, 'AFIB':2, 'ST':3, 'SVT':4, 'AF':5, 'SA':6, 'AT':7})
        
        
        if self.remove_origin:
            pass
            # Remove original fields
        
        return X    
    
#df.drop(['FileName'], axis = 1, inplace = True)
#df.drop(['Beat'], axis = 1, inplace = True)
#ind = df.loc[df['Rhythm'] == 'AVNRT'].index
#df = df.drop(ind, axis = 0)
#ind = df.loc[df['Rhythm'] == 'AVRT'].index
#df = df.drop(ind, axis = 0)
#ind = df.loc[df['Rhythm'] == 'SAAWR'].index
#df = df.drop(ind, axis = 0)

#df['Gender'] = df['Gender'].map({'FEMALE':0, 'MALE':1})
#df['Rhythm'] = df['Rhythm'].map({'SB':0, 'SR':1, 'AFIB':2, 'ST':3, 'SVT':4, 'AF':5, 'SA':6, 'AT':7})
    

#  ***************************************************************************
#  ***************************************************************************
#  ***************************************************************************
    
    
myPipe = Pipeline([('FN', FN()), 
                   ('Bt', Bt()),
                   ('SmCl', SmCl()),
                   ('Gnd', Gnd()),
                   ('Rht', Rht())
                   ('scaler', StandardScaler())
                   ])