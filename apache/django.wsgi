import os, sys

#mesto gde lejit django
#sys.path.append('/home/ramatahatta/workspace/journal/journal_prj/')
sys.path.append('/home/ramatahatta/workspace/apple_proj/apple_p')

#mesto gde lejit proekt
#sys.path.append('/home/ramatahatta/workspace/journal/')
sys.path.append('/home/ramatahatta/workspace/apple_proj/')

#file configuratsii proekta
#os.environ['DJANGO_SETTINGS_MODULE'] = 'journal_prj.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'apple_proj.settings'

from django.contrib.auth.handlers.modwsgi import check_password
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
