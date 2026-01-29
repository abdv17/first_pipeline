
pipeline {
  agent any
  environment {
    APP_ENV = 'ci'
    BUILD_OWNER = 'Sai'
  }

  stages {
    stage('print env vars') {
      steps {
        echo "APP_ENV is ${APP_ENV}"
        echo "BUILD_OWNER is ${BUILD_OWNER}"
      }

    }
    stage('checkout') {
      steps {
        checkout scm
        echo 'Code checked out successfully'
      }

    }
    stage('workspaceproof') {
      steps {
        sh 'pwd'
        sh 'ls -la'
      }
    }
    stage('ControlledFailure') {
      steps {
        script {
          def status = sh(script: 'exit 1', returnStatus: true)
          echo "command exited with ${status}, but pipeline continues"
        }
      }

    }
    stage('Setup VirtualEnv') {
      steps {
        sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
            playwright install
        '''
      }

    }
    stage('RunPython') {
      steps {
        sh '''
          . venv/bin/activate
          python hello.py
          pytest tests/test_login.py
        '''
      }
    }
    stage('build') {
      steps {
        echo 'Build stage running successfully'
      }

    }
  }
}
