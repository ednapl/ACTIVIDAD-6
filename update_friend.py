import os
import sys

def update_friend(name_to_update, new_number):
    """
    Actualiza el número de un contacto existente en el archivo friendsContact.txt.
    Si el nombre no se encuentra, no se realiza ninguna actualización.
    """
    file_name = "friendsContact.txt"
    temp_file_name = "temp.txt"
    updated = False
    lines_to_write = []

    try:
        # Comprueba si el archivo existe. Si no, no hay nada que actualizar.
        if not os.path.exists(file_name):
            print(f"El archivo '{file_name}' no existe. No hay contactos para actualizar.")
            return

        # Lee todas las líneas del archivo original.
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Procesa cada línea para encontrar y actualizar el contacto.
        for line in lines:
            original_line = line.strip()
            parts = original_line.split('!')
            if len(parts) == 2:
                name = parts[0]
                # No necesitamos el número antiguo para la comparación, solo el nombre.
                # number = int(parts[1])

                if name == name_to_update:
                    # Si el nombre coincide, actualiza la línea con el nuevo número.
                    lines_to_write.append(f"{name_to_update}!{new_number}\n")
                    updated = True
                else:
                    # Si no coincide, añade la línea original.
                    lines_to_write.append(original_line + "\n")
            else:
                # Si el formato es incorrecto, añade la línea original tal cual.
                lines_to_write.append(original_line + "\n")

        if updated:
            # Escribe las líneas actualizadas de vuelta al archivo original.
            with open(file_name, 'w', encoding='utf-8') as file:
                file.writelines(lines_to_write)
            print("Amigo actualizado.")
        else:
            print(f"El nombre de entrada '{name_to_update}' no existe.")

    except ValueError:
        print("Error: El nuevo número de contacto debe ser un número válido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    # Comprueba si se proporcionaron los argumentos correctos.
    if len(sys.argv) != 3:
        print("Uso: python update_friend.py <nombre_a_actualizar> <nuevo_numero>")
        sys.exit(1)

    # Obtiene el nombre y el nuevo número de los argumentos de la línea de comandos.
    name_to_update_arg = sys.argv[1]
    try:
        new_number_arg = int(sys.argv[2])
    except ValueError:
        print("Error: El nuevo número de contacto debe ser un número entero válido.")
        sys.exit(1)

    update_friend(name_to_update_arg, new_number_arg)