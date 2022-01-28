from dataclasses import fields
from ConnectionManager import ConnectionManager 
from Product import Product
from ProductFields import ProductFields 

class ProductsRepository: 
  def __init__(self): 
    self.connection_manager = ConnectionManager() 
  
  def getAllProducts(self, _cache={}): 
    products  = []
    conn      = self.connection_manager.get_connection()
    cursor    = conn.cursor()
    query     = """
    SELECT * FROM producto WHERE ACTIVO = 1 
    """
    cursor.execute(query)

    for (ID, NOMBRE, MARCA, VARIANTE, CADUCIDAD, PRECIO, REQUERIDO, ACTIVO) in cursor: 
      product = Product(ID, NOMBRE, MARCA, VARIANTE, CADUCIDAD, PRECIO, REQUERIDO, ACTIVO)  
      products.append(product)
    self.connection_manager.close_connection()
    return products  
  
  def getProductByID(self, id): 
    products = self.getAllProducts()
    product = next(
      (x for x in products if x.getID() == id), 
      None
    )
    return product 

  def getProductByName(self, name): 
    products = self.getAllProducts()
    product = next(
      (x for x in products if x.name.upper() == name.upper()), 
      None
    )
    return product

  def getProductByBrand(self, brand:str): 
    products = self.getAllProducts()
    product = next(
      (x for x in products if x.brand == brand), 
      None
    )
    return product

  def getAllProductsOrderBy(self, field: ProductFields, asc = True) -> list: 
    column    = field.value
    products  = []
    conn      = self.connection_manager.get_connection()
    cursor    = conn.cursor()
    ascDesc   = 'ASC' if asc else 'DESC'

    query= """
    SELECT * FROM producto WHERE ACTIVO = 1 ORDER BY {} {}
    """
    query.format(column, ascDesc)
    cursor.execute(query)
    for (ID, NOMBRE, MARCA, VARIANTE, CADUCIDAD, PRECIO, REQUERIDO, ACTIVO) in cursor: 
      product = Product(ID, NOMBRE, MARCA, VARIANTE, CADUCIDAD, PRECIO, REQUERIDO, ACTIVO)  
      products.append(product)
    self.connection_manager.close_connection()
    return products  
    
  def getProductByFieldEqualsTo(self, field: ProductFields, value, operator) -> Product: 
    column    = field.value
    products  = []
    conn      = self.connection_manager.get_connection()
    cursor    = conn.cursor()
    query     = """
    SELECT * FROM producto WHERE ACTIVO = 1 AND {} {} {}
    """
    query.format(column, operator, value)
    cursor.execute(query)
    for (ID, NOMBRE, MARCA, VARIANTE, CADUCIDAD, PRECIO, REQUERIDO, ACTIVO) in cursor: 
      product = Product(ID, NOMBRE, MARCA, VARIANTE, CADUCIDAD, PRECIO, REQUERIDO, ACTIVO)  
      products.append(product)
    self.connection_manager.close_connection()
    return products