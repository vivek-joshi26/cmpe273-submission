postGRE = {
    "urlBegin": "postgresql",                   #provide the initial url for postgre db
    "host": "localhost",                        #provide the postGRE DB host name
    "user": "postgres",                         #provide the postGRE DB user name
    "passwd": "password",                       #provide the postGRE DB password
    "db": "college",                            #provide the postGRE DB name
}
mongoDB = {
    # Below one is the current url that I am using after combining these values,
    # in case you want to remove ssl and ssl_cert_reqs query params, kindly update urlEnd to empty string
    #"url": "",
    "urlBegin": "mongodb+srv",                  #provide the intial url for mongodb, for atlas service I am using mongodb+srv
    "host": "cluster0.3tccv.mongodb.net",       #provide the mongodb  host name, I am using atlas service, so this is the cluster name
    "user": "",                            #provide the mongodb user name
    "passwd": "",               #provide the mongodb password
    "db": "college",                            #provide the mongodb db name
    "collection" : "students",                  #provide the collection name
    "urlEnd" : "?ssl=true&ssl_cert_reqs=CERT_NONE",
    #"urlEnd" : "",
}

