import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import joblib
import os

# Verileri yükle
data = pd.read_csv('one_hot_encoded_data.csv')  # Veri setinin adını doğru şekilde belirtmelisiniz

# Bağımsız değişkenler ve hedef değişkeni ayır
X = data.drop('fiyat', axis=1)
y = data['fiyat']

# Eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verileri ölçeklendir
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Farklı algoritmaları deneyerek model performansını değerlendir
models = {
    'LinearRegression': LinearRegression(),
    'SVR': SVR(),
    'DecisionTreeRegressor': DecisionTreeRegressor(),
    'RandomForestRegressor': RandomForestRegressor(),
    'GradientBoostingRegressor': GradientBoostingRegressor(),
    'KNeighborsRegressor': KNeighborsRegressor(),
    'MLPRegressor': MLPRegressor()
}

# Klasörü oluştur
os.makedirs('mLmodels', exist_ok=True)  # Klasör adını düzelttim

for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(model_name + ' MSE:', mse)

    # Eğitilmiş modeli kaydet
    joblib.dump(model, 'mLmodels/' + model_name + '_model.pkl')  # Klasör adını düzelttim
