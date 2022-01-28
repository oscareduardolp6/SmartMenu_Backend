import json
from Product import Product 
from datetime import datetime 

class ProductEncoder(json.JSONEncoder): 
  def default(self, obj):
    if isinstance(obj, Product): 
      return {
        'id': obj.getID(),
        'name': obj.name, 
        'brand': obj.brand, 
        'variation': obj.variation, 
        'expiration': obj.expiration.strftime("%d/%m/%Y, %H:%M:%S"), 
        'price': obj.getPrice(),
        'required': obj.getRequired(), 
        'active': obj.getActive()
      }
    return super().default(obj)