# Python for Frontend
# 
# Load the content to the main_section
#
from browser import document, alert

def show(ev):
    alert('click on %s' %ev.currentTarget.id)

def show_stop(ev):
    alert('click on %s' %ev.currentTarget.id)
    ev.stopPropagation()

document['about'].bind('click', show)

