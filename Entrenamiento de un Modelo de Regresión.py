from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

# Cargar el dataset
df = pd.read_csv("transporte_dataset.csv")

# Separar las características (X) y la variable objetivo (y)
X = df[["Origen", "Destino"]]
y = df["Costo"]

# Convertir las características categóricas en variables dummy
X = pd.get_dummies(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión Ridge
alpha = 0.1  # Factor de regularización
model = Ridge(alpha=alpha)
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular el error cuadrático medio
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio con Ridge:", mse)
