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
                sh 'python -m venv helloworld'
                sh '.\smsBackend\Scripts\Activate '
                sh 'pip install -r requirements.txt'
                sh 'python manage.py jenkins --enable-coverage'
            }
        }
    }
}