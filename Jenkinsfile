pipeline {
    agent any

    environment {
        // Set up environment variables
        ANSIBLE_INVENTORY = 'dynamic-inventory.json'
        ANSIBLE_PLAYBOOK = 'install_redis.yml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from the Git repository without credentials
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
                // Add the SSH host key for the inventory host
                sh '''
                    # Extract the host from the inventory file and add its SSH key
                    HOST=$(jq -r '.all.hosts.debian_host.ansible_host' ${ANSIBLE_INVENTORY})
                    ssh-keyscan -H ${HOST} >> ~/.ssh/known_hosts
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
            // Clean up or perform post-build actions
            echo 'Pipeline execution completed.'
        }
    }
}
