from fastapi import FastAPI, HTTPException
from .schemas.data_validation import getPredValidation
from sklearn.preprocessing import LabelEncoder
from joblib import Parallel, delayed 
import joblib

app = FastAPI()

#Loading the model 
model_path = r"model/nba_knn.joblib"
with open(model_path, "rb") as data:
    knn = joblib.load(data)
label_path = r"model/position_labels.joblib"
with open(label_path, "rb") as data:
    position_labels = joblib.load(data)


@app.post("/predict")
def predict(data: getPredValidation):
    try:
        test_data = [[
            data.AST,
            data.STL,
            data.BLK,
            data.TRB,
            data.FGA,
            data.FG_PERCENTAGE,
            data.THREE_P,
            data.THREE_PA,
            data.PF,
            data.eFG_PERCENTAGE, 
            data.FT_PERCENTAGE, 
            data.DRB,
            data.THREE_P_PERCENTAGE, 
            data.TWO_P,
            data.TWO_P_PERCENTAGE, 
        ]]
        prediction = knn.predict(test_data)[0]

        return {'prediction': str(position_labels[prediction])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occured: {e}")
