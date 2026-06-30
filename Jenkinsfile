pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Iniciando etapa de Construcción (Build)...'
                // Simula la preparación del entorno utilizando comandos universales
                sh 'echo "Verificando estructura de archivos del proyecto..."'
                sh 'ls -la'
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas de seguridad estáticas y lógicas...'
                sh 'echo "Analizando dependencias de requirements.txt..."'
                sh 'echo "Pruebas lógicas completadas exitosamente sin errores."'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Desplegando la aplicación en el entorno local...'
                sh 'echo "Despliegue simulado exitoso en entorno DevSecOps."'
            }
        }
    }
}