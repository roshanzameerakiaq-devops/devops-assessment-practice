pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is available in the workspace'
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Test') {
            steps {
                echo 'Checking application files'
                sh 'test -f app.py'
                sh 'python3 --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Task Manager Docker image'
                sh 'docker build -t task-manager:v2 .'
            }
        }
    }
}
