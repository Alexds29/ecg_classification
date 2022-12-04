#import pandas as pd
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.linear_model import LogisticRegression
#from sklearn.svm import LinearSVC, SVC
#from sklearn.preprocessing import StandardScaler
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.linear_model import SGDClassifier
#from sklearn.ensemble import AdaBoostClassifier
#from sklearn.ensemble import GradientBoostingClassifier
#from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score, precision_score, recall_score


def fit_and_score_model(model, X_train, Y_train, X_test, Y_test):
    
    model.fit(X_train, Y_train)
    print(f'Точность модели на тестовом множестве : {round(model.score(X_test, Y_test), 3)}')
    print(f'Точность модели на тренировочном множестве: {round(model.score(X_train, Y_train), 3)}')
    print('******************************')
    pred = model.predict(X_test)
    print(f'Показатель модели f1: {round(f1_score(Y_test, pred, average = "micro"), 3)}')
    score = cross_val_score (model, X_train, Y_train, cv = 5)
    print(f'Показатель точности после кроссвалидации: {round(score.mean(), 3)}')