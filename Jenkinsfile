pipeline {
	agent any
	environment{
		PATH = "/usr/local/src/apache-maven/bin:/usr/local/bin:/bin:/usr/local/sbin:/usr/sbin"
		M2_HOME = "/usr/local/src/apache-maven"
	}
	stages {
		stage('Clean'){
			steps {
				echo 'Clean'
				sh 'mvn clean'	
			}
		}
		stage('Test'){
			steps {
				echo 'Test'
				sh 'mvn test'	
			}
		}
		stage('Package'){
			steps {
				echo 'Package'
				sh 'mvn package'
			}
		}
		stage('Deploy'){
			steps {
				echo "Deploy"
				sh 'ssh root@192.168.33.11 "scp root@192.168.33.12:${WORKSPACE}/rpm/target/rpm/unixutils-test-rpm/RPMS/noarch/unixutils-test-rpm-1.0.0-1.0.0.noarch ~/ ; rpm -e  unixutils-test-rpm-1.0.0-1.0.0.noarch" '
				sh 'rpm -ivh unixutils-test-rpm-1.0.0-1.0.0.noarch'
			}
		}
		
		
	}
}















