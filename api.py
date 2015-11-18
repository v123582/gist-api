# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_restful import Resource, Api
from geopy.geocoders import GoogleV3
geolocator = GoogleV3()
app = Flask(__name__)
api = Api(app)

@app.route('/show')
def show():
    return render_template('show.html')

class index(Resource):
    def get(self):
        return {'帥哥': '偉宏', '正妹': '旻諺'}

class gistApi(Resource):
    def get(self, source, target):
        (address,(latitude_s, longitude_s)) = geolocator.geocode(source)
        (address,(latitude_t, longitude_t)) = geolocator.geocode(target)
        return {'來源': [latitude_s, longitude_s], '目的': [latitude_t, longitude_t]}
        #return {'來源': source, '目的': target}



api.add_resource(index, '/')
api.add_resource(gistApi, '/<string:source>/<string:target>')


if __name__ == '__main__':
    app.run(debug=True)
