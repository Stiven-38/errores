# Crear listas vacías
aprendices = []
edades = []

for i in range(30):
    nombre = input("Ingrese el nombre del aprendiz ")
    edad = int(input("Ingrese la edad del aprendiz: "))
    aprendices(nombre)
    edades.append(edad)

print("Lista de aprendices:", aprendices)
print("Lista de edades:", edades)

mayor_edad = edades.index(min(edades))
aprendiz_mayor_edad = aprendices[mayor_edad]
print("El aprendiz con mayor edad es:", aprendiz_mayor_edad)

instructora = "Adriana Lucia Rincon"
(1, instructora)

cantidad18años = edades.count(18)
print("Cantidad de aprendices con 18 años:", cantidad18años)

aprendiz = "Andres"
aprendices.append(aprendiz)


aprendices.remove(instructora)


dato_buscar = input("Ingrese un dato a buscar en la lista de aprendices: ")
if dato_buscar in aprendices:
    print(dato_buscar, "se encuentra en la lista de aprendices.")
else:
    print(dato_buscar, "no se encuentra en la lista de aprendices.")

print("primeros 10 aprendices:", aprendices[:10])

print("Últimos 10 aprendices:", aprendices[10:])

print("Elementos del 10 al 20:", aprendices[9:20])



