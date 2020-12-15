pipeline {
    agent any
    stages {
        stage('test') {
             agent {
                  docker {
                       image 'qnib/pytest'
                  }
             }
             steps {
                  sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python helloworld/tests.py'
             }
        }
    }
}