from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource, NoResource
from twisted.web.http import proxiedLogFormatter

from twisted.python import log
from twisted.python.logfile import DailyLogFile

import cgi
import time

from platforms.Android import Android

class API(Resource):
    def getChild(self, devicetype, request):
        try: 
            if devicetype == "Android":
                return Android()
            else:
                return "1111111111"+NoResource()
        except:
             return "222222222222"+NoResouce()

    def render_GET(self, request):
       return "3333333"+NoResource()


#log.startLogging(DailyLogFile.fromFullPath('/var/log/twisted/error.log'), setStdout=False,)
resourceroot = API()
factory = Site(resourceroot)
reactor.listenTCP(8888, factory,)
print "...."
reactor.run()
