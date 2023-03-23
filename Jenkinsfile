pipeline {
    agent any
    stages {
        stage('Clone repository from GitHub'){
            steps {
                checkout scmGit(branches: [[name: '**']], extensions: [], userRemoteConfigs: [[credentialsId: '9d735792-a50f-4f5f-a3aa-0d9bc503f98d', url: 'https://github.com/SuvadDulic/telerik-test']])
                }
            }
        stage('Testing GitHub-tests locally') {
            steps {
                dir('C:/Users/SuvDul/Documents/telerik_test'){
                    bat 'python -m unittest'
                }
            }
        }
        stage('Clean Workspace'){
            steps {
                cleanWs()
            }
        }
        }