#!/usr/bin/python3

import os
from ldap3 import Server, Connection, ALL, LDIF, MODIFY_REPLACE

print('test python/ldap3')

# variables
rootpw = os.environ['ROOTPW'] if 'ROOTPW' in os.environ else 'changeit'
port = '12389'
host = 'localhost:' + port
rootdn = 'dc=at'
admindn = 'cn=admin,dc=at'
userdn = 'tstgid=tt1,dc=at'
testpw = 'test'

print('connecting as ' + admindn)
s = Server(host, get_info=ALL)
conn1 = Connection(s, admindn, rootpw, auto_bind=True, raise_exceptions=True)

print('search testusers ')
conn1.search('dc=at', '(uid=*)')
print(conn1.entries)

print('change password for ' + userdn)
conn1.modify(userdn, {'userPassword': [(MODIFY_REPLACE, ['newpass'])]})

print('connecting as ' + userdn)
conn2 = Connection(s, userdn, 'newpass', auto_bind=True, raise_exceptions=True)
conn2.search('dc=at', '(uid=test@bmspot.gv.at)')
assert len(conn2.entries) >= 1
