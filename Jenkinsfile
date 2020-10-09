node {
    stage('Cleanup') {
        step([$class: 'WsCleanup'])
    }
    stage('Checkout SCM') {
        checkout scm
    }
    def pythonImage
    stage('build docker image') {
        pythonImage = docker.build("youtube:build")
    }
    stage('test') {
        pythonImage.inside {
            sh '. /tmp/venv/bin/activate && pytest'
        }
    }
}
