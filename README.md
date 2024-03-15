# Descripción del Proyecto

Este proyecto consiste en un script de Python que lee datos de usuarios desde un archivo de texto en formato JSON, instancia objetos de la clase Usuario con estos datos, y los almacena en una lista. Además, el script maneja diferentes tipos de errores y los registra en un archivo de registro.

## Características

- **Lectura de Datos:** El script lee datos de usuarios desde un archivo de texto en formato JSON.
- **Creación de Instancias:** Cada conjunto de datos de usuario se utiliza para crear una instancia de la clase Usuario.
- **Manejo de Errores:** Se manejan distintos tipos de errores durante el proceso de lectura y creación de instancias, y se registran en un archivo de registro.
- **Visualización de Datos:** Se muestran los datos de usuarios almacenados y los errores registrados.

## Requisitos

- Python 3.x
- Archivo de texto en formato JSON con datos de usuarios (usuarios.txt)

## Uso

1. Asegúrate de tener instalado Python en tu sistema.
2. Coloca el archivo de texto con los datos de usuarios (usuarios.txt) en el mismo directorio que el script.
3. Ejecuta el script utilizando el comando `python script.py`.
4. Observa la salida en la consola, que mostrará los datos de usuarios y los errores registrados.

## Estructura del Proyecto

- **script.py:** Contiene el código del script principal.
- **usuario.py:** Define la clase Usuario utilizada en el script principal.
- **usuarios.txt:** Archivo de texto en formato JSON con los datos de usuarios.
- **error.log:** Archivo de registro que almacena los errores encontrados durante la ejecución del script.

## Autor

Jose Contreras Stoltze
