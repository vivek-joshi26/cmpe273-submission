'''
DB
name: college
Table: students

id(Postgres
default
primary
key)
first_name(string)
last_name(string)
sjsu_id(string)
email(string)
create_timestamp
update_timestamp
'''

# Schema is used to validate the model attributes

from marshmallow import Schema, fields

# Below one is used for validation for the JSON data that will be used for student model
class StudentSchema(Schema):
    id = fields.Int()
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    sjsu_id = fields.Str(required=True)
    email = fields.Email()
    create_timestamp = fields.DateTime(format='timestamp')
    update_timestamp = fields.DateTime(format='timestamp')
