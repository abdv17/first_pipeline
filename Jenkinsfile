
pipeline {
  agent any
  environment {
    APP_ENV = 'ci'
    BUILD_OWNER = 'Sai'
  }

  stages {
    stage('clean') {
      steps {
        deleteDir()
      }
    }
    stage('print env vars') {
      steps {
        echo 'This is env vars section'
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
        // python hello.py
        // pytest tests/test_login.py --html=reports/test_report.html --junitxml=reports/test_report.xml
        sh '''
          . venv/bin/activate

        '''
      }
    }

    stage('Run Tests') {

      steps {
        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE'){
          sh '''
            . venv/bin/activate
            pytest tests --junitxml=reports/test_report.xml --html=reports/test_report.html
          '''
        }
      }
    }

    stage('build') {
      steps {
        echo 'Build stage running successfully'
      }

    }

    stage('Publish Test Results') {
      steps {
        junit 'reports/*.xml'
      }
    }

    post {
      always {
        archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
      }
      unstable {
        echo 'Some test failed. Please check report'
      }
    }


  }
}
