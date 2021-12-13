pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }

    stages {
        stage('Build') {
            parallel {
                stage('Build A') {
                    steps {
                        echo 'Building A..'
                    }
                }
                stage('Build B') {
                    steps {
                        echo 'Building B..'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
