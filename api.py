import sys as sys
sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Model/')
sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Database/')
from ProductsRepository import ProductsRepository

repo = ProductsRepository()

print(repo.getAllProducts())