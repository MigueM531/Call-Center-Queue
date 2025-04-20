from DataStructures import PriorityQueue, EmptyQueue
import time
from time import sleep
from mensajes import lineas


class Mensaje:
  contador_id = 0
  palabras_clave = {
    "emergencia": 10, "urgente": 8, "fallo crítico": 9,
    "problema": 5, "consulta": 2, "duda": 1
    }

  def __init__(self, contenido) -> None:
    Mensaje.contador_id += 1
    self.id = Mensaje.contador_id
    self.contenido = contenido
    self.longitud = len(contenido.strip())
    self.peso_mensaje: int = 0
    self.calcular_peso_palabras()

  def calcular_peso_palabras(self) -> int:
      self.peso_mensaje = 0
      for palabra, peso in Mensaje.palabras_clave.items():
        if palabra in self.contenido.lower():
          self.peso_mensaje += peso
      return self.peso_mensaje


  def encolar():
    cola_priorizada = PriorityQueue("min", key=lambda x: x.peso_mensaje)
    for mensaje in mensajes:
      mensaje.calcular_peso_palabras()
      cola_priorizada.enqueue(mensaje)
    return cola_priorizada

  def calcular_dificultad_mensaje(self):
    for _ in mensajes:
      dificultad_mensaje = self.longitud + self.peso_mensaje
    return dificultad_mensaje

  def __repr__(self):
    return f"ID: {self.id}; LONG: {self.longitud}; PESO: {self.peso_mensaje}"


class Agente:
  contador_id = 0
  def __init__(self, nivel_experiencia, estado = "disponible"):
   Agente.contador_id += 1
   self.id = Agente.contador_id
   self.nivel_experiencia: str = nivel_experiencia 
   self.estado: str = estado
   self.tiempo_respuesta = 0
   self.calcular_tiempo_respuesta()
  
  def calcular_tiempo_respuesta(self, mensaje) -> float:
    

  def calcular_factor_respuesta(self) -> float:
     factores = {"basico": 1.0, "intermedio": 0.75, "experto": 0.5}
     return factores.get(self.nivel_experiencia, 1.0)
    



#----------------------------------------------------------------------------------------
mensajes = [Mensaje(linea) for linea in lineas]
for mensaje in mensajes:
  print(mensaje)
cola = Mensaje.encolar()
print("COLA DE MENSAJES:")
print(cola)

