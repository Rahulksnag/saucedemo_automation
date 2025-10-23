pipeline {
    agent any

    environment {
        VENV_PATH = "venv\\Scripts\\activate"
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
            parallel {
                stage('Chrome Tests') {
                    steps {
                        echo "Running tests on Chrome..."
                        bat """
                            call ${VENV_PATH}
                            pytest --browser chrome --alluredir=reports/allure-results/chrome -v -s
                        """
                    }
                }
                stage('Edge Tests') {
                    steps {
                        echo "Running tests on Edge..."
                        bat """
                            call ${VENV_PATH}
                            pytest --browser edge --alluredir=reports/allure-results/edge -v -s
                        """
                    }
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo "Generating Allure report..."
                allure([
                    includeProperties: false,
                    results: [
                        [path: 'reports/allure-results/chrome'],
                        [path: 'reports/allure-results/edge']
                    ]
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
