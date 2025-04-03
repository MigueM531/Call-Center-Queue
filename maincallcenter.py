from DataStructures import PriorityQueue, EmptyQueue, Queue
from typing import Literal
from time import sleep
from mensajes import lineas


class Mensaje:
  contador = 0
  palabras_clave = {
    "emergencia": 10, "urgente": 8, "fallo crítico": 9,
    "problema": 5, "consulta": 2, "duda": 1}

  def __init__(self, contenido) -> None:
    Mensaje.contador += 1
    self.id = Mensaje.contador
    self.contenido = contenido
    self.longitud = len(contenido.strip())
    #self.peso_palabras_clave = self.calcular_peso_palabras()

  """
  #def calcular_prioridad(self) -> int:
  #  prioridad = 0
  #  for palabra, peso in self.palabras_clave.items():
  #    if palabra in self.contenido.lower():
  #      prioridad += peso
  #  return prioridad"
  """

  def calcular_peso_palabras(self) -> int:
    peso_total = 0
    contenido_lower = self.contenido.lower().split()
    for palabra, peso in self.palabras_clave.items():
      peso_total += contenido_lower.count(palabra) * peso
    return peso_total
  
  def encolar(self, contenido_lower):
    cola_priorizada = Queue()
    for self.contenido in mensajes:
      if contenido_lower.peso_total > 0:
        cola_priorizada.enqueue(self.contenido)
      print(cola_priorizada)
    return cola_priorizada

  def __str__(self):
    return f"{self.id}, {self.contenido}"


class Agente:
  def __init__(self, id, nivel_experiencia, estado):
    self.id: int = id
    self.nivel_experiencia: Literal["basico", "intermedio", "experto"] = nivel_experiencia
    self.estado: Literal["disponible", "ocupado"] = estado
    #self.tiempo_de_respuesta = self.calcular_tiempo_respuesta()

  def calcular_factor_respuesta(self, nivel_experiencia) -> float:
    if nivel_experiencia == "basico":
      factor_respuesta = 1
    elif nivel_experiencia == "intermedio":
      factor_respuesta = 0.75
    elif nivel_experiencia == "experto":
      factor_respuesta == 0.5
    return factor_respuesta

  def calcular_tiempo_respuesta(self, factor_respuesta, tiempo_de_respuesta):
    tiempo_estimado = (len(Mensaje()) / 10) + (self.peso_palabras_clave / 2)
    tiempo_de_respuesta = tiempo_estimado * factor_respuesta
    return tiempo_de_respuesta

  def __str__(self):
    return f"agente id: {self.id}, nivel: {self.nivel_experiencia}, estado: {self.estado}"


mensajes = [Mensaje(linea) for linea in lineas]
for mensaje in mensajes:
  print(f"ID: {mensaje.id}; LONGITUD: {mensaje.longitud}; CONTENIDO: {mensaje.contenido}")