pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/ThLighthouse/flask-api.git'
        PROJECT_DIR = 'flask-api'
    }

    stages {
        stage('Manual Checkout') {
            steps {
                sh 'rm -rf $PROJECT_DIR'
                sh 'git clone $REPO_URL'
            }
        }

        stage('Build') {
            steps {
                dir('flask-api') {
                    sh 'docker build -t flask-api .'
                }
            }
        }

        stage('Lint') {
            steps {
                dir('flask-api') {
                    sh 'docker run --rm flask-api flake8 app'
                }
            }
        }

        stage('Push') {
            steps {
                echo "🔧 Тут будет push в DockerHub"
            }
        }

        stage('Deploy') {
            steps {
                echo "🚀 Тут будет деплой по SSH"
            }
        }
    }
}

