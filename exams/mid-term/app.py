from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
import userData

app = Flask(__name__)

# Swagger config
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "Twitter-like REST API"
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)



@app.route('/users',  methods=['POST'])
def createUser():
    content = request.get_json()
    response = userData.createUser(content)
    return response



@app.route('/users/<path:user_id>/followers/<path:follower_id>',  methods=['PATCH'])
def addFollower(user_id, follower_id):
    print(user_id)
    print(follower_id)
    response = userData.addFollower(user_id,follower_id)
    return response


@app.route('/users/<path:user_Id>/tweets',  methods=['POST'])
def addTweet(user_Id):
    content = request.get_json()
    print(content)
    print(user_Id)
    response = userData.addTweet(user_Id, content)
    return response


@app.route('/users/<path:user_ID>',  methods=['GET'])
def getUser(user_ID):
    response = userData.getUser(user_ID)
    return response




@app.route('/users/<path:user_id>/timeline',  methods=['GET'])
def getUserTimeline(user_id):
    response = userData.getTweets(user_id)
    #userData.getTweets(user_id)
    return response


if __name__ == '__main__':
    app.run(debug=True)




