pipeline{
    agent any

    stages{
        stage('Cloning Github repo to jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to jenkins....'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Devmangukiya/Hotel_Reservation_prediction.git']])
                }
            }
        }
    }
}