import mariadb 
import sys 

class ConnectionManager: 
  __conn = None 

  def get_connection(self):
    try: 
      self.__conn = mariadb.connect(
        user      = 'root', 
        password  = '', 
        host      = '127.0.0.1', 
        port      = 3306, 
        database  = 'casa_v1'
      )
    except mariadb.Error as ex: 
      print(f"Error al conectarse a la base de datos: {ex}")
      sys.exit(1)
    return self.__conn 

  def close_connection(self): 
    self.__conn.close()
