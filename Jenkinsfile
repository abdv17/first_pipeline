pipeline {
  agent {
    docker {
      image 'mcr.microsoft.com/playwright/python:v1.45.0-jammy' // match your Playwright version
      args '--ipc=host' // optional, helps with Chrome stability under heavy parallelism
    }
  }
  stages {
    stage('Install & Test (Python Playwright)') {
      steps {
        sh '''
          python --version
          pip install --upgrade pip
          pip install -r requirements.txt
          # Install Playwright browsers (already present in this image, but safe to ensure)
          python -m playwright install
          # Run tests
          pytest -q --maxfail=1 --disable-warnings --junitxml=reports/junit.xml
        '''
      }
    }
  }
  post {
    always {
      junit 'reports/junit.xml'
      archiveArtifacts artifacts: 'playwright-report/**', fingerprint: true
    }
  }
}
