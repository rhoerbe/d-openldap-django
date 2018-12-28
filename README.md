# Docker image with Django-ldapdb and local OpenLDAP server     

## Usage

cp docker-compose.yaml.default docker-compose.yaml
docker-compose up

# wihtin the container now:
/tests/init_rootpw.sh
/tests/load_data.sh
/tests/test_authn.sh

