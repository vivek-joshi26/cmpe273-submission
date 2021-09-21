from pymongo import MongoClient
import json

client = MongoClient('mongodb+srv://mongo:HxCOxXZkxYCU8LXw@cluster0.3tccv.mongodb.net/college?ssl=true&ssl_cert_reqs=CERT_NONE')
db = client.college
students = db.students

'''
cursor = students.find()
for record in cursor:
    print(record)
'''

def generateJson(message):
    print("Inside mongo Generate JSON method")
    message_json = json.loads(message)
    listofmsgs = message_json['change']
    #print(listofmsgs)
    for singlemsg in listofmsgs:
        print("")
        kind = singlemsg['kind']
        if kind == "insert":
             insertJsonToMongodb(singlemsg['columnnames'],singlemsg['columntypes'], singlemsg['columnvalues'])
        elif kind == "update":
             updateJsonToMongodb(singlemsg['columnnames'], singlemsg['columntypes'], singlemsg['columnvalues'])
        elif kind == "delete":
             deleteJsonToMongodb(singlemsg['oldkeys']['keynames'], singlemsg['oldkeys']['keyvalues'])
    return ("Operation completed successfully")


def insertJsonToMongodb(col_names, col_types, col_values):
    print("****************************************************** Inside Insert *****************************************************")
    dict = {}
    for i in range(0, len(col_names)):
        dict[col_names[i]] = col_values[i]

    record = students.insert_one(dict)
    print(f'Inserted Successfully : %s' % record.inserted_id)


def updateJsonToMongodb(col_names, col_types, col_values):
    print("****************************************************** Inside Update *******************************************************")
    myquery = {col_names[0]: col_values[0]}     # will get the id attribute based on that row will be retrieved from mongodb
    dict = {}
    for i in range(0, len(col_names)):
        dict[col_names[i]] = col_values[i]
    newvalues = {"$set": dict}
    record = students.update_one(myquery, newvalues)
    print(f'Updated Successfully : %d' % record.modified_count)


def deleteJsonToMongodb(keyname, keyvalue):
    print("******************************************************* Inside Delete ********************************************************")
    myquery = {keyname[0]: keyvalue[0]}
    students.delete_one(myquery)
    print(f'Student with id %d, deleted Successfully.' % keyvalue[0])

