import datetime
from Product import Product
from ProductsRepository import ProductsRepository 

class ProductController: 
  def __init__(self) -> None:
    self.repo = ProductsRepository() 

  def addProduct(
    self, 
    name, 
    brand       = 'libre', 
    variation   = '', 
    expiration  = datetime.datetime.now(), 
    price       = 0,
    required    = False, 
  ): 
    product = Product(1, name, brand, variation, expiration, price, required)
    product.save()
    return 'OK'
  
  def getAllProducts(self): 
    return self.repo.getAllProducts()

  def getProductByName(self, name) -> Product: 
    return self.repo.getProductByName(name) 

  def getProductByID(self, id):
    return self.repo.getProductByID(id) 

  def updateProduct(self, id, fieldValueDict : dict): 
    product = self.repo.getProductByID(id)
    for field in fieldValueDict.keys(): 
      print("campo" + str(field))
      if field == 'id': 
        raise Exception('Error: id is an private property')
      value = fieldValueDict[field]
      setattr(product, field, value)
    product.update()
    return 'OK'

  def removeProduct(self, id): 
    product = self.repo.getProductByID(id)
    product.setActive(False)
    product.update()
    return 'OK'