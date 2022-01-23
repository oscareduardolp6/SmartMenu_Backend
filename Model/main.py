import sys

from ProductFields import ProductFields 

sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Model/')
sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Database/')

from Product import Product
from ProductsRepository import ProductsRepository

newProduct = Product(
  1, 
  'Cereal', 
  'Kellogs',
  variation = 'ChocoKrispis',
  price = 5, 
  required = True
)

# newProduct.save()

repo = ProductsRepository()
productos = repo.getAllProducts()
for product_ in productos: 
    print(product_.name)

product = repo.getProductByID(17)
print('Nombre' + product.name) 

product = repo.getProductByName('Cereal')
print('ID: ' + str(product.getID()))

productos = repo.getAllProductsOrderBy(ProductFields.price)


# print('valido: ' + repo.getAllProductsOrderby('id'))



print("Ejecutado")