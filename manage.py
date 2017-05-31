#!/usr/bin/env python

# This manage.py exists for the purpose of creating migrations
import sys, os

import django
from django.conf import settings
from django.core.management import execute_from_command_line

# settings.configure(
#     ROOT_URLCONF='paypal.urls',#'paypal.standard.ipn.tests.test_urls',  # So Django 1.9 doesn't die
#     DATABASES={'default':
#                {'ENGINE': 'django.db.backends.sqlite3',
#                 'NAME': 'test.db',
#                 }},
#     PAYPAL_IDENTITY_TOKEN='',
#     INSTALLED_APPS=[
#         'django.contrib.auth',
#         'django.contrib.contenttypes',
#         'paypal.pro',
#         'paypal.standard',
#         'paypal.standard.ipn',
#         'paypal.standard.pdt',
#     ] + (['south'] if django.VERSION < (1, 7) else []),
#     CACHES={
#         'default': {
#             'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#             'TIMEOUT': 0,
#             'KEY_PREFIX': 'paypal_tests_',
#         }
#     },
#     MIDDLEWARE_CLASSES=[],
#     DEBUG=True,
#
# )

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "paypal.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
