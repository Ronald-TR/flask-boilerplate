from flask.views import View, MethodView
from flask import jsonify, request

 
class Hello(MethodView):
    methods = ['GET', 'POST']
   
    def get(self, id):
        result = {
            'id': id,
            'msg': 'default message GET success'
        }
        return jsonify(result)
    
    def post(self):
        result = {
            'id': '0',
            'msg': 'default message POST success'
        }
        return jsonify(result)
