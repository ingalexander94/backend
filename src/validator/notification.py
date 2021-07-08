from marshmallow import Schema, fields
from marshmallow.validate import Length

class NotificationSchema(Schema):
    title = fields.Str(required=True)
    url = fields.Str(required=True)
    date = fields.DateTime(required=True)
    isActive = fields.Bool(required=True)
    codeReceiver = fields.Str(required=True, validate=Length(equal=7))