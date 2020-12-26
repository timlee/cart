pipeline{

    agent any

    tools{
       maven 'mvn' 
    }
  

    stages{
        stage('build'){
            steps{
                echo 'this is the build job'
                sh 'mvn compile'
            }
        }
        stage('test'){
            steps{
                echo 'this is the test job'
                sh 'mvn clean test'
            }
        }
        stage('package'){
            steps{
                echo 'this is the package job'
                sh 'mvn package -DskipTests'
            }
        }
    }
    
    post{
        always{
            echo 'this pipeline has completed...'
        }
        
    }
    
}
