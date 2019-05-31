pipeline {
    agent {
        docker {
            image 'node:12.3.1-alpine'
            args '-p 3000:3000'
        }
    }
    environment {
        CI = 'true'
    }
    stages {
        stage('Test frontend') {
            steps {
                dir('frontend') {
                    sh 'npm prune'
                    sh 'npm install'
                    sh 'npm run test'
                }
            }
        }
        stage('Build frontend') {
            steps {
                dir('frontend') {
                    sh 'npm run build'
                }
            }
        }
        stage('Cleanup') {
            steps {
                dir('frontend') {
                    sh 'npm prune'
                    sh 'rm -rf node_modules'
                }
            }
        }
    }
}
