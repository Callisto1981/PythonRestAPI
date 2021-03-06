from flask import Flask
from  flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld (Resource):
    def get(self):
        return {"data": "Hello Wordld"}


api.add_resource(HelloWorld, "/helloWordl")

if __name__ == "__main__":
    app.run(debug=True) # Only run in Development environment to test
