import datetime
from Product import Product
from ProductsRepository import ProductsRepository

class ProductController: 
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
  
  def getAllProducts(self): 
    return ProductsRepository.getAllProducts() 

  def getProductByName(self, name): 
    return ProductsRepository.getProductByName(name) 

  def getProductByID(self, id):
    return ProductsRepository.getProductByID(id) 


