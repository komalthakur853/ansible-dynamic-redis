pipeline {
    agent any

    environment {
        ANSIBLE_INVENTORY = 'dynamic_inventory.json'
        ANSIBLE_PLAYBOOK = 'install_redis.yml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/komalthakur853/ansible-dynamic-redis.git'
            }
        }
        
        stage('Generate Inventory') {
            steps {
                sh '''
                    chmod +x ./dynamic_inventory.py
                    ./dynamic_inventory.py > ${ANSIBLE_INVENTORY}
                    cat ${ANSIBLE_INVENTORY}
                '''
            }
        }

        stage('Add SSH Host Key') {
            steps {
                // Bypass SSH host key checking
                sh '''
                    echo 'Host *' >> ~/.ssh/config
                    echo '    StrictHostKeyChecking no' >> ~/.ssh/config
                    chmod 600 ~/.ssh/config
                '''
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
