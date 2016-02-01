"""
dev settings
"""

import os


def set_env(var, val):
    """
    Set a default for an environment variable. Allows for override of
    production settings while still giving preference to existing
    environment variables.
    """
    os.environ.setdefault(var, val)


set_env('SECRET_KEY', 'a-4t7cm_#=&uvkorig$m%hvbmh^h4yxc#)5qezwn!55t)^#&11')
set_env('DB_NAME', 'hites')
set_env('DB_USER', 'postgres')
set_env('DB_PASSWORD', 'ooglyboogly')
set_env('DB_HOST', '192.168.99.100')

DEBUG = True


# pylint: disable=wildcard-import,wrong-import-position,unused-wildcard-import
from hites.settings import *


ALLOWED_HOSTS = ['127.0.0.1']
