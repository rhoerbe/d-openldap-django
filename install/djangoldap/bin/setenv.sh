#!/bin/bash -e
# set run time environment with default values for RHEL/Centos7 and macOS

scriptsdir=$(cd "$(dirname ${BASH_SOURCE[0]})" && pwd)
export APP_HOME=$(dirname $scriptsdir)
export PYTHONPATH=$PYTHONPATH:$APP_HOME:.
export DJANGO_SETTINGS_MODULE=djangoldap.settings

