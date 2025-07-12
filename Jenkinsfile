pipeline{
    agent any

    stages{
        stage('Cloning Githib repo to Jenkins.'){
            steps {
                script {
                    echo 'Cloning Github repo to jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Devmangukiya/Hotel_Reservation.git']])
                }
            }
        }
    }
} 