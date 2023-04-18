import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import gzip

dataframe = pd.read_csv('./data/truck_list_v_best.csv', names=['list_price', 'best_price'], header=0)
dataframe['list_price'] = dataframe['list_price'] * 1000
dataframe['best_price'] = dataframe['best_price'] * 1000

x_train, x_test, y_train, y_test = train_test_split(np.array(dataframe['list_price']), np.array(dataframe['best_price']), test_size=.3, random_state=42)

pipe = Pipeline([('model', LinearRegression())])

pipe.fit(x_train.reshape(-1,1), y_train)

predictions = pipe.predict(x_test.reshape(-1,1))

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
print({"R2": r2, "MAE": mae, "MSE": mse})

# Export model
joblib.dump(pipe, gzip.open('model/model_binary.dat.gz', "wb"))