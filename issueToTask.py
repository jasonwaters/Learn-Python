from api import StreamClient, ObjCode, AtTaskObject
from dot8_credentials import API_URL, USERNAME, PASSWORD

GANG_GREEN = '501ad8da000020e7edc603378964c6e8'
APERTURE = '4ffe5ced000065b2a4dbc3349040eeaf'
TWACA = '501ad91a00002b26f6bae30ba3fb69d9'
JIGGLYPUFF = '50044a2f0011d53a5854980f47f8785f'

MICHAEL_BRIGHT = '4d52e742000196b941a0479014ae95c8'
JAKE_TURPIN = '4dde6ffb00052152a2733ca820329b45'
JT = '4d52e23900019587c0320470f94bcc6a'
BRYAN_HINTON = '4e9f2bfa00002db16fa94d369c6f88e1'

AGILE_LEAD = {
    GANG_GREEN : JT,
    APERTURE: BRYAN_HINTON,
    TWACA: MICHAEL_BRIGHT,
    JIGGLYPUFF: JAKE_TURPIN
}


TEAM_PROJECTS = [GANG_GREEN,APERTURE,TWACA,JIGGLYPUFF]

CATEGORY_BACKLOG_ITEM = '4c78aaa7000c4bc23722d1bebdf9d77f'

class TShirtSize:
    SMALL = 5
    MEDIUM = 10
    LARGE = 15

connection = StreamClient(API_URL)

try:
    connection.login(USERNAME,PASSWORD)
except Exception, e:
    print "Error connecting to %s" % connection.url
    print e
    exit(0)

def printProject(project):
    print "%s [Project]" % project['name']
    tasks = sorted(project['tasks'],key=lambda k: k['taskNumber'])
    for task in tasks:
        if task['parentID'] is None: #parent task
            print "\tTask %d: %s" % (task['taskNumber'],task['name'])
    line()


def line():
    print "="*100


#print all top level tasks for all teams
#for teamID in TEAMS:
#    project = connection.get(ObjCode.PROJECT,teamID,['tasks:*'])
#    printProject(project)

issue = connection.get(ObjCode.ISSUE, '50353237000546e5ff90f37a3f9b9ede',['priority', 'description', 'resolvingObjID'])

def addTaskFromIssue(issue, projectID, isBlocking=False):
    if issue['resolvingObjID'] is None:
        print issue['name']
        print issue['description']
        task = connection.post(ObjCode.TASK,{
            'name': issue['name'],
            'description': issue['description'],
            'categoryID': CATEGORY_BACKLOG_ITEM,
            'DE:Blocking': 'Yes' if isBlocking else 'No',
            'DE:T-Shirt Size': TShirtSize.SMALL,
            'projectID':projectID,
            'assignedToID': AGILE_LEAD[projectID],
#            'priority':
        })

        connection.put(ObjCode.ISSUE, issue['ID'],{
            'resolvingObjCode': task['objCode'],
            'resolvingObjID': task['ID']
        })

print issue['priority']




#addTaskFromIssue(issue, TWACA, True)