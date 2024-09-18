print("Programacion POO")
# Definicion de clases
class perro:
    # Funciones dentro de la clase
    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self,nombre,edad):
        print(f"Nombre del perro: {nombre} Edad: {edad}")


# Zona de creacion de objetos
pitbull=perro()



# Zona de uso de objetos

pitbull.Datos_perro("Toby",4)
pitbull.morder()