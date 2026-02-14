pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        GIT_CREDENTIALS       = credentials('git-creds')
        BEST_ACCURACY         = credentials('best-accuracy')
        DOCKERHUB_REPO        = '2022bcs00067/wine-quality-api'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                python3 -m venv .venv
                . .venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . .venv/bin/activate
                cd scripts
                python train.py
                '''
            }
        }

        stage('Read Accuracy') {
            steps {
                script {
                    env.CURRENT_ACCURACY = sh(
                        script: "cat app/artifacts/metrics.json | jq -r '.accuracy'",
                        returnStdout: true
                    ).trim()
                }
                
                // Print metrics + name + roll no
                sh '''
                echo "=========================================="
                echo "Model Metrics:"
                cat app/artifacts/metrics.json | jq .
                echo "=========================================="
                echo "Model accuracy: $CURRENT_ACCURACY"
                echo "Student: Bavishya, Roll No: 2022bcs0067"
                echo "=========================================="
                '''
            }
        }

        stage('Compare Accuracy') {
            steps {
                script {
                    env.IS_BETTER = sh(
                        script: "echo \"${env.CURRENT_ACCURACY} > ${env.BEST_ACCURACY}\" | bc",
                        returnStdout: true
                    ).trim()
                    echo "Current Accuracy: ${env.CURRENT_ACCURACY}"
                    echo "Best Accuracy: ${env.BEST_ACCURACY}"
                    echo "IS_BETTER = ${env.IS_BETTER}"
                }
            }
        }

        stage('Build Docker Image') {
            when {
                expression { env.IS_BETTER == '1' }
            }
            steps {
                sh '''
                # Copy model to model/ directory for Docker build
                mkdir -p model
                cp app/artifacts/model.pkl model/model.pkl
                
                echo "$DOCKERHUB_CREDENTIALS_PSW" | docker login -u "$DOCKERHUB_CREDENTIALS_USR" --password-stdin
                docker build -t $DOCKERHUB_REPO:${BUILD_NUMBER} -t $DOCKERHUB_REPO:latest .
                '''
            }
        }

        stage('Push Docker Image') {
            when {
                expression { env.IS_BETTER == '1' }
            }
            steps {
                sh '''
                docker push $DOCKERHUB_REPO:${BUILD_NUMBER}
                docker push $DOCKERHUB_REPO:latest
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'app/artifacts/**', fingerprint: true
        }
    }
}
