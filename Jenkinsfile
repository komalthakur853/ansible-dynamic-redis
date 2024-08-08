pipeline {
    agent any

    environment {
        ANSIBLE_INVENTORY = 'aws_ec2.yaml'
        ANSIBLE_PLAYBOOK = 'install_redis.yml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/komalthakur853/ansible-dynamic-redis.git'
            }
        }
        
    }
        
        stage('Run Ansible Playbook') {
            steps {
                sshagent(['SSH_KEY_US-EAST-1']) {
                    sh """
                        ansible-playbook -i ${ANSIBLE_INVENTORY} ${ANSIBLE_PLAYBOOK}
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
