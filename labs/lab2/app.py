from apispec import APISpec
from apispec_fromfile import FromFilePlugin
from apispec_fromfile import from_file
from flask import Flask, jsonify
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from students.model import StudentSchema
from flasgger import Swagger

spec = APISpec(
    title="SJSU Student Registration API",
    version="0.0.1",    # our api version
    openapi_version="3.0.3",    # this is open api version
    plugins=[
        #FromFilePlugin("resource"),  # plugin that we will be using,
        FlaskPlugin(),
        MarshmallowPlugin()
    ],
)

app = Flask(__name__)
swagger = Swagger(app)  # use /apidocs

# we will be getting endpoints details from api.yml file, just like the yaml file we create for mulesoft
# Create API Endpoints

@app.route("/")
def index():
    return jsonify({"foo":"OK"})

@app.route("/spec")
def get_apispec():
    #return spec.to_yaml()
    return jsonify((spec.to_dict()))


@app.route("/students")
def get_students():
    #this is used to provide spec details for the openapi , the below details will be provided in the endpoints detail in the openapi
    """
    Get all SJSU students
    ---
    get:
        description: Get all students
        responses:
            200:
                content:
                    application/json:
                        schema : StudentSchema
    """
    student =  dict(first_name="Foo", last_name="Bar", sjsu_id="1234", email = "abc@sjsu.edu")
    return StudentSchema().dump(student)      # This is to validate with the model definition that we created



''' # Not working need to check, try to implement to read spec from yaml file
@from_file("spec/api.yml")
def index():
    return {"OK"}

'''
# to kill from terminal sudo lsof -t -i tcp:5000 | xargs kill -9
with app.test_request_context():
    spec.path(view = index)      # so for / index method will be called
    spec.path(view=get_students)    # if spec path is mentioned here then only that path will be shown in the openapi spec, it is like registering the end point
