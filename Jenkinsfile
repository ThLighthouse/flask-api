pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t flask-api .'
            }
        }

        stage('Lint') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 app'
            }
        }

        stage('Push') {
            steps {
                echo "🔧 Тут должен быть push в DockerHub (по заданию)"
            }
        }

        stage('Deploy') {
            steps {
                echo "🚀 Тут должен быть деплой по SSH на сервер (по заданию)"
            }
        }
    }
}

