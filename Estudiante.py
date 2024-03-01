class Estudiante:
    def __init__(self, nombre, apellido, correo, telefono, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.cedula = cedula

class Main:
    @staticmethod
    def imprimir_estudiante(estudiante):
        print("Nombre:", estudiante.nombre)
        print("Apellido:", estudiante.apellido)
        print("Correo:", estudiante.correo)
        print("Teléfono:", estudiante.telefono)
        print("Cédula:", estudiante.cedula)
        print("---------------------")

# Ejemplo de uso en el main
if __name__ == "__main__":
    estudiante1 = Estudiante("Daniel", "Altahona", "ddanielalejandroaltahona@gmail.com", "3212800962-3147861572", "1043295629")


    Main.imprimir_estudiante(estudiante1)


