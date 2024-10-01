from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import prediction

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
 
def wel(text):
    try:
        return {'Post Values': text}, 201
    
        data = request.get_json()
        predict = prediction.predict_mpg(data) 
        return {'predict':predict}, 201
    
    except Exception as error:
        return {'error': error}

api.add_resource(wel,'/getData/<string:text>')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)