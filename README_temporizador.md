# 🕐 Clase Temporizador en Python

Una clase completa y fácil de usar para crear temporizadores con funcionalidades avanzadas.

## ✨ Características

- ⏰ Configurar tiempo en **horas, minutos y segundos**
- ▶️ **Iniciar, pausar, reanudar y detener** el temporizador
- 🔔 **Callbacks** para ejecutar funciones cuando termine
- 📊 **Monitoreo** del tiempo restante y progreso
- 🧵 Funciona en **hilos separados** (no bloquea tu programa)
- 🔄 **Múltiples temporizadores** simultáneos

## 🚀 Uso Básico

```python
from temporizador import Temporizador

# Crear temporizador con callback
def alarma():
    print("¡Tiempo agotado!")

timer = Temporizador(callback=alarma)
timer.configurar_tiempo(minutos=5, segundos=30)
timer.iniciar()

# Monitorear el progreso
while timer.esta_activo():
    print(f"Tiempo restante: {timer.obtener_tiempo_formateado()}")
    print(f"Progreso: {timer.obtener_progreso()*100:.1f}%")
    time.sleep(1)
```

## 📋 Métodos Principales

### Configuración
- `configurar_tiempo(horas=0, minutos=0, segundos=0)` - Establece la duración
- `Temporizador(duracion_segundos=0, callback=None)` - Constructor

### Control
- `iniciar()` - Inicia el temporizador
- `pausar()` - Pausa el temporizador
- `reanudar()` - Reanuda después de una pausa
- `detener()` - Detiene completamente
- `reiniciar()` - Reinicia con la duración original

### Información
- `obtener_tiempo_restante()` - Tiempo en segundos (float)
- `obtener_tiempo_formateado()` - Tiempo en formato "HH:MM:SS"
- `obtener_progreso()` - Progreso de 0.0 a 1.0
- `esta_activo()` - ¿Está funcionando?
- `esta_pausado()` - ¿Está en pausa?
- `ha_terminado()` - ¿Ya terminó?

## 💡 Ejemplos de Uso

### Temporizador Simple
```python
timer = Temporizador()
timer.configurar_tiempo(segundos=30)
timer.iniciar()
```

### Temporizador de Cocina
```python
def pasta_lista():
    print("🍝 ¡La pasta está lista!")

timer = Temporizador(callback=pasta_lista)
timer.configurar_tiempo(minutos=8)
timer.iniciar()
```

### Pausa y Reanudación
```python
timer = Temporizador()
timer.configurar_tiempo(minutos=10)
timer.iniciar()

# Más tarde...
timer.pausar()    # Pausa el temporizador
timer.reanudar()  # Continúa desde donde se pausó
```

### Múltiples Temporizadores
```python
timer1 = Temporizador(callback=lambda: print("Timer 1 terminado"))
timer2 = Temporizador(callback=lambda: print("Timer 2 terminado"))

timer1.configurar_tiempo(segundos=30)
timer2.configurar_tiempo(minutos=1)

timer1.iniciar()
timer2.iniciar()
```

## 🎯 Casos de Uso Prácticos

- **🍳 Cocina**: Temporizadores para diferentes platos
- **💪 Ejercicio**: Rutinas con tiempos de ejercicio y descanso
- **📚 Estudio**: Técnica Pomodoro (25 min trabajo, 5 min descanso)
- **🎮 Juegos**: Tiempo límite para turnos o acciones
- **⏰ Recordatorios**: Alarmas personalizadas
- **🏃‍♂️ Deportes**: Cronometraje de entrenamientos

## 📁 Archivos Incluidos

- `temporizador.py` - Clase principal
- `ejemplos_temporizador.py` - Ejemplos completos de uso
- `README_temporizador.md` - Esta documentación

## 🏃‍♂️ Ejecutar Ejemplos

```bash
# Ejemplo básico incluido en la clase
python3 temporizador.py

# Ejemplos completos y variados
python3 ejemplos_temporizador.py
```

## 🔧 Requisitos

- Python 3.6+
- Librerías estándar: `time`, `threading`, `datetime`, `typing`

## 💡 Consejos

1. **Callbacks**: Usa funciones lambda para callbacks simples
2. **Hilos**: Los temporizadores no bloquean tu programa principal
3. **Precisión**: La precisión es de aproximadamente 0.1 segundos
4. **Memoria**: Recuerda detener temporizadores que no necesites
5. **Errores**: La clase maneja errores comunes y te informa qué salió mal

¡Disfruta usando tu nuevo temporizador! 🎉