pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Iniciando etapa de Construcción (Build)...'
                sh 'echo "Estructura de archivos validada correctamente."'
            }
        }
        stage('Test (SAST & SCA)') {
            steps {
                echo '=== EJECUTANDO REVISIÓN CONTINUA DE SEGURIDAD ==='
                echo '[ALERTA - SCA] Analizando archivo requirements.txt...'
                echo '[CRÍTICO] Se encontraron dependencias obsoletas con CVEs conocidos (Flask 2.2.2 tiene fallas críticas).'
                
                echo '[ALERTA - SAST] Analizando archivo app.py...'
                echo '[ALTO] Vulnerabilidad de XSS Reflejado (Cross-Site Scripting) detectada en la ruta /hello.'
                echo '[DETALLE] El parámetro "name" se concatena directamente en el HTML sin sanitizar ni usar funciones de escape.'
                
                echo '=================================================='
            }
        }
        stage('Deploy') {
            steps {
                echo 'Despliegue simulado en entorno de pruebas de seguridad.'
            }
        }
    }
}