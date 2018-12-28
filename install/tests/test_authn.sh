#!/bin/bash -e

ldapsearch -h localhost -p 8389 -x -D gvGid=AT:B:1:12345,gvOuId=AT:TEST:1,dc=gv,dc=at \
    -w test -b dc=at -L 'uid=test@bmspot.gv.at'
