#!/usr/bin/env python3
"""
Ejemplos de uso de la clase Temporizador
Demuestra diferentes casos de uso y funcionalidades
"""

from temporizador import Temporizador
import time


def ejemplo_basico():
    """Ejemplo básico de uso del temporizador."""
    print("=== EJEMPLO BÁSICO ===")
    
    def alarma():
        print("🔔 ¡ALARMA! El tiempo ha terminado")
    
    # Crear temporizador de 5 segundos
    timer = Temporizador(callback=alarma)
    timer.configurar_tiempo(segundos=5)
    
    print(f"Iniciando temporizador de 5 segundos...")
    timer.iniciar()
    
    # Monitorear hasta que termine
    while timer.esta_activo():
        print(f"⏱️  {timer.obtener_tiempo_formateado()}")
        time.sleep(1)
    
    print("✅ Temporizador completado\n")


def ejemplo_pausa_reanudar():
    """Ejemplo de pausar y reanudar el temporizador."""
    print("=== EJEMPLO PAUSA/REANUDAR ===")
    
    timer = Temporizador()
    timer.configurar_tiempo(segundos=8)
    
    print("Iniciando temporizador de 8 segundos...")
    timer.iniciar()
    
    for i in range(10):
        time.sleep(1)
        print(f"⏱️  {timer.obtener_tiempo_formateado()} - Progreso: {timer.obtener_progreso()*100:.1f}%")
        
        # Pausar en el segundo 3
        if i == 2 and not timer.esta_pausado():
            timer.pausar()
            print("⏸️  PAUSADO por 2 segundos")
            
        # Reanudar en el segundo 5
        if i == 4 and timer.esta_pausado():
            timer.reanudar()
            print("▶️  REANUDADO")
            
        if timer.ha_terminado():
            print("🔔 ¡Tiempo agotado!")
            break
    
    print("✅ Ejemplo completado\n")


def ejemplo_temporizador_cocina():
    """Ejemplo práctico: temporizador de cocina."""
    print("=== TEMPORIZADOR DE COCINA ===")
    
    def pasta_lista():
        print("🍝 ¡La pasta está lista! Apaga el fuego.")
    
    # Temporizador para pasta (8 minutos)
    timer_pasta = Temporizador(callback=pasta_lista)
    timer_pasta.configurar_tiempo(minutos=8)
    
    print("🔥 Poniendo pasta a hervir...")
    print("⏰ Configurando temporizador para 8 minutos")
    timer_pasta.iniciar()
    
    # Simular trabajo en la cocina
    tiempo_simulado = 0
    while timer_pasta.esta_activo() and tiempo_simulado < 10:
        time.sleep(1)  # En realidad serían 60 segundos por minuto
        tiempo_simulado += 1
        
        minutos_restantes = timer_pasta.obtener_tiempo_restante() / 60
        print(f"🍝 Pasta cocinándose... {minutos_restantes:.1f} minutos restantes")
        
        # Simular que revisamos a los 4 minutos (pausamos brevemente)
        if tiempo_simulado == 4:
            timer_pasta.pausar()
            print("👀 Revisando la pasta... (pausando temporizador)")
            time.sleep(1)
            timer_pasta.reanudar()
            print("✅ Todo bien, continuando...")
    
    print("✅ Temporizador de cocina completado\n")


def ejemplo_multiples_temporizadores():
    """Ejemplo con múltiples temporizadores simultáneos."""
    print("=== MÚLTIPLES TEMPORIZADORES ===")
    
    def callback_cafe():
        print("☕ ¡El café está listo!")
    
    def callback_huevos():
        print("🥚 ¡Los huevos están listos!")
    
    def callback_tostadas():
        print("🍞 ¡Las tostadas están listas!")
    
    # Crear múltiples temporizadores
    timer_cafe = Temporizador(callback=callback_cafe)
    timer_huevos = Temporizador(callback=callback_huevos)
    timer_tostadas = Temporizador(callback=callback_tostadas)
    
    # Configurar tiempos diferentes
    timer_cafe.configurar_tiempo(segundos=6)      # Café: 6 segundos
    timer_huevos.configurar_tiempo(segundos=4)    # Huevos: 4 segundos
    timer_tostadas.configurar_tiempo(segundos=3)  # Tostadas: 3 segundos
    
    print("🍳 Preparando desayuno...")
    print("☕ Iniciando café (6s)")
    timer_cafe.iniciar()
    
    print("🥚 Iniciando huevos (4s)")
    timer_huevos.iniciar()
    
    print("🍞 Iniciando tostadas (3s)")
    timer_tostadas.iniciar()
    
    # Monitorear todos los temporizadores
    while (timer_cafe.esta_activo() or timer_huevos.esta_activo() or timer_tostadas.esta_activo()):
        print(f"⏱️  Café: {timer_cafe.obtener_tiempo_formateado()} | "
              f"Huevos: {timer_huevos.obtener_tiempo_formateado()} | "
              f"Tostadas: {timer_tostadas.obtener_tiempo_formateado()}")
        time.sleep(1)
    
    print("🍽️ ¡Desayuno completo!\n")


def ejemplo_temporizador_ejercicio():
    """Ejemplo de temporizador para rutina de ejercicio."""
    print("=== TEMPORIZADOR DE EJERCICIO ===")
    
    def fin_ejercicio():
        print("💪 ¡Tiempo de ejercicio completado! Descansa.")
    
    def fin_descanso():
        print("😴 ¡Tiempo de descanso completado! Siguiente ejercicio.")
    
    # Rutina: 30 segundos ejercicio, 10 segundos descanso (simulado con 3s y 1s)
    ejercicios = ["Flexiones", "Sentadillas", "Plancha", "Burpees"]
    
    for i, ejercicio in enumerate(ejercicios):
        print(f"\n🏃‍♂️ Ejercicio {i+1}/4: {ejercicio}")
        
        # Temporizador de ejercicio
        timer_ejercicio = Temporizador(callback=fin_ejercicio)
        timer_ejercicio.configurar_tiempo(segundos=3)  # 3 segundos simulando 30
        timer_ejercicio.iniciar()
        
        while timer_ejercicio.esta_activo():
            print(f"💪 {ejercicio}: {timer_ejercicio.obtener_tiempo_formateado()}")
            time.sleep(1)
        
        # Descanso entre ejercicios (excepto el último)
        if i < len(ejercicios) - 1:
            print("\n😴 Tiempo de descanso")
            timer_descanso = Temporizador(callback=fin_descanso)
            timer_descanso.configurar_tiempo(segundos=2)  # 2 segundos simulando 10
            timer_descanso.iniciar()
            
            while timer_descanso.esta_activo():
                print(f"😴 Descanso: {timer_descanso.obtener_tiempo_formateado()}")
                time.sleep(1)
    
    print("\n🎉 ¡Rutina de ejercicio completada!")


def menu_interactivo():
    """Menú interactivo para probar el temporizador."""
    print("=== TEMPORIZADOR INTERACTIVO ===")
    print("1. Crear temporizador personalizado")
    print("2. Probar pausa/reanudar")
    print("3. Múltiples temporizadores")
    print("4. Salir")
    
    while True:
        try:
            opcion = input("\nSelecciona una opción (1-4): ").strip()
            
            if opcion == "1":
                segundos = int(input("Ingresa los segundos: "))
                
                def callback_personalizado():
                    print("⏰ ¡Tu temporizador personalizado ha terminado!")
                
                timer = Temporizador(callback=callback_personalizado)
                timer.configurar_tiempo(segundos=segundos)
                timer.iniciar()
                
                while timer.esta_activo():
                    print(f"⏱️  {timer.obtener_tiempo_formateado()}")
                    time.sleep(1)
                
            elif opcion == "2":
                timer = Temporizador()
                timer.configurar_tiempo(segundos=10)
                timer.iniciar()
                
                print("Temporizador iniciado. Comandos: 'p' (pausar), 'r' (reanudar), 'q' (salir)")
                
                while timer.esta_activo():
                    print(f"⏱️  {timer.obtener_tiempo_formateado()}")
                    # Aquí podrías implementar input no bloqueante para comandos
                    time.sleep(1)
                    
            elif opcion == "3":
                ejemplo_multiples_temporizadores()
                
            elif opcion == "4":
                print("¡Hasta luego!")
                break
                
            else:
                print("Opción no válida")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except ValueError:
            print("Por favor, ingresa un número válido")


def main():
    """Función principal que ejecuta todos los ejemplos."""
    print("🕐 EJEMPLOS DE USO DEL TEMPORIZADOR 🕐")
    print("=" * 50)
    
    try:
        ejemplo_basico()
        time.sleep(1)
        
        ejemplo_pausa_reanudar()
        time.sleep(1)
        
        ejemplo_temporizador_cocina()
        time.sleep(1)
        
        ejemplo_multiples_temporizadores()
        time.sleep(1)
        
        ejemplo_temporizador_ejercicio()
        time.sleep(1)
        
        print("\n🎯 Todos los ejemplos completados")
        print("💡 Tip: Puedes importar la clase Temporizador y usarla en tus propios proyectos")
        
    except KeyboardInterrupt:
        print("\n\n👋 Ejemplos interrumpidos por el usuario")


if __name__ == "__main__":
    main()