import pyodbc
from models.plantilla import Plantilla

class ServicePlantilla:
    def __init__(self):
        self.connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes') 
    
    def getPlantilla(self):
        sql = "select * from PLANTILLA"
        cursor = self.connection.cursor()
        data:list[Plantilla] = []
        cursor.execute(sql)
        for row in cursor:
            plan = Plantilla()
            plan.idPlantilla = row[2]
            plan.apellido = row[3]
            plan.funcion = row[4]
            plan.salario = row[6]
            plan.hospital = row[0]
            data.append(plan)
        cursor.close()
        return data

    def updateSalarioPlantilla(self, incremento, hospital):
        sql = "update PLANTILLA set SALARIO=SALARIO + ? where HOSPITAL_COD=?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (incremento, hospital))
        registros = cursor.rowcount
        cursor.close()
        return registros