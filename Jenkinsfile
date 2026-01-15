pipeline {
    agent any

    stages {

        stage('Verify Workspace') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t medical-rag:latest .'
            }
        }

        stage('Trivy Scan') {
            steps {
                sh '''
                trivy image medical-rag:latest \
                  --severity HIGH,CRITICAL \
                  --format json -o trivy-report.json || true
                '''
                archiveArtifacts artifacts: 'trivy-report.json'
            }
        }
    }
}
