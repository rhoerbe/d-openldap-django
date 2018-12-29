#!/bin/bash

/tests/load_data.sh
if (( $? != 0 )); then
    echo "loading of initial data failed, test aborted"
    exit 1
fi

/tests/test_authn.sh
test_result=$?

source /etc/profile

python /tests/test_ldap3_changepw.py
rc=$?
test_result=$((test_result=test_result+rc))

pytest /tests/test_django_ldapdb.py
rc=$?
test_result=$((test_result=test_result+rc))

exit $test_result