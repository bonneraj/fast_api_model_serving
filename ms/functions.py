import pandas as pd
from ms import model


def predict(X, model):
    prediction = model.predict(X)[0]
    return prediction


def get_model_response(input):
    X = pd.json_normalize(input.__dict__)
    prediction = predict(X, model)
    return {
        'prediction': round(float(prediction), 2)
    }