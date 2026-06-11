import joblib
import numpy as np

model = joblib.load('./model/model.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

def predict_charges(smoker, age, bmi):
    """
    Predice los cargos de seguro para nuevos valores.

    Args:
        smoker (int): 0 for 'no' smoker, 1 for 'yes' smoker.
        age (int): Age of the individual.
        bmi (float): BMI of the individual.

    Returns:
        float: Predicted insurance charges.
    """
    new_data = np.array([[smoker, age, bmi]])
    scaled_new_data = sc_x.transform(new_data)
    scaled_prediction = model.predict(scaled_new_data)
    prediction = sc_y.inverse_transform(scaled_prediction)
    prediction_value = float(prediction[0][0])

    return round(prediction_value,2)