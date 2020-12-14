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
                sh 'python helloworld/manage.py jenkins --enable-coverage'
            }
        }
    }
}