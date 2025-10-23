pipeline {
    agent any

    environment {
        VENV_PATH = "venv\\Scripts\\activate"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Rahulksnag/saucedemo_automation.git', branch: 'main'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat "${env.VENV_PATH} && pip install --upgrade pip"
                bat "${env.VENV_PATH} && pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "${env.VENV_PATH} && pytest --alluredir=reports/allure-results -v -s"
            }
        }

        stage('Generate Allure Report') {
    steps {
        allure includeProperties: false, jdk: '', installation: 'Allure', results: [[path: 'reports/allure-results']]
    }
}

    }

    post {
        always {
            echo "Tests completed. Check Allure report."
        }
    }
}
