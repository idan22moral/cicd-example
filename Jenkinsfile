pipeline {
    node {
        checkout scm
    
        def customImage = docker.build("image", "./Dockerfile")
    
        customImage.inside {
            sh 'echo 123'
        }
    }
}