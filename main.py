from flask import Flask, request
from  flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


videos = {}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        
        return


api.add_resource((Video, "/video/<int:video_id>"))


api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")

if __name__ == "__main__":
    app.run(debug=True)  # Only run in Development environment to test
