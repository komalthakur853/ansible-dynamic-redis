 pipeline {
    agent any

    environment {
        // Set up environment variables
        ANSIBLE_INVENTORY = 'dynamic-inventory.yml'
        ANSIBLE_PLAYBOOK = 'install_redis.yml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from the Git repository without credentials
                git branch: 'main', url: 'https://github.com/komalthakur853/ansible-dynamic-redis.git'
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
