pipeline {
    agent any
    checkout scm
    
    def customImage = docker.build("image", "./Dockerfile")

    customImage.inside {
        sh 'echo 123'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}