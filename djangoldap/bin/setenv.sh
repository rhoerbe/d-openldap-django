#!/bin/bash -e
# set run time environment with default values for RHEL/Centos7 and macOS

scriptdir=$(cd "$(dirname ${BASH_SOURCE[0]})" && pwd)
mod_home=$(cd "$(dirname ${scriptdir})" && pwd)
app_home=$(cd "$(dirname ${mod_home})" && pwd)
export PYTHONPATH=$app_home:.
export DJANGO_SETTINGS_MODULE=djangoldap.settings

