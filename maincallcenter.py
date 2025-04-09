from DataStructures import PriorityQueue, EmptyQueue
import time
from time import sleep
from mensajes import lineas


class Mensaje:
  contador = 0
  palabras_clave = {
    "emergencia": 10, "urgente": 8, "fallo crítico": 9,
    "problema": 5, "consulta": 2, "duda": 1
    }

  def __init__(self, contenido) -> None:
    Mensaje.contador += 1
    self.id = Mensaje.contador
    self.contenido = contenido
    self.longitud = len(contenido.split())
    self.peso_mensaje: int = 0

  def calcular_peso_palabras(self) -> int:
      self.peso_mensaje = 0
      for palabra, peso in Mensaje.palabras_clave.items():
        if palabra in self.contenido.lower():
          self.peso_mensaje += peso
      return self.peso_mensaje
  
  def encolar(self):
    cola_priorizada = PriorityQueue("min")
    for mensaje in mensajes:
      cola_priorizada.enqueue(mensaje.peso_mensaje)
    return cola_priorizada

  def __repr__(self):
    return f"ID: {mensaje.id}; LONGITUD: {mensaje.longitud}\
        | CONTENIDO: {mensaje.contenido}; PESO: {Mensaje.calcular_peso_palabras(self=mensaje)}"


class Agente:
  def __init__(self, id: int, nivel_experiencia: str, estado: str = "disponible"):
   self.id = id 
   self.nivel_experiencia: str = nivel_experiencia 
   self.estado: str = estado
  
  def calcular_factor_respuesta(self) -> float:
     factores = {"basico": 1.0, "intermedio": 0.75, "experto": 0.5}
     return factores.get(self.nivel_experiencia, 1.0)
  
  def calcular_tiempo_respuesta(self, mensaje) -> float:
    pass 



#----------------------------------------------------------------------------------------
mensajes = [Mensaje(linea) for linea in lineas]
for mensaje in mensajes:
  print(mensaje)

print(f"COLA DE MENSAJES POR PRIORIDAD: {Mensaje.encolar(self=Mensaje)}")
