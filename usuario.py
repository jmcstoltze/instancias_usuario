
# Define clase usuario
class Usuario():

    # Método constructor con parámetros y atributos
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.genero = genero

    # Método accesador que retorna un diccionario con la información del usuario
    @property
    def obtener_atributos(self) -> str:
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "genero": self.genero
        }

# Módulo de pruebas
if __name__ == "__main__":

    # Crea dos instancias de prueba
    u1 = Usuario('jose', 'contreras', 'abc@abc.com', 'masculino')
    u2 = Usuario('juanita', 'rodriguez', 'def@def.com', 'femenino')

    # Imprime las instancias como objetos
    print(u1)
    print(u2)

    # Imprime un string tipo diccionario con la información de las instancias
    print(u1.obtener_atributos)
    print(u2.obtener_atributos)
