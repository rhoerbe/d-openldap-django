#!/bin/bash

[[ $LOGLEVEL ]] && override_loglevel="-d $LOGLEVEL"
# override_loglevel='-d conns,config,stats,shell,trace'

cmd="slapd -4 -h ldap://$SLAPDHOST:8389/ $override_loglevel -u ldap  -u ldap -f /etc/openldap/slapd.conf"
echo $cmd
$cmd

echo 'OpenLDAP server started.'

cd /opt/djangoldap
bash -l