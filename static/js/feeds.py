# Python for Frontend
# 
# Feed catcher using AJAX on Brython
#

import time

from browser import document as doc
from browser import ajax

__author__="Python Mexico"
__copyright__="Python Mexico"
__license__="GPL v3"
__version__=".1"

def on_complete(req):
    if req.status==200 or req.status==0:
        doc["result"].html = req.text
    else:
        doc["result"].html = "error "+req.text

def err_msg():
    doc["result"].html = "server didn't reply after %s seconds" %timeout

