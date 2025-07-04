import time
import threading
from datetime import datetime, timedelta
from typing import Optional, Callable


class Temporizador:
    """
    Clase para crear y manejar un temporizador con funcionalidades avanzadas.
    
    Características:
    - Configurar tiempo en segundos, minutos u horas
    - Iniciar, pausar, reanudar y detener el temporizador
    - Callbacks para cuando el temporizador termina
    - Monitoreo del tiempo restante y estado
    - Funciona en un hilo separado para no bloquear el programa principal
    """
    
    def __init__(self, duracion_segundos: float = 0, callback: Optional[Callable] = None):
        """
        Inicializa el temporizador.
        
        Args:
            duracion_segundos (float): Duración del temporizador en segundos
            callback (Callable, optional): Función a ejecutar cuando termine el temporizador
        """
        self.duracion_total = duracion_segundos
        self.tiempo_restante = duracion_segundos
        self.callback = callback
        
        # Estados del temporizador
        self.activo = False
        self.pausado = False
        self.terminado = False
        
        # Control de hilos
        self._hilo = None
        self._detener_evento = threading.Event()
        self._pausar_evento = threading.Event()
        
        # Tiempos de control
        self.tiempo_inicio = None
        self.tiempo_pausa = None
        
    def configurar_tiempo(self, horas: int = 0, minutos: int = 0, segundos: float = 0):
        """
        Configura el tiempo del temporizador.
        
        Args:
            horas (int): Horas
            minutos (int): Minutos  
            segundos (float): Segundos
        """
        if self.activo:
            raise ValueError("No se puede configurar el tiempo mientras el temporizador está activo")
            
        total_segundos = horas * 3600 + minutos * 60 + segundos
        self.duracion_total = total_segundos
        self.tiempo_restante = total_segundos
        self.terminado = False
        
    def iniciar(self):
        """Inicia el temporizador."""
        if self.activo:
            raise ValueError("El temporizador ya está activo")
            
        if self.duracion_total <= 0:
            raise ValueError("Debe configurar un tiempo válido antes de iniciar")
            
        self.activo = True
        self.pausado = False
        self.terminado = False
        self.tiempo_inicio = time.time()
        
        # Reiniciar eventos
        self._detener_evento.clear()
        self._pausar_evento.clear()
        
        # Iniciar en un hilo separado
        self._hilo = threading.Thread(target=self._ejecutar, daemon=True)
        self._hilo.start()
        
    def pausar(self):
        """Pausa el temporizador."""
        if not self.activo:
            raise ValueError("El temporizador no está activo")
            
        if self.pausado:
            raise ValueError("El temporizador ya está pausado")
            
        self.pausado = True
        self.tiempo_pausa = time.time()
        self._pausar_evento.set()
        
    def reanudar(self):
        """Reanuda el temporizador después de una pausa."""
        if not self.activo:
            raise ValueError("El temporizador no está activo")
            
        if not self.pausado:
            raise ValueError("El temporizador no está pausado")
            
        # Ajustar el tiempo de inicio considerando el tiempo pausado
        tiempo_pausado = time.time() - self.tiempo_pausa
        self.tiempo_inicio += tiempo_pausado
        
        self.pausado = False
        self._pausar_evento.clear()
        
    def detener(self):
        """Detiene el temporizador completamente."""
        if not self.activo:
            return
            
        self.activo = False
        self.pausado = False
        self._detener_evento.set()
        
        if self._hilo and self._hilo.is_alive():
            self._hilo.join(timeout=1.0)
            
    def reiniciar(self):
        """Reinicia el temporizador con la duración original."""
        self.detener()
        self.tiempo_restante = self.duracion_total
        self.terminado = False
        
    def obtener_tiempo_restante(self) -> float:
        """
        Obtiene el tiempo restante en segundos.
        
        Returns:
            float: Tiempo restante en segundos
        """
        if not self.activo or self.terminado:
            return self.tiempo_restante
            
        if self.pausado:
            tiempo_transcurrido = self.tiempo_pausa - self.tiempo_inicio
        else:
            tiempo_transcurrido = time.time() - self.tiempo_inicio
            
        self.tiempo_restante = max(0, self.duracion_total - tiempo_transcurrido)
        return self.tiempo_restante
        
    def obtener_tiempo_formateado(self) -> str:
        """
        Obtiene el tiempo restante en formato HH:MM:SS.
        
        Returns:
            str: Tiempo formateado
        """
        tiempo = self.obtener_tiempo_restante()
        horas = int(tiempo // 3600)
        minutos = int((tiempo % 3600) // 60)
        segundos = int(tiempo % 60)
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"
        
    def obtener_progreso(self) -> float:
        """
        Obtiene el progreso del temporizador como porcentaje.
        
        Returns:
            float: Progreso entre 0.0 y 1.0
        """
        if self.duracion_total <= 0:
            return 0.0
            
        tiempo_transcurrido = self.duracion_total - self.obtener_tiempo_restante()
        return min(1.0, tiempo_transcurrido / self.duracion_total)
        
    def esta_activo(self) -> bool:
        """Verifica si el temporizador está activo."""
        return self.activo
        
    def esta_pausado(self) -> bool:
        """Verifica si el temporizador está pausado."""
        return self.pausado
        
    def ha_terminado(self) -> bool:
        """Verifica si el temporizador ha terminado."""
        return self.terminado
        
    def _ejecutar(self):
        """Método interno que ejecuta el temporizador en un hilo separado."""
        while self.activo and not self._detener_evento.is_set():
            # Esperar si está pausado
            if self.pausado:
                self._pausar_evento.wait()
                continue
                
            # Verificar si el tiempo se agotó
            if self.obtener_tiempo_restante() <= 0:
                self.terminado = True
                self.activo = False
                
                # Ejecutar callback si existe
                if self.callback:
                    try:
                        self.callback()
                    except Exception as e:
                        print(f"Error ejecutando callback: {e}")
                break
                
            # Esperar un poco antes de verificar nuevamente
            self._detener_evento.wait(0.1)
            
    def __str__(self) -> str:
        """Representación en string del temporizador."""
        estado = "Inactivo"
        if self.activo:
            estado = "Pausado" if self.pausado else "Activo"
        elif self.terminado:
            estado = "Terminado"
            
        return f"Temporizador({self.obtener_tiempo_formateado()}) - Estado: {estado}"
        
    def __repr__(self) -> str:
        """Representación detallada del temporizador."""
        return (f"Temporizador(duracion_total={self.duracion_total}, "
                f"tiempo_restante={self.tiempo_restante:.2f}, "
                f"activo={self.activo}, pausado={self.pausado}, "
                f"terminado={self.terminado})")


# Ejemplo de uso y funciones de utilidad
def ejemplo_uso():
    """Ejemplo de cómo usar la clase Temporizador."""
    
    def cuando_termine():
        print("¡Tiempo agotado! ⏰")
        
    # Crear temporizador de 10 segundos
    timer = Temporizador(callback=cuando_termine)
    timer.configurar_tiempo(segundos=10)
    
    print(f"Temporizador configurado: {timer}")
    
    # Iniciar
    timer.iniciar()
    print("Temporizador iniciado...")
    
    # Simular uso
    for i in range(12):
        time.sleep(1)
        print(f"Tiempo restante: {timer.obtener_tiempo_formateado()} "
              f"({timer.obtener_progreso()*100:.1f}%)")
        
        # Pausar en el segundo 5
        if i == 4 and not timer.esta_pausado():
            timer.pausar()
            print("⏸️  Temporizador pausado")
            
        # Reanudar en el segundo 7
        if i == 6 and timer.esta_pausado():
            timer.reanudar()
            print("▶️  Temporizador reanudado")
            
        if timer.ha_terminado():
            break
            
    print(f"Estado final: {timer}")


if __name__ == "__main__":
    ejemplo_uso()