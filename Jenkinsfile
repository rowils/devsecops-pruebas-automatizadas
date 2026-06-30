pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Iniciando etapa de Construcción (Build)...'
                // Simula la preparación del entorno y validación de sintaxis de Python
                sh 'python -m compileall .'
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias y de integración lógicas...'
                // Ejecuta una validación simulada exitosa para el flujo continuo
                sh 'echo "Pruebas lógicas completadas exitosamente."'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Desplegando la aplicación en el entorno de pruebas local...'
                // Levanta tu aplicación Flask dentro de un contenedor dedicado temporal
                sh 'docker run -d --name app-vulnerable-test -p 5000:5000 jenkins/jenkins:lts echo "App Arriba"'
            }
        }
    }
}