from marshmallow import Schema, fields
from marshmallow.validate import Length

class PostulationSchema(Schema) :
    student = fields.Dict(required=True)
    date = fields.DateTime(required=True)
    postulator = fields.Dict(allow_none=True)
    description = fields.Str(required=True, validate=Length(min=20, max=200))
    
class PostulateSchema(Schema):
    student = fields.Dict(required=True)
    isActive = fields.Bool(required=True)
    
class FilterPostulation(Schema):
    code = fields.Str(required=True, validate=Length(equal=7))