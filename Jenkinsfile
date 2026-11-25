pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully'
            }
        }

        stage('Environment Check') {
            steps {
                sh '''
                    python3 --version
                    git --version
                '''
            }
        }

        stage('Unit Testing') {
            steps {
                dir('Q1-CI-CD-Testing') {
                    sh '''
                        python3 -m unittest discover \
                        -s tests -p "test_calculator.py" -v
                    '''
                }
            }
        }

        stage('Integration Testing') {
            steps {
                dir('Q1-CI-CD-Testing') {
                    sh '''
                        python3 -m unittest discover \
                        -s tests -p "test_integration.py" -v
                    '''
                }
            }
        }

        stage('Deployment Gate') {
            steps {
                echo 'All automated tests passed.'
                echo 'Deployment is approved.'
            }
        }
    }

    post {
        success {
            echo 'CI/CD PIPELINE: SUCCESS'
        }

        failure {
            echo 'CI/CD PIPELINE: FAILED - Deployment blocked.'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
