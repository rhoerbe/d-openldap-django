#!/bin/bash -e

echo "test authentication with user test@bmspot.gv.at"

ldapsearch -h localhost -p $SLAPDPORT -x -D tstgid=tt1,dc=at \
    -w test -b dc=at -L 'tstgid=tt1'
