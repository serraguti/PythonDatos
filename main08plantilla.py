#from services import service08oracleplantilla as service
#from services import service08sqlserverplantilla as service
from services import service08mysqlplantilla as service
from models.plantilla import Plantilla

print("Ejemplo final BBDD")
servicio = service.ServicePlantilla()
empleados = servicio.getPlantilla()
for emp in empleados:
    print(f"Apellido: {emp.apellido}, Función: {emp.funcion}, Salario: {emp.salario}, Hospital: {emp.hospital}")
#HACEMOS LA FUNCIONALIDAD PARA INCREMENTAR SALARIOS POR HOSPITAL
print("Introduzca un incremento para los empleados")
incremento = int(input())
print("Código de Hospital a incrementar")
hospital = int(input())
registros = servicio.updateSalarioPlantilla(incremento, hospital)
print(f"Empleados modificados: {registros}")
print("Fin de programa")