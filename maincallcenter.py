from DataStructures import PriorityQueue, EmptyQueue, Queue
from typing import Literal
from time import sleep
from mensajes import lineas
import time


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
    cola_priorizada = Queue()
    for self.peso_mensaje in mensajes:
      if contenido_lower.peso_total > 0:
        cola_priorizada.enqueue(self.contenido)
      print(cola_priorizada)
    return cola_priorizada

  def __str__(self):
    return f"{self.id}, {self.contenido}"


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
  print(f"ID: {mensaje.id}; LONGITUD: {mensaje.longitud}; CONTENIDO: {mensaje.contenido}; PESO: {Mensaje.calcular_peso_palabras(self=mensaje)}")

