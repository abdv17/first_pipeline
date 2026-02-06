
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


    stage('Setup VirtualEnv') {
      steps {
        bat '''
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
            catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE'){
              echo 'Running tests on Chromium'
              bat '''
                venv\\Scripts\\activate
                pytest tests -m smoke \
                --browser=chromium \
                --env=${ENV} \
                --retry 2 --retry-delay 1 \
                --junitxml=reports/chromium.xml --alluredir=allure-results
                '''
            }

          }

        }
        //stage('firefox') {
        //  steps {
        //    catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE'){
        //      echo 'Running tests on Firefox'
        //      sh '''
        //        . venv/bin/activate
        //        pytest tests \
        //        --browser=firefox \
        //        --env=${ENV} \
        //        --junitxml=reports/firefox.xml --html=reports/test_report.html
        //        '''
        //    }
        //
        //  }
        //
        //}
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
          allure([

                results:[[path: 'allure-results']]
         ])
    }
    unstable {
      echo 'Some test failed. Please check report'
    }
  }
}
