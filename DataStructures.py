class EmptyQueue(Exception):
  ...
"""
class PriorityQueue:
  def __init__(self, priority: str):
    self.__queue: list[int] = []
    self.__priority: str = priority

  # agrega al final de la cola
  def enqueue(self, element: int):
    self.__queue.append(element)
    if(self.__priority == "max"):
      self.__queue.sort()
    elif(self.__priority == "min"):
      self.__queue.sort(reverse = True)

  # retorna y elimina el primer elemento que entró
  def dequeue(self) -> int:
    if(len(self.__queue) == 0):
      raise EmptyQueue("Cola Vacía...")
    return self.__queue.pop(0)

  # retorna el primer elemento que entró
  def first(self) -> int:
    if(len(self.__queue) == 0):
      raise EmptyQueue("Cola Vacía...")
    return self.__queue[0]

  def __repr__(self):
    return str(self.__queue)

  def __len__(self):
    return len(self.__queue)
"""

class PriorityQueue:
  def __init__(self, priority: str = "min", key=lambda x: x):
    self.__queue = []
    self.__priority = priority
    self.__key = key

  def enqueue(self, element):
    self.__queue.append(element)
    self.__queue.sort(key=self.__key, reverse=(self.__priority == "min"))

  def dequeue(self):
    if not self.__queue:
      raise EmptyQueue("Cola Vacía...")
    return self.__queue.pop(0)

  def first(self):
    if not self.__queue:
      raise EmptyQueue("Cola Vacía...")
    return self.__queue[0]

  def find_by_id(self, id_buscado):
    for elem in self.__queue:
      if hasattr(elem, "id") and elem.id == id_buscado:
        return elem
    return None

  def __repr__(self):
    return "\n".join([str(e) for e in self.__queue])

  def __len__(self):
    return len(self.__queue)
