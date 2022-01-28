# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, send_file
import sys as sys
import json
sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Model/')
sys.path.append('D:/Software/dev/Projects/SmartMenu/Backend/Database/')
from ProductEncoder import ProductEncoder
from ProductsRepository import ProductsRepository 

app = Flask(__name__)
productsRepo = ProductsRepository()

@app.route('/getProducts')
def getProducts():
  myResponse  = productsRepo.getAllProducts()
  myJson      = json.dumps(myResponse, cls=ProductEncoder)
  return myJson

@app.route('/getProduct')
def getProduct(): 
  productName = request.args.get('productName')
  if productName : 
    product     = productsRepo.getProductByName(productName)
    myJson      = json.dumps(product, cls = ProductEncoder)
    return myJson 
  return 'No encontrado'
    
# app.run(debug = True, port  = 8000)
if __name__ == "__main__":
  app.run(host='127.0.0.1')