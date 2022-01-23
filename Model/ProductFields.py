from enum import Enum

class ProductFields(Enum): 
  id          = 'ID'
  name        = 'NOMBRE'
  brand       = 'MARCA'
  variation   = 'VARIANTE'
  expiration  = 'CADUCIDAD'
  price       = 'PRECIO'
  required    = 'REQUERIDO'
  active      = 'ACTIVO'