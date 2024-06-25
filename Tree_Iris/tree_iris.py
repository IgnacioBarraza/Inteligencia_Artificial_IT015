import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree

#Cargar el dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

#Dividier el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Crear y entrenat el modelo de árbol de decision
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

#Predecir las etiquetas para el conjunto prueba
y_pred = tree.predict(X_test)

#Evaluar el rendimiento del modelo
acc = accuracy_score(y_test, y_pred)
print(f"Exactitud con Árbol de decision: {acc:.2f}")

#Generar un informe de clasificación
print("Informe de clasificación:")
print(classification_report(y_test, y_pred))

#Matriz de confusión
print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))

#Visualizar el árbol de decisión
plt.figure(figsize=(20, 12))
plot_tree(tree, filled=True, rounded=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()