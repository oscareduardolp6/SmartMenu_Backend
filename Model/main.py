import sys 

sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Model/')

from Product import Product

newProduct = Product(1, 'Tortillas', 'Tortilleria',price = 5, required = True)
newProduct.save()
print("Ejecutado")