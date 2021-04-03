from marshmallow import fields, post_dump
from config import ma


class GenreSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
