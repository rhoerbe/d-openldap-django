#!/bin/bash

[[ $LOGLEVEL ]] && override_loglevel="-d $LOGLEVEL"
# override_loglevel='-d conns,config,stats,shell,trace'

/tests/init_rootpw.sh

cmd="slapd -4 -h ldap://127.0.0.1:12389/ $override_loglevel -u ldap  -u ldap -f /etc/openldap/slapd.conf"
echo $cmd
$cmd && echo 'OpenLDAP server started.'

cd /opt/djangoldap
bash -l