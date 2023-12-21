from http import HTTPStatus

from flask import Flask, request
from flask_restful import Resource, Api 

from models import Oppo

app = Flask(__name__)
api = Api(app)        

class Recommendation(Resource):

    def post(self):
        kriteria = request.get_json()
        kriteria_valid = ['brand','ram','prosesor','storage','baterai','harga','os']
        oppo = Oppo()

        if not kriteria:
            return 'kriteria is empty', HTTPStatus.BAD_REQUEST.value

        if not all([v in kriteria_valid for v in kriteria]):
            return 'kriteria is not found', HTTPStatus.NOT_FOUND.value

        recommendations = oppo.get_recs(kriteria)

        return {
            'alternatif': recommendations
        }, HTTPStatus.OK.value


api.add_resource(Recommendation, '/recommendation')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
