import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

# Define the file name for contacts
FILE_NAME = "friendsContact.txt"

def create_file_if_not_exists():
    """Ensures the contact file exists."""
    if not os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'w', encoding='utf-8') as f:
                pass  # Create an empty file
        except IOError as e:
            messagebox.showerror("Error de archivo", f"No se pudo crear el archivo de contactos: {e}")

def add_friend_logic(name_to_add, number_to_add):
    """
    Adds a new contact (name and number) to the friendsContact.txt file.
    If the name or number already exists, the contact is not added.
    """
    create_file_if_not_exists()
    contacts = []
    found = False

    try:
        with open(FILE_NAME, 'r+', encoding='utf-8') as file:
            # Read existing contacts
            for line in file:
                parts = line.strip().split('!')
                if len(parts) == 2:
                    name = parts[0]
                    try:
                        number = int(parts[1])
                    except ValueError:
                        # Skip malformed lines
                        continue
                    contacts.append((name, number))

                    if name == name_to_add or number == number_to_add:
                        found = True
                        break

            if not found:
                # If not found, append the new contact
                file.write(f"{name_to_add}!{number_to_add}\n")
                return "Amigo añadido exitosamente."
            else:
                return "El nombre o número de entrada ya existe."

    except ValueError:
        return "Error: El número de contacto debe ser un número válido."
    except Exception as e:
        return f"Ocurrió un error: {e}"

def display_friends_logic():
    """
    Reads and returns all contacts from the friendsContact.txt file as a string.
    """
    create_file_if_not_exists()
    output = []
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                return "El archivo de contactos está vacío."

            output.append("--- Lista de Amigos ---\n")
            for line in lines:
                parts = line.strip().split('!')
                if len(parts) == 2:
                    name = parts[0]
                    try:
                        number = int(parts[1])
                        output.append(f"Nombre del amigo: {name}\nNúmero de contacto: {number}\n")
                    except ValueError:
                        output.append(f"Advertencia: Línea con formato de número incorrecto ignorada: {line.strip()}\n")
                else:
                    output.append(f"Advertencia: Línea con formato incorrecto ignorada: {line.strip()}\n")
            output.append("--- Fin de la Lista ---")
    except Exception as e:
        return f"Ocurrió un error al leer el archivo: {e}"
    return "".join(output)

def update_friend_logic(name_to_update, new_number):
    """
    Updates the number of an existing contact in the friendsContact.txt file.
    If the name is not found, no update is performed.
    """
    create_file_if_not_exists()
    updated = False
    lines_to_write = []

    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            original_line = line.strip()
            parts = original_line.split('!')
            if len(parts) == 2:
                name = parts[0]
                if name == name_to_update:
                    lines_to_write.append(f"{name_to_update}!{new_number}\n")
                    updated = True
                else:
                    lines_to_write.append(original_line + "\n")
            else:
                lines_to_write.append(original_line + "\n") # Keep malformed lines as is

        if updated:
            with open(FILE_NAME, 'w', encoding='utf-8') as file:
                file.writelines(lines_to_write)
            return "Amigo actualizado exitosamente."
        else:
            return f"El nombre de entrada '{name_to_update}' no existe."

    except ValueError:
        return "Error: El nuevo número de contacto debe ser un número válido."
    except Exception as e:
        return f"Ocurrió un error: {e}"

def delete_friend_logic(name_to_delete):
    """
    Deletes a contact from the friendsContact.txt file based on the name.
    If the name is not found, no deletion is performed.
    """
    create_file_if_not_exists()
    deleted = False
    lines_to_keep = []

    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            original_line = line.strip()
            parts = original_line.split('!')
            if len(parts) == 2:
                name = parts[0]
                if name == name_to_delete:
                    deleted = True
                else:
                    lines_to_keep.append(original_line + "\n")
            else:
                lines_to_keep.append(original_line + "\n") # Keep malformed lines as is

        if deleted:
            with open(FILE_NAME, 'w', encoding='utf-8') as file:
                file.writelines(lines_to_keep)
            return "Amigo eliminado exitosamente."
        else:
            return f"El nombre de entrada '{name_to_delete}' no existe."

    except Exception as e:
        return f"Ocurrió un error: {e}"

class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Gestor de Contactos")
        master.geometry("400x500") # Set initial window size
        master.resizable(False, False) # Make window not resizable

        # Configure grid for better layout control
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=1)
        master.grid_rowconfigure(3, weight=1)
        master.grid_rowconfigure(4, weight=1)
        master.grid_rowconfigure(5, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

        # Nombre input
        self.name_label = tk.Label(master, text="Nombre:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Numero input
        self.number_label = tk.Label(master, text="Numero:")
        self.number_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.number_entry = tk.Entry(master, width=30)
        self.number_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Buttons frame for better alignment
        self.button_frame = tk.Frame(master)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.create_button = tk.Button(self.button_frame, text="Create", command=self.create_contact)
        self.create_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.read_button = tk.Button(self.button_frame, text="Read", command=self.read_contacts)
        self.read_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.update_button = tk.Button(self.button_frame, text="Update", command=self.update_contact)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete", command=self.delete_contact)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Message display area
        self.message_label = tk.Label(master, text="Estado:", anchor="w")
        self.message_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.output_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Initial file creation check
        create_file_if_not_exists()

    def update_output(self, message, is_error=False):
        """Updates the output text area with a message."""
        self.output_text.delete(1.0, tk.END) # Clear previous content
        self.output_text.insert(tk.END, message)
        if is_error:
            self.output_text.tag_configure("error", foreground="red")
            self.output_text.tag_add("error", 1.0, tk.END)
        self.output_text.see(tk.END) # Scroll to the end

    def get_inputs(self):
        """Retrieves and validates name and number from entry fields."""
        name = self.name_entry.get().strip()
        number_str = self.number_entry.get().strip()
        
        if not name:
            self.update_output("Error: El nombre no puede estar vacío.", is_error=True)
            return None, None
        
        if number_str:
            try:
                number = int(number_str)
            except ValueError:
                self.update_output("Error: El número debe ser un valor numérico entero.", is_error=True)
                return name, None # Return name even if number is invalid for some operations
        else:
            number = None # Allow number to be empty for operations like delete/read all

        return name, number

    def create_contact(self):
        name, number = self.get_inputs()
        if name is None or number is None: # Number must be valid for creation
            return
        
        result = add_friend_logic(name, number)
        self.update_output(result)

    def read_contacts(self):
        result = display_friends_logic()
        self.update_output(result)

    def update_contact(self):
        name, number = self.get_inputs()
        if name is None or number is None: # Number must be valid for update
            return
        
        result = update_friend_logic(name, number)
        self.update_output(result)

    def delete_contact(self):
        name, _ = self.get_inputs() # Only need name for deletion
        if name is None:
            return
        
        result = delete_friend_logic(name)
        self.update_output(result)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()