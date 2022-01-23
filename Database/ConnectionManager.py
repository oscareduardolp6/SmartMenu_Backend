import mariadb 
import sys 

class ConnectionManager: 
  conn = None 

  def get_connection(self):
    if self.conn == None : 
      try: 
        self.conn = mariadb.connect(
          user      = 'root', 
          password  = '', 
          host      = '127.0.0.1', 
          port      = 3306, 
          database  = 'casa_v1'
        )
      except mariadb.Error as ex: 
        print(f"Error al conectarse a la base de datos: {ex}")
        sys.exit(1)
      return self.conn
    return self.conn 

  def close_connection(self): 
    self.conn.close()
  


