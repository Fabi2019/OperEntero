# Aplicación Android "Hola Mundo"

Esta es una aplicación básica de Android que muestra "¡Hola Mundo!" en español.

## 📱 Características

- Aplicación nativa para Android
- Interfaz simple y limpia con el mensaje "¡Hola Mundo!"
- Mensaje de bienvenida adicional
- Colores y tema personalizados
- Compatible con Android API 21+ (Android 5.0 Lollipop y superior)

## 📂 Estructura del Proyecto

```
android-hola-mundo/
├── app/
│   ├── build.gradle              # Configuración de build de la app
│   └── src/main/
│       ├── AndroidManifest.xml   # Manifiesto de la aplicación
│       ├── java/com/example/holamundo/
│       │   └── MainActivity.java # Actividad principal
│       └── res/
│           ├── layout/
│           │   └── activity_main.xml  # Layout principal
│           ├── values/
│           │   ├── strings.xml       # Textos de la app
│           │   ├── colors.xml        # Colores definidos
│           │   └── themes.xml        # Temas de la app
│           └── mipmap-*/             # Íconos de la app
├── build.gradle                  # Configuración de build del proyecto
├── settings.gradle              # Configuración del proyecto
└── gradle.properties           # Propiedades de Gradle
```

## 🛠️ Requisitos para Compilar

Para compilar esta aplicación necesitas:

1. **Java Development Kit (JDK) 8 o superior**
2. **Android SDK** con:
   - Android API 34 (Android 14)
   - Build Tools 34.0.0
   - Platform Tools
3. **Android Studio** (recomendado) o línea de comandos

## 🚀 Cómo Compilar la APK

### Opción 1: Con Android Studio

1. Abre Android Studio
2. Selecciona "Open an existing project"
3. Navega a la carpeta `android-hola-mundo`
4. Espera a que Gradle sincronice el proyecto
5. Ve a `Build > Build Bundle(s)/APK(s) > Build APK(s)`
6. La APK se generará en `app/build/outputs/apk/debug/`

### Opción 2: Línea de Comandos

1. Asegúrate de tener configurado `ANDROID_HOME`:
   ```bash
   export ANDROID_HOME=/path/to/android/sdk
   export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd android-hola-mundo
   ```

3. Compila la APK:
   ```bash
   ./gradlew assembleDebug
   ```

4. La APK se generará en `app/build/outputs/apk/debug/app-debug.apk`

## 📱 Instalación en Dispositivo

### En un dispositivo físico:

1. Habilita "Opciones de desarrollador" en tu dispositivo Android
2. Activa "Depuración USB"
3. Conecta el dispositivo a tu computadora
4. Instala la APK:
   ```bash
   adb install app/build/outputs/apk/debug/app-debug.apk
   ```

### En un emulador:

1. Abre Android Studio
2. Ve a `Tools > AVD Manager`
3. Crea un dispositivo virtual si no tienes uno
4. Arrastra y suelta la APK al emulador

## 🎨 Personalización

### Cambiar el mensaje:
Edita el archivo `app/src/main/res/values/strings.xml`:

```xml
<string name="hello_world">¡Tu mensaje aquí!</string>
<string name="welcome_message">Tu mensaje de bienvenida</string>
```

### Cambiar colores:
Edita el archivo `app/src/main/res/values/colors.xml`:

```xml
<color name="primary_color">#FF6200EE</color>
<color name="text_color">#FF2C3E50</color>
```

### Cambiar el ícono:
Reemplaza los archivos en las carpetas `app/src/main/res/mipmap-*/` con tus propios íconos.

## 🔧 Resolución de Problemas

### Error: SDK no encontrado
- Asegúrate de tener el Android SDK instalado
- Configura correctamente la variable `ANDROID_HOME`
- Acepta las licencias del SDK: `sdkmanager --licenses`

### Error: Build Tools no encontrados
- Instala las Build Tools: `sdkmanager "build-tools;34.0.0"`

### Error: Gradle no encontrado
- Usa el wrapper incluido: `./gradlew` en lugar de `gradle`

## 📄 Archivos Importantes

- **MainActivity.java**: Contiene la lógica principal de la aplicación
- **activity_main.xml**: Define la interfaz de usuario
- **strings.xml**: Contiene todos los textos de la aplicación
- **AndroidManifest.xml**: Declara las características y permisos de la app

## 🎯 Características de la App

- **Nombre**: Hola Mundo
- **Package**: com.example.holamundo
- **Versión**: 1.0
- **API Mínima**: 21 (Android 5.0)
- **API Target**: 34 (Android 14)

## 📝 Notas Importantes

- Esta es una aplicación de ejemplo con fines educativos
- Los íconos incluidos son placeholders y deben ser reemplazados con íconos reales
- Para publicar en Google Play Store, necesitarás firmar la APK con una clave de release

## 🆘 Soporte

Si tienes problemas compilando la aplicación:

1. Verifica que tienes todos los requisitos instalados
2. Revisa los logs de error en Android Studio
3. Asegúrate de que las variables de entorno estén configuradas correctamente
4. Intenta limpiar y reconstruir el proyecto: `./gradlew clean assembleDebug`

¡Disfruta tu primera aplicación Android "Hola Mundo"! 🎉