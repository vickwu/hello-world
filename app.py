# %% Load package
from flask import Flask, request,jsonify
from flask_restful import Resource, Api
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