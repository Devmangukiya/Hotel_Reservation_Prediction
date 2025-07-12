pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages{
        stage('Cloning Githib repo to Jenkins.'){
            steps {
                script {
                    echo 'Cloning Github repo to jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Devmangukiya/Hotel_Reservation.git']])
                }
            }
        }

        stage('Setting up our vitual environment and installing dependencies'){
            steps {
                script {
                    echo 'Setting up our vitual environment and installing dependencies...............'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
} 