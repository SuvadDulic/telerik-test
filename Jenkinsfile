pipeline {
    agent any
    stages {
	  stage('Testing GitHub-tests locally') {
            steps {
                dir('C:/Users/SuvDul/Documents/telerik_test'){
                    bat 'pytest'
                }
            }
        }
        stage('Clean Workspace'){
            steps {
                cleanWs()
            }
        }
        }
        }