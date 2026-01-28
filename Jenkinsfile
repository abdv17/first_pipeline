
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
    stage('build') {
      steps {
        echo 'Build stage running successfully'
      }

    }
  }
}
