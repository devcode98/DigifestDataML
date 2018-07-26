import review_analysis as ra
from flask import *
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
api.add_resource(ra.func2())

if __name__ == '__main__':
      app.run();