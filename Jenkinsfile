pipeline {
    agent any
    environment {
        compose_cfg='docker-compose.yaml'
        compose_f_opt=''
        container='openldap_pv'
        d_containers="${container} dc_${container}_run_1"
        d_volumes="${container}.etc_openldap ${container}.var_db"
        network='dfrontend'
        service='openldap_pv'
    }
    options { disableConcurrentBuilds() }
    stages {
        stage('Config ') {
            steps {
                sh '''#!/bin/bash -e
                    echo "using ${compose_cfg} as docker-compose config file"
                    if [[ "$DOCKER_REGISTRY_USER" ]]; then
                        echo "  Docker registry user: $DOCKER_REGISTRY_USER"
                        ./dcshell/update_config.sh "${compose_cfg}.default" $compose_cfg
                    else
                        cp "${compose_cfg}.default" $compose_cfg
                    fi
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
                    [[ "$nocache" ]] && nocacheopt='-c' && echo 'build with option nocache'
                    docker-compose build $nocacheopt
                '''
            }
        }
        stage('Test: setup') {
            steps {
                sh '''#!/bin/bash -e
                    source ./jenkins_scripts.sh
                    create_docker_network
                    echo "initialize persistent data"
                    nottyopt=''; [[ -t 0 ]] || nottyopt='-T'  # autodetect tty
                    docker-compose -p 'dc' run $nottyopt --rm $service /tests/init_rootpw.sh
                    echo "Starting $service"
                    export LOGLEVEL='conns,config,stats,shell'
                    docker-compose --no-ansi up -d
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