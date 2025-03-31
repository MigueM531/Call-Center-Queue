from DataStructures import PriorityQueue, EmptyQueue
from typing import Literal
import mensajes

class Mensaje:

  palabras_clave = {
    "emergencia": 10, "urgente": 8, "fallo crítico": 9,
    "problema": 5, "consulta": 2, "duda": 1}

  def __init__(self, id, contenido) -> None:
    self.id = id
    self.contenido: str = contenido
    self.longitud = len(contenido.split())
    #self.prioridad = self.calcular_prioridad()
    self.peso_palabras_clave = self.calcular_peso_palabras()

  def obtener_contenido(self, contenido):
    for mensaje_actual in mensajes:
      contenido = mensaje_actual
    return contenido

  #def calcular_prioridad(self) -> int:
  #  prioridad = 0
  #  for palabra, peso in self.palabras_clave.items():
  #    if palabra in self.contenido.lower():
  #      prioridad += peso
  #  return prioridad

  def calcular_peso_palabras(self) -> int:
    peso_total = 0
    contenido_lower = self.contenido.lowel().split()
    for palabra, peso in self.palabras_clave.items():
      peso_total += contenido_lower.count(palabra) * peso
    return peso_total
  
  def encolar(self):
    ...


class Agente:
  def __init__(self, id, nivel_experiencia, estado, tiempo_de_respuesta):#pendiente tiempo de respuesta
    self.id: int = id
    self.nivel_experiencia: Literal["basico", "intermedio", "experto"] = nivel_experiencia
    self.estado: Literal["disponible", "ocupado"] = estado
    self.tiempo_de_respuesta = tiempo_de_respuesta

  def calcular_factor_respuesta(self, nivel_experiencia) -> float:
    if nivel_experiencia == "basico":
      factor_respuesta = 1
    elif nivel_experiencia == "intermedio":
      factor_respuesta = 0.75
    elif nivel_experiencia == "experto":
      factor_respuesta == 0.5
    return factor_respuesta

  def calcular_tiempo_respuesta(self, factor_respuesta, tiempo_de_respuesta):
    tiempo_estimado = (len(Mensaje) / 10) + (self.peso_palabras_clave / 2)
    tiempo_de_respuesta = tiempo_estimado * factor_respuesta
    return tiempo_de_respuesta

  
