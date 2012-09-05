import argparse
import sys
from api import StreamClient, ObjCode
from dot8_credentials import ATTASK_BASE_URL, USERNAME, PASSWORD

API_URL = ATTASK_BASE_URL+"/attask/api-internal"

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

#get the command line parameters and make sense of them
parser = argparse.ArgumentParser(description='Issue To Task')
parser.add_argument('issueID', action='store', type=str, help="This is the issue GUID on dot8")
parser.add_argument('-b', action='store_true', default=False, dest='isBlocking', help='Whether to set it as a blocking task')
parser.add_argument('-p', nargs="?", dest='points', default=0, type=int, required=False, help='How many points the task is worth')

args = parser.parse_args() #we will refer to this object later to key off the properties set on it

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

#taskPriorities = connection.get(ObjCode.CUSTOM_ENUM, "taskPriorities")
#issuePriorities = connection.get(ObjCode.CUSTOM_ENUM, "opTaskPriorities")

issue = connection.get(ObjCode.ISSUE, args.issueID,['priority', 'description', 'resolvingObjID'])

def addTaskFromIssue(issue, projectID, isBlocking=False):
    if issue['resolvingObjID'] is None:
        task = connection.post(ObjCode.TASK,{
            'name': issue['name'],
            'description': issue['description'],
            'categoryID': CATEGORY_BACKLOG_ITEM,
            'DE:Blocking': 'Yes' if isBlocking else 'No',
            'DE:T-Shirt Size': TShirtSize.SMALL,
            'DE:Points': args.points,
            'projectID':projectID,
            'assignedToID': AGILE_LEAD[projectID]
        })

        connection.put(ObjCode.ISSUE, issue['ID'],{
            'resolvingObjCode': task['objCode'],
            'resolvingObjID': task['ID']
        })

        print "A new task '%s' was created successfully." % task['name']
        line()
        print ATTASK_BASE_URL + "/task/view?ID="+task['ID']
        print ATTASK_BASE_URL + "/issue/view?ID="+issue['ID']
    else:
        print "Issue '%s' already has a resolving object." % issue['name']

addTaskFromIssue(issue, TWACA, args.isBlocking)

