import django
import os
import pytest
import random
import sys
if __name__ == '__main__':
    django_proj_path = os.path.dirname(os.path.dirname(os.getcwd()))
    sys.path.append(django_proj_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoldap.settings")
django.setup()
from djangoldap.models import *

pytestmark = pytest.mark.django_db

print('test django-ldapdb')


def test_inetOrgPerson_update():
    u = inetOrgPerson.objects.get(dn='cn=admin,dc=at')
    new_mail = 'me{}@me.com'.format(random.randint(1,999999))
    u.email = new_mail
    u.save()
    u = inetOrgPerson.objects.get(dn='cn=admin,dc=at')
    assert u.email == new_mail


def test_tstPerson_get_by_dn():
    u = tstPerson.objects.get(dn='tstgid=tt1,dc=at')
    assert u.tstgid == 'tt1'


def test_tstPerson_update():
    u = tstPerson.objects.get(dn='tstgid=tt1,dc=at')
    assert u.email == ''
    u.email = 'tt1@localhost.local'
    u.save()
    u = tstPerson.objects.get(dn='tstgid=tt1,dc=at')
    assert u.email == 'tt1@localhost.local'

def test_tstPerson2_get_by_attribute():
    u = tstPerson2.objects.get(tstgid='tt2')
    assert u.email == 'tt2@localhost.local'

def test_tstPerson2_insert():
    u = tstPerson2(tstgid='tt3')
    u.email = 'tt3@localhost.local'
    u.cn = 'testeroni testafari'
    u.sn = 'testafari'
    u.uid = 'tt3@localhost.local'
    u.tstgid = 'tt3'
    u.tstscope = 'intranet'
    u.save()

