# ldapsearch -h localhost -p $SLAPDPORT -x -D cn=admin,dc=at -w changeit -b dc=at -L 'uid=*'
# ldapsearch -h devl11 -p 8389 -x -D cn=admin,dc=at -w changeit -b dc=at -L 'uid=*'

import django
import os
import sys
django.setup()
from djangoldap.models import *

u = tstPerson.objects.get(dn='tstgid=tt1,dc=at')
assert u.tstgid == 'tt1'
u.save()
assert u.email == 'tt@localhost.local'
u.email = 'tt1@localhost.local'
u.save()

u = tstPerson2.objects.get(tstgid='tt2')
