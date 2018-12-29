# Docker image with Django-ldapdb and local OpenLDAP server     

## Usage

cp docker-compose.yaml.default docker-compose.yaml
docker-compose up -d
docker-compose exec openldap_django openldap_django bash
# wihtin the container run:
/tests/test_all.sh

