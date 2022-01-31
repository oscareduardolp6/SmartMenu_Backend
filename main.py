from datetime import datetime
from flask import Flask , request 
from flask_cors import CORS, cross_origin 
import sys  as sys
import json

sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Model/')
sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Database/')
sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Routes/')

from ProductEncoder     import ProductEncoder
from ProductsRepository import ProductsRepository 
from Routes.ProductRoutes import parseProduct
from Product import Product

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

productsRepo = ProductsRepository()
NoneType = type(None)

@app.route('/getProducts')
def getProducts():
  myResponse  = productsRepo.getAllProducts()
  myJson      = json.dumps(myResponse, cls = ProductEncoder)
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
  productID = int(request.args.get('id')) 
  if productID : 
    product = productsRepo.getProductByID(productID)
    myJson  = json.dumps(product, cls = ProductEncoder)
    return myJson
  pass 

@app.route('/addProduct', methods = ['POST']) 
def addProduct(): 
  request_json = request.get_json(force = True)
  newProduct = parseProduct(request_json) 
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