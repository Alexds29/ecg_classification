from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import Pipes.train_test_split_2 as tts

X_train, Y_train, _, __ = tts.read_split()

def grid_search(model, model_params):

    grid = GridSearchCV(model, model_params, cv=5, verbose=True, scoring = 'f1_micro')
    grid.fit(X_train, Y_train)
    print(f'Лучшие параметры модели: {grid.best_params_}')
    print(f'Лучший показатель точности модели: {grid.best_score_}')