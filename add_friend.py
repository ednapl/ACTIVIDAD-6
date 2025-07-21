import os
import sys

def add_friend(name_to_add, number_to_add):
    """
    Añade un nuevo contacto (nombre y número) al archivo friendsContact.txt.
    Si el nombre o número ya existen, el contacto no se añade.
    """
    file_name = "friendsContact.txt"
    contacts = []
    found = False

    try:
        # Abre el archivo en modo de lectura y escritura.
        # 'a+' permite leer desde el principio y escribir al final.
        with open(file_name, 'a+', encoding='utf-8') as file:
            # Mueve el puntero al principio del archivo para leer.
            file.seek(0)
            lines = file.readlines()

            for line in lines:
                # Elimina espacios en blanco al principio/final y divide la línea
                # por el delimitador '!' para obtener el nombre y el número.
                parts = line.strip().split('!')
                if len(parts) == 2:
                    name = parts[0]
                    number = int(parts[1]) # Convierte el número a entero.
                    contacts.append((name, number))

                    # Comprueba si el nombre o el número ya existen.
                    if name == name_to_add or number == number_to_add:
                        found = True
                        break # Si se encuentra, no es necesario seguir buscando.

            if not found:
                # Si el contacto no se encontró, lo añade al final del archivo.
                # Se mueve el puntero al final para asegurar la escritura.
                file.seek(0, os.SEEK_END)
                file.write(f"{name_to_add}!{number_to_add}\n")
                print("Amigo añadido.")
            else:
                print("El nombre o número de entrada ya existe.")

    except FileNotFoundError:
        # Esto no debería ocurrir con 'a+', ya que crea el archivo si no existe,
        # pero se mantiene por si acaso se cambia el modo de apertura.
        print(f"El archivo '{file_name}' no se encontró.")
    except ValueError:
        print("Error: El número de contacto debe ser un número válido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    # Comprueba si se proporcionaron los argumentos correctos.
    if len(sys.argv) != 3:
        print("Uso: python add_friend.py <nombre> <numero>")
        sys.exit(1)

    # Obtiene el nombre y el número de los argumentos de la línea de comandos.
    new_name_arg = sys.argv[1]
    try:
        new_number_arg = int(sys.argv[2])
    except ValueError:
        print("Error: El número de contacto debe ser un número entero válido.")
        sys.exit(1)

    add_friend(new_name_arg, new_number_arg)
