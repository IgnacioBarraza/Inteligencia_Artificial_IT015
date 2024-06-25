import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#Cargar el dataset de Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

#Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Estandarizar las caracteristicas
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Crear y entrenar el modelo SVM
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

#Predecir las etiquetas para el conjunto de pruebas
y_pred = svm.predict(X_test)

#Evaluar un informe de clasificación
acc = accuracy_score(y_test, y_pred)

print(f"Exactitud con SVM: {acc:.2f}")
print("Informe de clasificación")
print(classification_report(y_test, y_pred))
print("Matriz de confusión")
print(confusion_matrix(y_test, y_pred))