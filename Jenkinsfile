pipeline {
    agent any
    stages {
        stage('Basic Information') {
            steps{
                ehco "echo some basic informations"
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