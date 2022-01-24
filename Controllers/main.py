from datetime import datetime
from datetime import timedelta
import sys

sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Model/')
sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Database/')

from ProductController import ProductController 

controller = ProductController()

name        = 'Refresco'
brand       = 'Peñafiel'
variation   = 'Naranjada'
expiration  = datetime.now() + timedelta(days = 30) 
price       = 22
required_   = False

controller.addProduct(name, brand, variation, expiration, price, required_)

productos = controller.getAllProducts()

for product in productos: 
  print(product.name)

producto = controller.getProductByName('Refresco')

changes = { price: 33 }

result = controller.updateProduct(producto.getID(), changes)

result2 = controller.removeProduct(17)

print('Eliminacion ' + result2) 

productos = controller.getAllProducts()

for product in productos: 
  print(product.name)