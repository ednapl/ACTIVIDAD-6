import os
import sys

def display_friends():
    """
    Lee y muestra todos los contactos del archivo friendsContact.txt.
    """
    file_name = "friendsContact.txt"

    try:
        # Abre el archivo en modo de lectura.
        # Si el archivo no existe, se crea uno vacío (como en Java).
        if not os.path.exists(file_name):
            open(file_name, 'w', encoding='utf-8').close() # Crea el archivo vacío
            print(f"El archivo '{file_name}' no existía y ha sido creado.")
            return # No hay contactos que mostrar si el archivo acaba de ser creado.

        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                print("El archivo de contactos está vacío.")
                return

            print("--- Lista de Amigos ---")
            for line in lines:
                # Elimina espacios en blanco al principio/final y divide la línea
                # por el delimitador '!' para obtener el nombre y el número.
                parts = line.strip().split('!')
                if len(parts) == 2:
                    name = parts[0]
                    number = int(parts[1]) # Convierte el número a entero.
                    print(f"Nombre del amigo: {name}")
                    print(f"Número de contacto: {number}\n")
                else:
                    print(f"Advertencia: Línea con formato incorrecto ignorada: {line.strip()}")
            print("--- Fin de la Lista ---")

    except FileNotFoundError:
        # Esto no debería ocurrir con la comprobación os.path.exists, pero es una buena práctica.
        print(f"Error: El archivo '{file_name}' no se encontró.")
    except ValueError:
        print("Error: Se encontró un número de contacto no válido en el archivo.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    display_friends()