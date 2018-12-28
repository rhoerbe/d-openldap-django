#!/bin/bash

function exec_script() {
    printf "execute $1\n"
    $1
}


exec_script /tests/wpvAt/load_data.sh
exec_script /tests/wpvAt/test_authn.sh
exec_script /tests/wpvAt/test_changepw.py
exec_script /tests/wpvAt/test_django_ldapdb.py
