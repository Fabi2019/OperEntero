#!/bin/bash

# Script para compilar la APK "Hola Mundo"
# Este script automatiza el proceso de compilación

echo "🚀 Compilando APK 'Hola Mundo'..."
echo "=================================="

# Verificar si existe Java
if ! command -v java &> /dev/null; then
    echo "❌ Error: Java no está instalado."
    echo "   Por favor instala JDK 8 o superior."
    exit 1
fi

echo "✅ Java encontrado: $(java -version 2>&1 | head -n 1)"

# Verificar ANDROID_HOME
if [ -z "$ANDROID_HOME" ]; then
    echo "⚠️  ANDROID_HOME no está configurado."
    echo "   Intentando detectar SDK de Android..."
    
    # Intentar encontrar Android SDK en ubicaciones comunes
    POTENTIAL_PATHS=(
        "$HOME/Android/Sdk"
        "$HOME/Library/Android/sdk"
        "/opt/android-sdk"
        "/usr/local/android-sdk"
    )
    
    for path in "${POTENTIAL_PATHS[@]}"; do
        if [ -d "$path" ]; then
            export ANDROID_HOME="$path"
            echo "✅ Android SDK encontrado en: $ANDROID_HOME"
            break
        fi
    done
    
    if [ -z "$ANDROID_HOME" ]; then
        echo "❌ Error: No se pudo encontrar Android SDK."
        echo "   Por favor instala Android SDK y configura ANDROID_HOME."
        exit 1
    fi
fi

# Configurar PATH
export PATH="$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools"

echo "🔧 Configuración:"
echo "   ANDROID_HOME: $ANDROID_HOME"
echo "   Java: $(java -version 2>&1 | head -n 1)"

# Verificar si Gradle wrapper existe
if [ ! -f "./gradlew" ]; then
    echo "❌ Error: gradlew no encontrado."
    echo "   Este script debe ejecutarse desde el directorio del proyecto Android."
    exit 1
fi

# Hacer ejecutable el gradlew
chmod +x ./gradlew

echo ""
echo "📦 Compilando la aplicación..."
echo "   Esto puede tomar unos minutos la primera vez..."

# Compilar la APK
if ./gradlew assembleDebug; then
    echo ""
    echo "🎉 ¡APK compilada exitosamente!"
    echo ""
    echo "📱 Ubicación de la APK:"
    echo "   app/build/outputs/apk/debug/app-debug.apk"
    echo ""
    echo "🔧 Para instalar en un dispositivo:"
    echo "   adb install app/build/outputs/apk/debug/app-debug.apk"
    echo ""
    echo "📋 Información de la APK:"
    if [ -f "app/build/outputs/apk/debug/app-debug.apk" ]; then
        APK_SIZE=$(du -h app/build/outputs/apk/debug/app-debug.apk | cut -f1)
        echo "   Tamaño: $APK_SIZE"
        echo "   Nombre: Hola Mundo"
        echo "   Package: com.example.holamundo"
        echo "   Versión: 1.0"
    fi
else
    echo ""
    echo "❌ Error al compilar la APK."
    echo "   Revisa los errores anteriores para más información."
    echo ""
    echo "🔧 Posibles soluciones:"
    echo "   1. Verifica que tienes Android SDK instalado"
    echo "   2. Acepta las licencias: sdkmanager --licenses"
    echo "   3. Instala dependencias: sdkmanager 'platforms;android-34' 'build-tools;34.0.0'"
    echo "   4. Limpia el proyecto: ./gradlew clean"
    exit 1
fi