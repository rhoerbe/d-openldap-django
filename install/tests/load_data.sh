#!/bin/sh

echo "load initial data"

ldapadd -h localhost -p 12389 \
    -x -D cn=admin,dc=at -w $ROOTPW \
    -f /tests/data/initial_data.ldif

ldappasswd -h localhost -p 12389 \
    -x -D cn=admin,dc=at -w $ROOTPW \
    -s 'test' \
    'gvGid=AT:B:1:12345,gvOuId=AT:TEST:1,dc=gv,dc=at'

