pipeline {
    agent any

    environment {
        VENV_PATH = "venv\\Scripts\\activate"
    }

    stages {

        stage('Checkout') {
            steps {
                // Checkout the repo
                git branch: 'main', url: 'https://github.com/Rahulksnag/saucedemo_automation.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "Creating virtual environment and installing dependencies..."
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests with pytest..."
                bat '''
                    call venv\\Scripts\\activate
                    pytest --alluredir=reports/allure-results -v -s
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo "Generating Allure report..."
                allure includeProperties: false, jdk: '', commandline: 'allure', results: [[path: 'reports/allure-results']]
            }
        }
    }

    post {
        always {
            echo "Tests completed. Check the Allure report section in Jenkins."
        }
    }
}
