#!/bin/bash

/tests/load_data.sh
/tests/test_authn.sh
source /etc/profile
python /tests/test_changepw.py
python /tests/test_django_ldapdb.py
