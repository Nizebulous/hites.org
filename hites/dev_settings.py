import os


def set_env(var, val):
    os.environ.setdefault(var, val)


set_env('SECRET_KEY', 'a-4t7cm_#=&uvkorig$m%hvbmh^h4yxc#)5qezwn!55t)^#&11')
set_env('DB_NAME', 'hites')
set_env('DB_USER', 'postgres')
set_env('DB_PASSWORD', 'ooglyboogly')
set_env('DB_HOST', '192.168.99.100')

DEBUG = True


from settings import *


ALLOWED_HOSTS = ['127.0.0.1']
