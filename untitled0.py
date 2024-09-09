# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:17:01 2023

@author: Lenovo
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('veriler_filtre.csv',low_memory=False)
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
print(x)
print(y)

from sklearn.preprocessing import LabelEncoder
kategorik_sutunlar = dataset.iloc[:, [4, 5, 6, 45]]

# LabelEncoder kullanarak sayısallaştırma
label_encoder = LabelEncoder()
for sutun in kategorik_sutunlar.columns:
    dataset[sutun] = label_encoder.fit_transform(dataset[sutun])
# Dönüştürülmüş veriyi gösterme
print(dataset.head())

# Veri setini tekrar kaydetme
dataset.to_csv("sayisallasan.csv", index=False)

newds=pd.read_csv('sayisallasan.csv')
x=newds.iloc[:,:-1].values
y=newds.iloc[:,-1].values

import pandas as pd
from sklearn.preprocessing import StandardScaler


# Verileri ölçeklendirme
scaler = StandardScaler()
X_std = scaler.fit_transform(x)

# Ölçeklenmiş verileri kullanarak analiz yapabilirsiniz
# Örneğin, X_std ve y'yi kullanarak bir makine öğrenmesi modeli eğitebilirsiniz


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(X_std,y,test_size=0.2,random_state=(0))


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
# Random Forest modelini eğitme
random_forest_model = RandomForestClassifier(random_state=42)
random_forest_model.fit(x_train, y_train)

# Random Forest modelinin başarı oranını değerlendirme
y_pred_rf = random_forest_model.predict(x_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print("Random Forest Başarı Oranı:", accuracy_rf)

# Support Vector Classifier (SVM) modelini eğitme
svm_model = SVC(random_state=42)
svm_model.fit(x_train, y_train)

# SVM modelinin başarı oranını değerlendirme
y_pred_svm = svm_model.predict(x_test)
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print("SVM Başarı Oranı:", accuracy_svm)





