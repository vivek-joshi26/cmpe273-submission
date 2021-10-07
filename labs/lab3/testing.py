from ariadne import gql, QueryType,make_executable_schema
from ariadne.asgi import GraphQL

#Step 3 Create querytype instance for Query type field defined in our schema
query = QueryType()


#Step 1 gql is used for validating the schema and raises GraphQLSyntaxError
type_defs = gql("""
        type Query{
            hello: String!
        }
    """)


#Step 4 We need to set our resolver to hello field of type Query
@query.field("hello")
# Step 2 The resolvers are functions mediating between API consumers and the application's business logic, below one is a root resolver, so we are disregarding the 1st argument
def resolve_hello(_, info):
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello, %s!" % user_agent

# Step 5 We need to combine our textual representation of the API's shape with the resolvers we have defined, pass the type definitions and the resolvers that we want to use
schema = make_executable_schema(type_defs, query)
# example for passing multiple resolvers(also called bindables) make_executable_schema(type_defs,[ query, user, mutations, fallback_resolvers]) , QueryType is one of many bindables


# Step 6 HTTP servers-  ASGI server like uvicorn, daphne, or hypercorn any1 can be used
app = GraphQL(schema, debug=True)

# to run type->     uvicorn filename:appname        example->   uvicorn testing:app   then on browser type {hello}