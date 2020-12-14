pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alphine'
                }
            }
            steps{
                sh 'python manage.py runserver'
            }
        }
    }
}