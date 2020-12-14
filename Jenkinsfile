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
                sh 'pip install -r requirements.txt'
                sh 'python manage.py jenkins --enable-coverage'
            }
        }
    }
}