import pandas as pd

from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.pipeline import Pipeline

# ***************************************************************

class FIT (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = True):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        
        
        if self.remove_origin:
            pass
        
        return X
    
#  ***************************************************************************
    
    
myPipe = Pipeline([('FN', FN()), 
                   ('Bt', Bt()),
                   ('SmCl', SmCl()),
                   ('Gnd', Gnd()),
                   ('Rht', Rht())
                   ])