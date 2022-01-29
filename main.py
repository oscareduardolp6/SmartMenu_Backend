from datetime import datetime
from typing_extensions import Required
from flask import Flask, jsonify, request, send_file
import sys  as sys
import json

sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Model/')
sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Database/')

from ProductEncoder     import ProductEncoder
from ProductsRepository import ProductsRepository 
from Product import Product


app = Flask(__name__)
productsRepo = ProductsRepository()

@app.route('/getProducts')
def getProducts():
  myResponse  = productsRepo.getAllProducts()
  myJson      = json.dumps(myResponse, cls=ProductEncoder)
  return myJson

@app.route('/getProductByName')
def getProductByName(): 
  productName = request.args.get('productName')
  if productName : 
    product     = productsRepo.getProductByName(productName)
    myJson      = json.dumps(product, cls = ProductEncoder)
    return myJson 
  pass 

@app.route('/getProductByID')
def getProductByID(): 
  productID = request.args.get('id')
  productID = int(productID)
  if productID : 
    product = productsRepo.getProductByID(productID)
    myJson  = json.dumps(product, cls= ProductEncoder)
    return myJson
  pass 

@app.route('/addProduct', methods = ['POST'])
def addProduct(): 
  # name        = request.args.get('name') 
  # brand       = request.args.get('brand') or 'Libre'
  # variation   = request.args.get('var') or ''
  # expiration  = request.args.get('exp') or datetime.now()
  # price       = request.args.get('price') or 0
  # required    = bool(request.args.get('req'))
  # active      = True 
  request_json  = request.get_json()
  # name          = request_json['name']
  name          = request_json.get('name') 
  brand         = request_json['brand'] or 'Libre'
  variation     = request_json['variation'] or ''
  #expiration    = request_json['expiration'] or datetime.now()
  expiration    = request_json.get('expiration') or datetime.now()
  price         = request_json['price'] or 0 
  #required      = bool(request_json['req']) 
  required      = bool(request_json.get('required'))
  active        = True

  
  if not name : 
    return 'Error, no se puede registrar un producto sin nombre'
  newProduct = Product(
    1, 
    name, 
    brand,
    variation, 
    expiration, 
    price, 
    required, 
    active
  )
  newProduct.save()
  return 'OK'

  
  
# app.run(debug = True, port  = 8000)
if __name__ == "__main__":
  host  = '127.0.0.1'
  debug = True
  app.run(
    host  = host, 
    debug = True 
  )