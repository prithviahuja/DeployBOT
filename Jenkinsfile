pipeline {
    agent any

    environment {
        AWS_REGION  = 'ap-south-1'
        ECR_REPO   = 'medical-rag'
        IMAGE_TAG  = 'latest'
        SERVICE_NAME = 'llmops-medical-service'
    }

    pipeline {
    agent any

    stages {
        stage('Checkout Source Code') {
            steps {
                cleanWs()
                checkout scmGit(
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        credentialsId: 'Medical_rag',
                        url: 'https://github.com/prithviahuja/DeployBOT.git'
                    ]]
                )
            }
        }
    }
}


        // stage('Build, Scan, and Push Docker Image to ECR') {
        //     steps {
        //         withCredentials([[
        //             $class: 'AmazonWebServicesCredentialsBinding',
        //             credentialsId: 'aws-token'
        //         ]]) {
        //             script {
        //                 def accountId = sh(
        //                     script: "aws sts get-caller-identity --query Account --output text",
        //                     returnStdout: true
        //                 ).trim()

        //                 def ecrUrl = "${accountId}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}"
        //                 def imageFullTag = "${ecrUrl}:${IMAGE_TAG}"

        //                 sh """
        //                 aws ecr get-login-password --region ${AWS_REGION} \
        //                   | docker login --username AWS --password-stdin ${ecrUrl}

        //                 docker build -t ${ECR_REPO}:${IMAGE_TAG} .

        //                 trivy image --severity HIGH,CRITICAL \
        //                   --format json -o trivy-report.json \
        //                   ${ECR_REPO}:${IMAGE_TAG} || true

        //                 docker tag ${ECR_REPO}:${IMAGE_TAG} ${imageFullTag}
        //                 docker push ${imageFullTag}
        //                 """

        //                 archiveArtifacts artifacts: 'trivy-report.json', allowEmptyArchive: true
        //             }
        //         }
        //     }
        // }
    

        // ------------------ OPTIONAL DEPLOYMENT STAGE ------------------
        // Uncomment when you are ready to deploy automatically
        //
        // stage('Deploy to AWS App Runner') {
        //     steps {
        //         withCredentials([[
        //             $class: 'AmazonWebServicesCredentialsBinding',
        //             credentialsId: 'aws-token'
        //         ]]) {
        //             script {
        //                 def accountId = sh(
        //                     script: "aws sts get-caller-identity --query Account --output text",
        //                     returnStdout: true
        //                 ).trim()
        //
        //                 def ecrUrl = "${accountId}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}"
        //                 def imageFullTag = "${ecrUrl}:${IMAGE_TAG}"
        //
        //                 echo "Triggering deployment to AWS App Runner..."
        //
        //                 sh """
        //                 SERVICE_ARN=\$(aws apprunner list-services \
        //                   --query "ServiceSummaryList[?ServiceName=='${SERVICE_NAME}'].ServiceArn" \
        //                   --output text --region ${AWS_REGION})
        //
        //                 echo "Found App Runner Service ARN: \$SERVICE_ARN"
        //
        //                 aws apprunner start-deployment \
        //                   --service-arn \$SERVICE_ARN \
        //                   --region ${AWS_REGION}
        //                 """
        //             }
        //         }
        //     }
        // }
    }
}
