#!/bin/bash -e

echo "test authentication with user test@bmspot.gv.at"

ldapsearch -h localhost -p $SLAPDPORT -x -D gvGid=AT:B:1:12345,gvOuId=AT:TEST:1,dc=gv,dc=at \
    -w test -b dc=at -L 'uid=test@bmspot.gv.at'
