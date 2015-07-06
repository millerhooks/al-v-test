from fabric.api import settings, abort, run, \
    cd, local, sudo, env, hosts
from fabric.contrib.console import confirm
import datetime


def rs():
    local('ifconfig && ./manage.py runserver 0.0.0.0:8000')






