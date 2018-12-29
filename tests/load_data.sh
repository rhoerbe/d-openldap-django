#!/bin/bash -e

echo "load initial data"

ldapadd -h localhost -p $SLAPDPORT \
    -x -D cn=admin,dc=at -w $ROOTPW \
    -c -f /tests/data/initial_data.ldif

ldappasswd -h localhost -p $SLAPDPORT \
    -x -D cn=admin,dc=at -w $ROOTPW \
    -s 'test' \
    'gvGid=AT:B:1:12345,gvOuId=AT:TEST:1,dc=gv,dc=at'

if [[ -e /tests/data/initial_data2.ldif ]]; then
    ldapadd -h localhost -p $SLAPDPORT \
        -x -D cn=admin,dc=at -w $ROOTPW \
        -c -f /tests/data/initial_data2.ldif
fi
