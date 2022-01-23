import sys 

sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Model/')
sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Database/')

from Product import Product

newProduct = Product(
  1, 
  'Cereal', 
  'Kellogs',
  variation = 'ChocoKrispis',
  price = 5, 
  required = True
)

newProduct.save()

print("Ejecutado")