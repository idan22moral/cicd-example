pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                def img = docker.build("cicd-img", "./Dockerfile")
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