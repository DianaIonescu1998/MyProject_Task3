pipeline {
	agent any
	environment{
		PATH = "/usr/local/src/apache-maven/bin:/usr/local/bin:/bin:/usr/local/sbin:/usr/sbin"
		M2_HOME = "/usr/local/src/apache-maven"
	}
	stages {
		stage('Stage 1'){
			steps {
				echo 'Hello!'
				sh 'mvn clean'	
			}
		}
		stage('Stage 2'){
			steps {
				echo 'I am...'
				sh 'mvn package'	
			}
		}
		stage('Stage 3'){
			steps {
				echo 'I am testing..'
				sh 'mvn test'
			}
		}
		
	}
}















