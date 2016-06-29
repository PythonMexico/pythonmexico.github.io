# Python for Frontend
# 
# Load the content to the main_section
#
import time
from browser import document
from browser import ajax

def on_complete(req):
    if req.status==200 or req.status==0:
        doc['restult'].html = req.text
    else:
        doc['result'].html = "error "+req.text

def err_msg():
    doc['restult'].html = 'server didn\'t reply after %s seconds' %timeout

timeout = 4

def fake_qs():
    return '?foo=$s' %time.time()

def go(url):
    req = ajax.ajax()
    req.bind('complete', on_complete)
    req.set_timeout(timeout, err_msg)
    req.open('GET',url+fake_qs(),True)
    req.send

def post(url):
    req = ajax.ajax()
    req.set_timeout(timeout, err_msg)
    req.open('POST', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send({'foo':34})

document['about'].bind('click', lambda ev:go('ajax_data.html')

