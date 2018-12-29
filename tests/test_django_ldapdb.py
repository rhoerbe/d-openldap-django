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


def test_gvOrgPerson_filter_cn():
    qs = gvOrgPerson.objects.filter(cn='Test User')
    p = qs[0]
    assert isinstance(p.cn, str)
    assert isinstance(p.gvGid, str), f'gvGid is {type(p.gvGid)}'
    assert p.gvGid == 'AT:B:1:12345'


def test_gvOrgPerson_filter_dn():
    qs = gvOrgPerson.objects.filter(dn='gvGid=AT:B:1:12345,gvOuId=AT:TEST:1,dc=gv,dc=at')
    p = qs[0]
    assert p.gvGid == 'AT:B:1:12345'


def test_gvOrgPerson_filter_gvGid():
    qs = gvOrgPerson.objects.filter(gvGid='AT:B:1:12345')
    p = qs[0]
    assert p.gvGid == 'AT:B:1:12345'


def test_gvOrgPerson_get_by_gvGid():
    p = gvOrgPerson.objects.get(gvGid='AT:B:1:12345')
    assert p.gvGid == 'AT:B:1:12345'


def test_gvOrgPerson_update():
    p = gvOrgPerson.objects.get(gvGid='AT:B:1:12345')
    assert p.gvStatus == 'active'
    p.gvStatus = 'inactive'
    p.save()
    p = gvOrgPerson.objects.get(gvGid='AT:B:1:12345')
    assert p.gvStatus == 'inactive'


def test_gvOrganisation_get():
    o = gvOrganisation.objects.get(gvOuId='AT:TEST:1')
    assert o.gvStatus == 'active'


def test_gvOrganisation_update():
    o = gvOrganisation.objects.get(gvOuId='AT:TEST:1')
    assert o.gvStatus == 'active'
    o.gvStatus = 'inactive'
    o.save()
    o = gvOrganisation.objects.get(gvOuId='AT:TEST:1')
    assert o.gvStatus == 'inactive'


def test_gvOrganisation_update():
    n = gvOrganisation(dn='gvOuId=AT:TEST:2,dc=gv,dc=at', gvOuId='AT:TEST:2')
    n.cn = 'test'
    n.dc = 'gv'
    n.gvOuCn = 'test'
    n.gvOuVKZ = 'test'
    n.o = 'test'
    n.ou = 'test'
    n.gvScope = 'public'
    n.gvSource = 'test'
    n.gvStatus = 'active'
    n.save()
    o = gvOrganisation.objects.get(dn='gvOuId=AT:TEST:2,dc=gv,dc=at')
    assert o.gvScope == 'public'
