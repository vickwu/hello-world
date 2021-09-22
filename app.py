# %% Load package
from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from joblib import load
import xgboost as xgb
import pandas as pd
import shap
MODEL_DIR = 'model/'
MODEL_FILE = 'bst.joblib'
DICT_FILE = 'reason_dic.joblib'
# %% Load modeling and ARR info
MODEL_PATH=MODEL_DIR+MODEL_FILE
DICT_PATH=MODEL_DIR+DICT_FILE

# Load model structure file
mdl= load(MODEL_PATH)
# load reason_code
reason_dict= load(DICT_PATH)
# Load SHAP value
explainer = shap.TreeExplainer(mdl)

# %% create service
app = Flask(__name__)
api = Api(app)
class prediction(Resource):
    def post(self):
        data=request.get_json()
        required_features=mdl.feature_names
        ordered_data={var:[data[var]] for var in required_features}
        X=pd.DataFrame.from_dict(ordered_data,orient='columns').astype(float)
        dX = xgb.DMatrix(X)
        preds = mdl.predict(dX)
        Score=int(preds[0]*10000)/100
        SHAP_VALUE=X.T
        shap_value = explainer(X)
        SHAP_VALUE['SHAP_contri']=list(shap_value[0].values)
        SHAP_VALUE['AAR']=SHAP_VALUE.index.map(reason_dict)
        SHAP_VALUE=SHAP_VALUE.sort_values(by='SHAP_contri', ascending=False)
        unique_code=list(SHAP_VALUE.AAR.drop_duplicates())
        return {'prediction(PD%)': Score,
        'reason_Code1':unique_code[0],
        'reason_Code2':unique_code[1],
        'reason_Code3':unique_code[2],
        'reason_Code4':unique_code[3]
        }
    def get(self):
        return {'Message':'successfully deployed'}
# %% service online 
api.add_resource(prediction, '/')
# %%running
if __name__ == '__main__':
    app.run(port=5000, debug=True)