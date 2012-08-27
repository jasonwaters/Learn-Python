from experiments.api import StreamClient, ObjCode
from experiments.local_credentials import API_URL, USERNAME, PASSWORD

PROJECT_ID = "50047866000005b833d7a1da52e5f69c"

connection = StreamClient(API_URL)

try:
    connection.login(USERNAME,PASSWORD)
except Exception, e:
    print "Error connecting to %s" % connection.url
    print e
    exit(0)

def createTask(name):
    result = connection.post(ObjCode.TASK,{'name': name, 'projectID':PROJECT_ID})

project = connection.get(ObjCode.PROJECT,PROJECT_ID,['tasks:*']) #AtTaskObject(connection.get(ObjCode.PROJECT,PROJECT_ID,['tasks:*']), connection)

print "%s [Project]" % project['name']

for task in project['tasks']:
    print "\tTask %d: %s" % (task['taskNumber'],task['name'])


createTask("bobbo's Task!!")