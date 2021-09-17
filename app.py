from flask import Flask # upper Case Flask always reporesent a class
from flask import jsonify # import method to convert to Jason
from flask import request # method used to get POST data
#create a class with unique name
app=Flask(__name__)
# %% Hello World Example
'''
# create an end point
@app.route('/') # 'http://71.185.227.158:5000/'
#create method
def home():
    return "Hello, World!"
app.run(port=5000) # run the rest-api
'''
# %% Server view
# POST  ---used to receive data
# Get   ---used to send data back only
stores=[
{
    'name':'my wonderful store',
    'items':[
        {'name':'Vick Item',
        'price': 15.99}
    ]
}
]

#GET /store
@app.route('/store/')#'http://71.185.227.158:5000/store/some_name'
def get_stores():
    #get all stores in the database
    return jsonify({'stores':stores})#store all stores list to dictionary then to jason format

#POST /store data:{name:}
@app.route('/store', methods=['POST'])#default is GET request
def create_store():
    request_data=request.get_json() # import data as dictionary
    new_store={
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>')#'http://71.185.227.158:5000/store/some_name'
def get_store(name):
    for store in stores:
        if store['name']==name: return jsonify(store)
    return jsonify({'message':'store not found'})


#POST /store/<string:name>/item {NAME:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data=request.get_json() # import data as dictionary
    for store in stores:
        if store['name']==name: 
            new_item={
                'name':request_data['name'],
                'price':request_data['price']
            }
            stores.append(new_item)
            return jsonify(new_item)    
    return jsonify({'message':'store not found'})    

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name']==name: return jsonify({'item':store['items']})
    return jsonify({'message':'store not found'})


app.run(port=5000)
# %%
