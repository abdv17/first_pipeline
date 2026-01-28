
pipeline {
  agent any 
  stages {
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
    stage('build') {
      steps {
        echo 'Build stage running successfully'
      }

    }
  }
}
