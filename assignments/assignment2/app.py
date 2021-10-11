from flask import Flask, request
from responses.responses import RetrieveSchema
from flask_swagger_ui import get_swaggerui_blueprint
import datetime

import generateHashCode
import dictionary

'''
spec = APISpec(
    title="Clone of BITLY API",
    version="0.0.1",    # our api version
    openapi_version="3.0.3",    # this is open api version
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin()
    ],
)
'''

app = Flask(__name__)

# Swagger config
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "CLone of Bitly API"
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)


@app.route('/v4/bitlinks/<path:bitlink>/clicks',  methods=['GET'])
def getClicks(bitlink):
    print(bitlink)
    # to read query params, just use the below code, in '' give the query param value we want to read
    queryparam = request.args.get('dateCreated')
    print(queryparam)
    response = dictionary.getClicks(bitlink, queryparam)
    return response



@app.route('/v4/bitlinks/<path:bitlink>',  methods=['GET'])
def retrieve(bitlink):
    dummy_data ={
          "references": { "First Demo" },
          "link": "Test.com",
          "id": "abc",
          "long_url": "Testing.com",
          "title": "Retrieve a bitlink",
          "archived": True,
          "created_at": "Bitly",
          "created_by": "Vivek",
          "client_id": "NA",
          "custom_bitlinks": [
            "Abc.com",
              "xyz.com"
          ],
          "tags": [
            "Demo"
          ],
          "launchpad_ids": [
            "NA"
          ],
          "deeplinks": [
            {
              "guid": "1",
              "bitlink": "abc.com",
              "app_uri_path": "sjdksa.com/sadas",
              "install_url": "ssada",
              "app_guid": "2",
              "os": "linux",
              "install_type": "string",
              "created": "string",
              "modified": "string",
              "brand_guid": "string"
            }
          ]
    }

    bitlink_content = dictionary.getUrl(bitlink)
    return RetrieveSchema().dump(bitlink_content)


@app.route('/v4/shorten',  methods=['POST'])
def shorten():
    content = request.get_json()
    print(content)
    if "domain" in content:
        domain = content["domain"]
    else:
        domain = "bit.ly"

    short_url = generateHashCode.idToShortURL(domain)
    dictionary.shortenUrl(short_url, content)

    dummy_data ={
          "references": { "First Demo" },
          "link": "DUMMY_DATA",
          "id": short_url,
          "long_url": content["long_url"],
          "title": "DUMMY_Title",
          "archived": False,
          "created_at": "Bitly",
          "created_by": "Vivek",
          "client_id": "NA",
          "custom_bitlinks": [
            "Abc.com",
              "xyz.com"
          ],
          "tags": [
            "Demo"
          ],
          "launchpad_ids": [
            "NA"
          ],
          "deeplinks": [
            {
              "guid": "1",
              "bitlink": short_url,
              "app_uri_path": "sjdksa.com/sadas",
              "install_url": "ssada",
              "app_guid": "2",
              "os": "linux"
            }
          ]
    }
    return RetrieveSchema().dump(dummy_data)





@app.route('/v4/bitlinks',  methods=['POST'])
def create():
    content = request.get_json()

    if "domain" in content:
        domain = content["domain"]
    else:
        domain = "bit.ly"

    short_url = generateHashCode.idToShortURL(domain)

    content["id"] = short_url
    content["archived"] = True
    content["created_at"] = datetime.datetime.now()
    if "deeplinks" in content:
        content["deeplinks"][0]["bitlink"] = short_url

    dictionary.createUrl(short_url, content)

    return RetrieveSchema().dump(content)



@app.route('/v4/bitlinks/<path:bitlink>',  methods=['PATCH'])
def update(bitlink):
    request_content = request.get_json()    # If we are always expecting a json body we can use as it is else get_json(silent=True)

    response = dictionary.updateUrl(bitlink, request_content)
    return RetrieveSchema().dump(response)


# to kill from terminal sudo lsof -t -i tcp:5000 | xargs kill -9
'''
with app.test_request_context():
    spec.path(view=test2)
    spec.path(view=retrieve)
    '''



if __name__ == '__main__':
    app.run(debug=True)