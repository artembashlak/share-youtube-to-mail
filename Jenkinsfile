def gitCred = "247a2050-69da-4697-8fd9-cab389d195d5"
def repoUrl = "https://github.com/artembashlak/share-youtube-to-mail.git"



node() {

        stage('Repository clone') {
            deleteDir()
            git branch: "master", credentialsId: "${gitCred}", url: "${repoUrl}"
        }

        stage('Launch test') {
            sh '/usr/local/opt/python/libexec/bin/python -m pytest tests/'
        }
    }