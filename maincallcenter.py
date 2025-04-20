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
    self.longitud = len(contenido.split())
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


  def __repr__(self):
    return f"ID: {self.id}; LONG: {self.longitud}; PESO: {self.peso_mensaje}"


class Agente:
  contador_id = 0
  def __init__(self, nivel_experiencia, estado = "disponible"):
   Agente.contador_id += 1
   self.id = Agente.contador_id
   self.nivel_experiencia: str = nivel_experiencia 
   self.factor_respuesta = 0
   self.estado: str = estado
   self.tiempo_respuesta = 0
   self.obtener_factor()
   self.calcular_tiempo_respuesta()
  
  def obtener_factor(self):
    if self.nivel_experiencia == "basico":
      self.factor_respuesta = 1.0
    elif self.nivel_experiencia == "intermedio":
      self.factor_respuesta = 0.75
    elif self.nivel_experiencia == "experto":
      self.factor_respuesta = 0.50
    
    return self.factor_respuesta
  
  def calcular_tiempo_respuesta(self) -> float:
    for mensaje in mensajes:
     tiempo_estimado = (mensaje.longitud/10) + (mensaje.peso_mensaje/2)
     self.tiempo_respuesta = tiempo_estimado * self.factor_respuesta

    return round(self.tiempo_respuesta) 
  
  def __repr__(self):
    return f"ID: {self.id}; Nivel: {self.nivel_experiencia}; factor: {self.factor_respuesta}; estado:{self.estado}; tiempo:{self.tiempo_respuesta}"

    

#----------------------------------------------------------------------------------------
mensajes = [Mensaje(linea) for linea in lineas]
#for mensaje in mensajes:
#  print(mensaje)
#cola = Mensaje.encolar()
#print("COLA DE MENSAJES:")
#print(cola)

agente= Agente("basico")
agente01= Agente("intermedio")
print (agente)
print (agente01)
