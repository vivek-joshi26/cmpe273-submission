from ariadne import gql, QueryType, MutationType, make_executable_schema, graphql_sync
from ariadne.asgi import GraphQL
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify

# Creating global counters for students and class
id = 0
class_id = 100
students = {}
classes = {}

# schema can be created separately in a file and then used like->  type_defs = load_schema_from_path('schema.graphql')

type_defs = gql("""
    type Query {
        hello: String!
        viewStudent(id: ID!) : Student!
        viewClass(id: ID!): Class!
        }
        
    type Mutation {
        insertStudent(name: String!): Student!
        createClass(name: String!): Class!
        addStudentToClass(id: ID!, class_id: ID!): Class
    }
    
    type Student {
        id: ID!
        name: String!
    }
    
    type Class{
        id: ID!
        name: String!
        students: [Student!]!
    }
""")


query = QueryType()
mutation = MutationType()


# Just to test if the program is working fine or not
@query.field("hello")
def resolve_hello(_, info):
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello, %s!" % user_agent



@query.field("viewStudent")
def viewStudent(_, info, id):
    #return {'id': id, 'name': "Testing"}
    return {'id': id, 'name': students.get(int(id))}



@query.field("viewClass")
def viewClass(_, info, id):
    classReturned = classes.get(int(id))
    print("INSIDE VIEW CLASS ***********************************")
    print(classReturned)
    return {'id': id, 'name': classReturned['name'], 'students': classReturned['students']}




@mutation.field("insertStudent")
def insertStudent(_, info, name):
    global id
    id += 1
    students[id] = name
    print(students)
    return {'id': id, 'name': name}



@mutation.field("createClass")
def createClass(_,info, name):
    global class_id
    class_id += 1
    classes[class_id] = { 'name' : name, 'students' : []}
    return {'id': class_id, 'name': name, 'students': []}



@mutation.field("addStudentToClass")
def addStudentToClass(_,info,id,class_id):
    student = students.get(int(id))
    print("INSIDE ADDSTUDENT TO CLASS *****************************************")
    print(student)
    classes[int(class_id)]['students'].append({"id": id, "name": student})
    print(classes)
    curClass = classes.get(int(class_id))
    return {'id': class_id, 'name': curClass['name'], 'students': curClass['students']}



schema = make_executable_schema(type_defs, [query,mutation])
'''
# We can use the below code and then fo to the address by running command - uvicorn app:app         , here first app is the python file name and the second app is the below variable
app = GraphQL(schema, debug=True)

# If we are not using the above step then we can use the below mentioned code and directly run the python file and then go to the /graphql resource
'''




app = Flask(__name__)


@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)