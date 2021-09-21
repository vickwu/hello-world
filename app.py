# %% Load package
from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from joblib import load
# import xgboost as xgb
# import pandas as pd
MODEL_DIR = 'model/'
MODEL_FILE = 'bst.joblib'
DICT_FILE = 'reason_dic.joblib'
SHAP_FILE = 'explainer.joblib'

# %% Load modeling and ARR info
MODEL_PATH=MODEL_DIR+MODEL_FILE
DICT_PATH=MODEL_DIR+DICT_FILE
SHAP_PATH=MODEL_DIR+SHAP_FILE
# Load model structure file
mdl= load(MODEL_PATH)
# load reason_code
reason_dict= load(DICT_PATH)
# Load SHAP value
explainer= load(SHAP_PATH)
# %% create service
app = Flask(__name__)
api = Api(app)
class prediction(Resource):
    def post(self):
        data=request.get_json()
        return data
    def get(self):
        return {'Message':'successfully deployed'}
# %% service online 
api.add_resource(prediction, '/')
# %%running
if __name__ == '__main__':
    app.run(port=5000)