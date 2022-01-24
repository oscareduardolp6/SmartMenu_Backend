import datetime
from ConnectionManager import ConnectionManager

class Product: 
  connection_manager = ConnectionManager()

  def __init__( 
                self, 
                id, 
                name, 
                brand       = 'libre', 
                variation   = '', 
                expiration  = datetime.datetime.now(), 
                price       = 0,
                required    = False, 
                active      = True
              ): 
    self.__id       = id 
    self.name       = name
    self.brand      = brand
    self.variation  = variation 
    self.expiration = expiration
    self.__price    = price
    self.__required = required
    self.__active   = active
  
  def getID(self): 
    return self.__id
  
  def setPrice(self, price): 
    self.__price = price if price.isnumeric() and price >= 0 else 0 
  
  def getPrice(self): 
    return self.__price

  def setRequired(self, required): 
    self.__required = required if isinstance(required, bool) else False 

  def getRequired(self): 
    return self.__required

  def getActive(self): 
    return self.__active

  def setActive(self, active: bool): 
    self.__active = active if isinstance(active, bool) else False 

  def save(self):
    conn    = self.connection_manager.get_connection()
    cursor  = conn.cursor()
    query   = """
    INSERT INTO producto (NOMBRE, MARCA, VARIANTE, CADUCIDAD, PRECIO, REQUERIDO) 
                  VALUES (?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (
      self.name, 
      self.brand, 
      self.variation, 
      self.expiration, 
      self.__price, 
      self.__required
      )
    )
    conn.commit()
    conn.close() 
  
  def update(self): 
    conn    = self.connection_manager.get_connection()
    cursor  = conn.cursor()
    query   = """
    UPDATE producto SET 
      NOMBRE    = ?
      MARCA     = ?
      VARIANTE  = ?
      CADUCIDAD = ?
      PRECIO    = ?
      REQUERIDO = ?
      ACTIVO    = ?
    WHERE ID = ?
    """
    cursor.execute(query, (
      self.name, 
      self.brand, 
      self.variation, 
      self.expiration, 
      self.__price, 
      self.__required, 
      self.__active, 
      self.__id
    ))
    conn.commit()
    conn.close() 
