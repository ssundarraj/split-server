from twisted.web.resource import Resource, NoResource
from twisted.web.server import Site
from twisted.python import log

import cgi
import json

class Android(Resource):
    #isLeaf = True
    # def __init__(self):
    #     Resource.__init__(self)
        
    def render_GET(self, request):
        return "Invalid Request"
    def render_POST(self, request):
        print request.args
        try:
            if(True):#request.args["code"][0] == "Ingenuis2014"):
                params_details=json.loads(request.args['params'][0])
                
                #Registration
                if(request.args['work_type'][0]=='user_reg'):
                    from working.user_reg import new_user_phno
                    return str(json.dumps({'user_id': new_user_phno(params_details)}))
                
                #New Group
                if(request.args['work_type'][0]=='new_group'):
                    from working.groups import new_group
                    return str(json.dumps({'group_id': new_group(params_details)}))

                #Add member to group
                if(request.args['work_type'][0]=='new_group_member'):
                    from working.groups import new_group_member
                    return str(json.dumps({'group_member_id': new_group_member(params_details)}))

                #Add expense to group
                if(request.args['work_type'][0]=='new_expense'):
                    from working.groups import new_expense
                    return str(json.dumps({'group_expense_id': new_group_member(params_details)}))

                #Get all groups for a user 
                if(request.args['work_type'][0]=='load_groups'):
                    from working.app_load import load_groups
                    return str(json.dumps(load_groups(params_details)))

                #Get all group data
                if(request.args['work_type'][0]=='load_groupdata'):
                    from working.app_load import load_groupdata
                    return str(json.dumps(load_groupdata(params_details)))


                else: #invalid args
                    log.msg(request.args)
                    return "INVALID!"                
            else: #invalid code
                return "Bad Code"
        except:
            print "ERROR CHECK THE LOGS"
            log.msg(request.args)
            log.err()
            return '-1'
            
