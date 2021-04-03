from flask import Flask, request
from flask_restplus import Api, Resource
from config import app, api, name_space
from logic import GenresLogic
import werkzeug

from serializers import GenreSchema
werkzeug.cached_property = werkzeug.utils.cached_property


@name_space.route("/genres")
class Genres(Resource):
    def get(self):
        data = GenresLogic.get_all_genres()
        genres = GenreSchema(many=True).dump(data)
        return genres, 200

    def post(self):
        data = request.get_json()

        genre = GenresLogic.create(data)

        if genre:
            genre = GenreSchema().dump(genre)

        return client, 201

api.add_resource(Genres, '/genres')

if __name__ == '__main__':
    app.run(debug=True)