# -*- coding: utf-8 -*- 

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'帥哥': '偉宏', '正妹': '旻諺'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)