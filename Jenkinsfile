pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps{
                sh 'virtualenv env && source env/bin/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}