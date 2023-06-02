# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1843448/data/www/ict-expo.ru')
sys.path.insert(1, '/var/www/u1843448/data//env/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()