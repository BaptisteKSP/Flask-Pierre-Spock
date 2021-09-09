from flask import Flask, request
from flask_restx import Resource, Api
import pierre_spoke

app = Flask(__name__)
api = Api(app)
#begin = Begin()

#param dans l'url
@api.route('/plus_one/<x>')
class PlusOne(Resource):
    def get(self, x):
        x = int(x)
        return {"x" : x+1}

#param dans QS
@api.route('/square')
@api.doc(params={"x": "Must be an integer"}, location="query")
class Square(Resource):
    def get(self):
        x = int(request.args.get('x', 5))
        return{"x" : x*x}

@api.route('/spock/')
@api.doc(params={"x": "Must be an integer"}, location="query")
class Spock(Resource):
    def get(self):
        x = int(request.args.get('x', 0))
        result = pierre_spoke.Begin(x)
        return result



@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)