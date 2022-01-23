import datetime
from Product import Product

class ProductController: 
  def addProduct(
    name, 
    brand       = 'libre', 
    variation   = '', 
    expiration  = datetime.datetime.now(), 
    price       = 0,
    required    = False, 
  ): 
    product = Product(1, name, brand, variation, expiration, price, required)
    product.save()
  
  
