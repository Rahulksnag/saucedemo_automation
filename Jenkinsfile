pipeline {
    agent any

    environment {
        VENV_PATH = "venv\\Scripts\\activate"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repo
                git url: 'https://github.com/Rahulksnag/saucedemo_automation.git', branch: 'main'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment
                bat 'python -m venv venv'

                // Activate venv and upgrade pip
                bat "${env.VENV_PATH} && pip install --upgrade pip"

                // Install dependencies from requirements.txt
                bat "${env.VENV_PATH} && pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest with Allure results directory
                bat "${env.VENV_PATH} && pytest --alluredir=reports/allure-results -v -s"
            }
        }

        stage('Generate Allure Report') {
            steps {
                // Generate Allure report
                allure includeProperties: false, jdk: '', results: [[path: 'reports/allure-results']]
            }
        }
    }

    post {
        always {
            echo "Tests completed. Check Allure report."
        }
    }
}
