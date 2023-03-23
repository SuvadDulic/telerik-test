pipeline {
    agent any
    stages {
        stage('Clone repository from GitHub'){
            steps {
                checkout scmGit(branches: [[name: '**']], extensions: [], url: 'https://github.com/SuvadDulic/telerik-test']])
                }
            }
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
}