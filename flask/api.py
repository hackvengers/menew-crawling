import sys
sys.path.insert(0, '/root/menew-crawling/instagram-crawler')
from flask import Flask, request
from flask_restful import Resource, Api
import menew_crawling_info

app = Flask(__name__)
api = Api(app)

food_names = {}
# class CreateUser(Resource):
#     def post(self):
#         return {'status': 'success'}
class GetFoodName(Resource):
    def put(self,food_name):
        food_names[food_name] = request.form['data']
        return {food_name : food_names[food_name]}

api.add_resource(GetFoodName, '/<string:food_name>')



if __name__ == '__main__':
    print('app run')
    app.run(host='0.0.0.0',debug=True)
