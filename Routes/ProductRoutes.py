from cmath import exp
from datetime import datetime
from Product import Product

def parseProduct(json: dict): 
  if json: 
    id          = json.get('id') or 1 
    name        = json.get('name') 
    brand       = json.get('brand') or 'Libre'
    variation   = json.get('variation') or ''
    expiration  = json.get('expiration') or datetime.now()
    price       = json.get('price') or 0 
    required    = bool(json.get('required'))
    active      = True
  if not name: 
    raise Exception('No se puede registrar Producto sin nombre')
  new_product = Product(
    id, 
    name, 
    brand, 
    variation,
    expiration, 
    price,
    required, 
    active
  )
  return new_product
    
  