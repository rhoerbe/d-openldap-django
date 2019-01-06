# Docker image with Django-ldapdb and local OpenLDAP server  

Reproduce behavior of django-ldapdb   

## Usage

Start and execute tests:

    cp docker-compose.yaml.default docker-compose.yaml
    docker-compose up -d
    docker-compose exec openldap_django bash
    # wihtin the container run:
    /tests/test_all.sh

Remove persistent storage:

    docker volume rm openldap_django.etc_openldap openldap_django.var_db
       