import sqlite3 as sql

class bd(sql.Connection):
    
    def __init__(self, bdNombre):
        super().__init__(bdNombre)
        
    def consultar(self, consulta):
        try:
            self.execute(consulta)
            self.commit()
        except sql.Error as e:
            print(f'Error en la consulta: {e}')
            
    def consulta_datos(self, consulta):
        try:
            cursor = self.cursor()
            cursor.execute(consulta)
            return cursor.fetchall()
        except sql.Error as e:
            print(f'Error en la consulta: {e}')
            return None 