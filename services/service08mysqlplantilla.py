import pymysql
from models.plantilla import Plantilla

class ServicePlantilla:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', port=3306
            , user='getafe', password='mysql', database='HOSPITAL')   
    
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
        sql = "update PLANTILLA set SALARIO=SALARIO + %s where HOSPITAL_COD=%s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (incremento, hospital))
        registros = cursor.rowcount
        cursor.close()
        return registros