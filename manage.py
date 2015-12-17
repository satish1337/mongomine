#!/usr/bin/env python
import os
import sys
from mongomine.libs.utils import get_default_django_settings_module

if __name__ == "__main__":

   os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_default_django_settings_module())
   os.environ.setdefault('DJANGO_CONFIGURATION', 'Settings')

   from configurations import importer
   importer.install()

   from django.core.management import execute_from_command_line

   execute_from_command_line(sys.argv)
