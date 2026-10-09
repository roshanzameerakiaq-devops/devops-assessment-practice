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
                echo 'Running application unit tests'
                sh 'python3 -m unittest test_app.py -v'
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
