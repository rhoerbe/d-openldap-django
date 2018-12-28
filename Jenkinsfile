pipeline {
    agent any
    environment {
        compose_cfg='docker-compose.yaml'
        container='openldap_django'
        d_containers="${container} dc_${container}_run_1"
        d_volumes="${container}.etc_openldap ${container}.var_db"
        service='openldap_django'
    }
    options { disableConcurrentBuilds() }
    stages {
        stage('Config ') {
            steps {
                sh '''#!/bin/bash -e
                    cp "${compose_cfg}.default" $compose_cfg
                    egrep '( image:| container_name:)' $compose_cfg || echo "missing keys in ${compose_cfg}"
                '''
            }
        }
        stage('Cleanup ') {
            steps {
                sh '''#!/bin/bash -e
                    source ./jenkins_scripts.sh
                    remove_containers $d_containers && echo '.'
                    remove_volumes $d_volumes && echo '.'
                '''
            }
        }
        stage('Build') {
            steps {
                sh '''#!/bin/bash -e
                    source ./jenkins_scripts.sh
                    remove_container_if_not_running
                    docker-compose build
                '''
            }
        }
        stage('Test: setup') {
            steps {
                sh '''#!/bin/bash -e
                    nottyopt=''; [[ -t 0 ]] || nottyopt='-T'  # autodetect tty
                    docker-compose -p 'dc' run $nottyopt --rm $service /tests/init_rootpw.sh
                    echo "Starting $service"
                    export LOGLEVEL='conns,config,stats,shell'
                    docker-compose --no-ansi up -d
                    source ./jenkins_scripts.sh
                    wait_for_container_up && echo "$service started"
                '''
            }
        }
        stage('Test: run') {
            steps {
                sh '''#!/bin/bash -e
                    ttyopt=''; [[ -t 0 ]] && ttyopt='-t'  # autodetect tty
                    # docker-compose not working here:
                    docker exec $ttyopt $container /tests/test_all.sh
               '''
            }
        }
    }
    post {
        always {
            sh '''#!/bin/bash -e
                source ./jenkins_scripts.sh
                remove_containers $d_containers && echo 'containers removed'
                remove_volumes $d_volumes && echo 'volumes removed'
            '''
        }
    }
}