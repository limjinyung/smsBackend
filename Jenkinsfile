// pipeline {
//      environment {
//           registry = "jinyunglim/smsbackend"
//           registryCredential = 'dockerhub_id'
//           dockerImage= ''
//      }
//     agent any
//     stages {
//         stage('Test') {
//              agent {
//                   docker {
//                        image 'qnib/pytest'
//                   }
//              }
//              steps {
//                   sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python helloworld/sms/tests.py'
//              }
//         }
//         stage('Build Docker image') { 
//             steps { 
//                 script { 
//                     dockerImage = docker.build registry + ":$BUILD_NUMBER" 
//                 }
//             } 
//         }
//         stage('Deploy Docker image') {
//              steps{
//                   script{
//                        docker.withRegistry('', registryCredential){
//                             dockerImage.push()
//                        }
//                   }
//              }
//         }

//         stage('Cleaning up docker') {
//              steps {
//                   sh 'docker rmi $registry:$BUILD_NUMBER'
//              }
//         }
//     }
//     post {
//          always {
//               emailext body: 'A Test Email', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
//          }
//     }
// }

//variables
def network='jenkins-${BUILD_NUMBER}'
def seleniumHub='selenium-hub-${BUILD_NUMBER}'
def chrome='chrome-${BUILD_NUMBER}'
def firefox='firefox-${BUILD_NUMBER}'
def containertest='conatinertest-${BUILD_NUMBER}'
pipeline {
  
   agent { label 'docker' }

   stages{
      stage('Setting Up Selenium Grid') {
         steps{        
            sh "docker network create ${network}"
            sh "docker run -d -p 4444:4444 --name ${seleniumHub} --network ${network} selenium/hub"
            sh "docker run -d -e HUB_PORT_4444_TCP_ADDR=${seleniumHub} -e HUB_PORT_4444_TCP_PORT=4444 --network ${network} --name ${chrome} selenium/node-chrome"
            sh "docker run -d -e HUB_PORT_4444_TCP_ADDR=${seleniumHub} -e HUB_PORT_4444_TCP_PORT=4444 --network ${network} --name ${firefox} selenium/node-firefox"
         }
      }
      stage('Run Test') {
         steps{
            parallel(
               "search-module":{
                  sh "docker run --rm -e SELENIUM_HUB=${seleniumHub} -e BROWSER=firefox -e MODULE=search-module.xml -v ${WORKSPACE}/search:/usr/share/tag/test-output --network ${network} iamsethi786/docker-selenium"
                  archiveArtifacts artifacts: 'search/**', fingerprint: true
               },
               "order-module":{
                  sh "docker run --rm -e SELENIUM_HUB=${seleniumHub} -e BROWSER=chrome -e MODULE=order-module.xml -v ${WORKSPACE}/order:/usr/share/tag/test-output  --network ${network} iamsethi786/docker-selenium"
                  archiveArtifacts artifacts: 'order/**', fingerprint: true
               }               
            ) 
         }
      }
    }
    post{
      always {
         sh "docker rm -vf ${chrome}"
         sh "docker rm -vf ${firefox}"
         sh "docker rm -vf ${seleniumHub}"
         sh "docker network rm ${network}"
      }   
   }
}