import os
import sys

def delete_friend(name_to_delete):
    """
    Elimina un contacto del archivo friendsContact.txt basándose en el nombre.
    Si el nombre no se encuentra, no se realiza ninguna eliminación.
    """
    file_name = "friendsContact.txt"
    deleted = False
    lines_to_keep = []

    try:
        # Comprueba si el archivo existe. Si no, no hay nada que eliminar.
        if not os.path.exists(file_name):
            print(f"El archivo '{file_name}' no existe. No hay contactos para eliminar.")
            return

        # Lee todas las líneas del archivo original.
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Procesa cada línea para encontrar y omitir el contacto a eliminar.
        for line in lines:
            original_line = line.strip()
            parts = original_line.split('!')
            if len(parts) == 2:
                name = parts[0]
                if name == name_to_delete:
                    # Si el nombre coincide, no añade esta línea a lines_to_keep.
                    deleted = True
                else:
                    # Si no coincide, añade la línea a la lista para mantener.
                    lines_to_keep.append(original_line + "\n")
            else:
                # Si el formato es incorrecto, añade la línea original tal cual.
                lines_to_keep.append(original_line + "\n")

        if deleted:
            # Escribe las líneas que se deben mantener de vuelta al archivo original.
            with open(file_name, 'w', encoding='utf-8') as file:
                file.writelines(lines_to_keep)
            print("Amigo eliminado.")
        else:
            print(f"El nombre de entrada '{name_to_delete}' no existe.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    # Comprueba si se proporcionaron los argumentos correctos.
    if len(sys.argv) != 2:
        print("Uso: python delete_friend.py <nombre_a_eliminar>")
        sys.exit(1)

    # Obtiene el nombre a eliminar de los argumentos de la línea de comandos.
    name_to_delete_arg = sys.argv[1]
    delete_friend(name_to_delete_arg)