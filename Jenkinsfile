
pipeline {
  agent any
  //parameters {
  //  choice(
  //          name: 'BROWSER',
  //          choices: ['chromium','firefox','webkit'],
  //          description: 'Browser to run tests'
  //  )
  //  choice(
  //          name: 'ENV',
  //          choices: ['qa','stage','prod'],
  //          description: 'Target Environment'
  //  )
  //}
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

    //stage('Run Tests') {
    //
    //  steps {
    //    catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE'){
    //      sh '''
    //        . venv/bin/activate
    //        pytest tests \
    //        --ui-browser=${BROWSER} \
    //        --env=${ENV} \
    //        --junitxml=reports/test_report.xml --html=reports/test_report.html
    //      '''
    //    }
    //  }
    //}

    stage('Paralle Browser Execution') {
      parallel {
        stage('chromium') {
          steps {
            echo 'Running tests on Chromium'
            sh '''
                . venv/bin/activate
                pytest tests \
                --ui-browser=chromium \
                --env=${ENV} \
                --junitxml=reports/chromium.xml --html=reports/test_report.html
            '''
          }

        }
        stage('firefox') {
          steps {
            echo 'Running tests on Firefox'
            sh '''
                . venv/bin/activate
                pytest tests \
                --ui-browser=firefox \
                --env=${ENV} \
                --junitxml=reports/firefox.xml --html=reports/test_report.html
            '''
          }

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
