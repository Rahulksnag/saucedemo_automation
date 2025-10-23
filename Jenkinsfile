pipeline {
    agent any

    environment {
        VENV_PATH = "venv\\Scripts\\activate"
        GITHUB_ACTIONS = "true"  // Enable headless mode in conftest.py
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out the code from GitHub..."
                git branch: 'main', url: 'https://github.com/Rahulksnag/saucedemo_automation.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "Creating virtual environment and installing dependencies..."
                bat """
                    python -m venv venv
                    call ${VENV_PATH}
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running all tests on both Chrome and Edge in headless mode..."
                bat """
                    call ${VENV_PATH}
                    pytest --alluredir=reports/allure-results --disable-warnings -v
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo "Generating Allure report..."
                allure([
                    includeProperties: false,
                    results: [[path: 'reports/allure-results']]
                ])
            }
        }
    }

    post {
        always {
            echo "Tests completed. Check the Allure report section in Jenkins."
            archiveArtifacts artifacts: 'reports/allure-results/**', fingerprint: true
        }
    }
}
