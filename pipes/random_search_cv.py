from scipy.stats import uniform, randint
from sklearn.model_selection import RandomizedSearchCV
#from sklearn.model_selection import GridSearchCV
#from sklearn.ensemble import GradientBoostingClassifier
#from sklearn.svm import SVC
#from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import Pipes.train_test_split as tts

X_train, Y_train, _, __ = tts.read_split()

def random_search(model, model_params):

    search = RandomizedSearchCV(model, param_distributions=model_params, n_iter=200, cv=5, verbose=True, n_jobs=1,  return_train_score=True, scoring = 'f1_micro')
    search.fit(X_train, Y_train)
    print(f'Лучшие параметры модели: {search.best_params_}')
    print(f'Лучший показатель точности модели: {search.best_score_}')