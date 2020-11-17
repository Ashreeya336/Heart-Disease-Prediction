import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import log_loss
import warnings
warnings.simplefilter(action = "ignore", category= FutureWarning)

from sklearn.ensemble import GradientBoostingClassifier
def process():
    data = pd.read_csv("heart.csv")
   
    target=data["target"]
    data = data.drop(["target"],axis=1)

    
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=10)
   
    clfs = []
    kfolds = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)
    #np.random.seed(1)
    pipeline_svm = make_pipeline(SVC(probability=True, kernel="linear", class_weight="balanced"))
    grid_svm = GridSearchCV(pipeline_svm,
    param_grid = {"svc__C": [0.01, 0.1, 1]},
    cv = kfolds,
    verbose=1,
    n_jobs=-1)
    grid_svm.fit(x_train, y_train)
    grid_svm.score(x_test, y_test)
    print("\ Model: %f using %s" % (grid_svm.best_score_, grid_svm.best_params_))
    print("\n")
    print("SVM LogLoss {score}".format(score=log_loss(y_test, grid_svm.predict_proba(x_test))))
    clfs.append(grid_svm)
    
    joblib.dump(grid_svm, "heart_13.pkl")
    model_grid_svm = joblib.load("heart_13.pkl" )
    y_preds = model_grid_svm.predict(x_test)
    print("SVM accuracy score: ",accuracy_score(y_test, y_preds))
    
    #classifierGBo= GradientBoostingClassifier(n_estimators=500, learning_rate=1.0, max_depth=1)
    #classifierGBo.fit(x_train,y_train)
    #classifierGBo.score(x_test, y_test)
    #joblib.dump(grid_svm, "heart_13.pkl")




def check_input(value):
 df = pd.DataFrame(data=value, index=[0])
 process()
 model_grid_svm = joblib.load("heart_13.pkl" )
 op = model_grid_svm.predict(df)
 return (op[0])


