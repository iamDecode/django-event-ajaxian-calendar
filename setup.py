#!/usr/bin/env python2

from distutils.core import setup

kwargs = {
    'name': 'django-event-ajaxian-calendar',
    'version': '0.1',
    'license': 'BSD',
    'description': 'A simple to use event calendar with ajax abilites and facebox event displaying. Schoolcalendar is an independent application so you can itegrate it easily to your project.',
    'author': 'makkalot',
    'packages': ['django_event_ajaxian_calendar', 'django_event_ajaxian_calendar.templatetags'],
    'package_data': {'django_event_ajaxian_calendar': ['templates/calendar/*.html']},
    'download_url': 'https://github.com/TMPST/django-event-ajaxian-calendar/zipball/master',
}

setup(**kwargs)
