
# Importaciones necesarias para el funcionamiento del script
from usuario import Usuario
import json

# Lista que almacenará las instancias de usuario 
lista_usuarios = []

# Se abre o se crea el archivo de errores para almacenar sin sobrescribir
with open("error.log", "a") as errores:

    # Intenta abrir el archivo y continuar, de lo contrario manejo de excepción
    try:
    
        # Abre el archivo 'usuarios.txt' en modo de lectura
        with open("usuarios.txt", "r") as usuarios:

            # Lee y captura una línea del archivo
            linea = usuarios.readline()

            # Variable auxiliar para identificar el número de línea que se lee
            linea_archivo = 1
    
            # El bucle se realiza mientras exista línea con información
            while linea:
        
                # Intenta la lectura de la información y la creación de la instancia usuario
                try:
        
                    # Toma los datos de la línea en formato json y los almacena en una variable
                    datos_usuario = json.loads(linea)

                    # La línea leída debiese contar con todas las claves esperadas
                    if all(key in datos_usuario for key in ["nombre", "apellido", "email", "genero"]):

                        # La línea leída debiese contar con todos los valores en string
                        if all(isinstance(datos_usuario[key], str) for key in ["nombre", "apellido", "email", "genero"]):
                    
                            # Genera la instancia del usuario con los datos obtenidos para cada clave
                            usuario = Usuario(
                                datos_usuario.get("nombre"),
                                datos_usuario.get("apellido"),
                                datos_usuario.get("email"),
                                datos_usuario.get("genero"),
                            )

                            # Agrega la instancia del usuario a la lista de usuarios
                            lista_usuarios.append(usuario)
                    
                        # Si la línea leída no cuenta con todos sus valores en string
                        else: 

                            # Levanta la excepción de valor y registra el error
                            raise ValueError('Invalid value type in the JSON dictionary\n')
                        
                    # Si la línea leída no cuenta con todas las claves esperadas
                    else:

                        # Levanta la excepción de clave y resgitra el error
                        raise KeyError ('Missing key or keys in the JSON dictionary')
                
                # Crea instancia del error 
                except ValueError as e:
                
                    # Almacena el mensaje de error en el archivo 'error.log'
                    errores.write(f'ERROR - Line {linea_archivo}: {e}\n')

                # Crea instancia del error
                except KeyError as e:

                    # Quita las comillas innecesarias del mensaje
                    e = str(e).replace("'", "")

                    # Almacena el mensaje de error en el archivo 'error.log'
                    errores.write(f'ERROR - Line {linea_archivo}: {e}\n')

                # Otro tipo de exceptiones
                except Exception as e:
                
                    # Almacena el mensaje de error en el archivo 'error.log'
                    errores.write(f'ERROR - Line {linea_archivo}: {e}\n')

                # Incrementa la variable que lleva la cuenta de las líneas de 'usuario.txt'
                linea_archivo += 1

                # Lee la siguiente línea del archivo
                linea = usuarios.readline()

    # Si no se encuentra el archivo 'usuarios.txt' maneja la excepción
    except FileNotFoundError as e:

        # Se escribe el error en el archivo 'error.log'
        errores.write(f'ERROR - File not found\n')


# Cuando el archivo 'script.py' se ejecuta como programa principal
if __name__ == "__main__":
    
    # Muestra el contenido del archivo 'usuarios.txt' tal como viene
    with open('usuarios.txt', 'r') as usuarios:
        print(f'\n{usuarios.read()}')

    print()

    # Itera la lista de usuarios generada después de filtrarla
    for user in lista_usuarios:

        # Imprime sus atributos en forma de diccionarios
        print(user.obtener_atributos)

    # Muestra el contenido del archivo 'error.log'
    with open('error.log', 'r') as errores:
        print(f'\n{errores.read()}')
   