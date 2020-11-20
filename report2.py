
import pandas as pd
import xgboost as xgb
from matplotlib import pyplot as plt
from xgboost.sklearn import XGBClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost.sklearn import XGBClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns

s = pd.read_csv('survey1.csv')
s.head()

n = LabelEncoder()
for i in s.columns:
    s[i] = n.fit_transform(s[i].astype('str'))

X = s.drop(['treatment','benefits','wellness_program','seek_help','anonymity','supervisor',
            'comments', 'Timestamp'], axis=1)
y = s.treatment
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state=1000)
xgb = XGBClassifier(learning_rate =0.01, n_estimators=4000, max_depth=5,
                    min_child_weight=6, gamma=0, subsample=0.8,
                    objective='binary:logistic', nthread=4, scale_pos_weight=2,
                    seed=27)

xgb.fit(X_train,y_train)
y_pred = xgb.predict(X_test)
accuracy1 = accuracy_score(y_test, y_pred)
print('ACCURACY : ',accuracy1*100,'%')


features = X.columns
for name, importance in zip(features, xgb.feature_importances_):
    print(name, "=", importance)

fimp = xgb.feature_importances_
indices = np.argsort(fimp)
plt.title('Importance of features')
plt.barh(range(len(indices)), fimp[indices], color='r', align='center')
plt.yticks(range(len(indices)), features)
plt.xlabel('Relative Importance')
plt.show()
#
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
sns.heatmap(cm,annot=True,fmt='',cmap='Greens')
plt.title('Confusion Matrix')
plt.show()

