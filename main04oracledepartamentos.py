from services import service04oracledepartamentos as service
from models import departamento

print("----SERVICIO ORACLE DEPARTAMENTOS")
#NECESITAMOS UNA OBJETO DE TIPO SERVICIO PARA TRABAJAR
servicio = service.ServiceOracleDepartamentos()
print("1.- Insertar departamento")
print("2.- Buscar departamento")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    print("Insertar departamento")
    print("Id del departamento")
    numero = int(input())
    print("Nombre del departamento")
    nombre = input()
    print("Localidad")
    localidad = input()
    afectados = servicio.insertarDepartamento(numero,nombre, localidad)
    print(f"Departamentos insertados: {afectados}")
elif (opcion == 2):
    print("Buscador de departamentos por ID")
    print("Introduzca el id del departamento")
    iddept = int(input())
    #DECLARAMOS UNA VARIABLE PARA GUARDAR EL DEPARTAMENTO
    dept = servicio.buscarDepartamentoId(iddept)
    print(f"{dept.numero}, {dept.nombre}, {dept.localidad}")
print("Fin de programa")