pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        ECR_REPO   = 'medical-rag'
        IMAGE_TAG  = 'latest'
    }

    stages {

        stage('Checkout') {
            steps {
                // Jenkins already cloned the repo
                // This just ensures a clean workspace
                cleanWs()
                checkout scm
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
                trivy image --severity HIGH,CRITICAL \
                  --format json -o trivy-report.json \
                  medical-rag:latest || true
                '''
                archiveArtifacts artifacts: 'trivy-report.json', allowEmptyArchive: true
            }
        }
    }
}
