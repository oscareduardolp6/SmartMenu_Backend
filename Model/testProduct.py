import mariadb 
import datetime
import sys

conn = None

def get_connection(): 
  try :
    conn = mariadb.connect(
      user      = 'root',
      password  = '', 
      host      = '127.0.0.1', 
      port      = 3306, 
      database  = 'casa_v1'
    )
  except mariadb.Error as ex:
    print(f"Error al conectarse a la base de datos: {ex}")
    sys.exit(1)
  return conn

def close_connection():
  conn.close()