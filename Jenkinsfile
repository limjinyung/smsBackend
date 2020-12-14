pipeline {
    agent none
    stages {
        stage('Basic Information') {
            steps{
                sh "echo some basic informations"
            }
        }

        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps{
                sh 'python -m py_compile helloworld/manage.py'
            }
        }
    }
}