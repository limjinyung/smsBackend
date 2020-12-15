pipeline {
    agent any
    stages {
        stage('Test') {
             agent {
                  docker {
                       image 'qnib/pytest'
                  }
             }
             steps {
                  sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python helloworld/sms/tests.py'
             }
        }
    }
}