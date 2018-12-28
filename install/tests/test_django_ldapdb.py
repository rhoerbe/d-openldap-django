import django
django.setup()
from djangoldap.models import *

print('test django-ldapdb')

o = gvOrganisation.objects.get(gvOuId='AT:TEST:1')
o.gvStatus = 'inactive'
o.save()
print(gvOrganisation.objects.get(gvOuId='AT:TEST:1').gvStatus)

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