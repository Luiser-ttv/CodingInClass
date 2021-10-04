import tkinter as tk
from tkinter import ttk
import secrets
import string


class App:

    def __init__(self, master):
        self.master = master
        self.master.title("Random Password Generator")
        self.master.resizable(True, True)

        self.font = ("courier", 11)

        self.create_gui()

    def create_gui(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.grid(row=0, column=0)

        self.long_char = tk.Label(self.main_frame, text="characters: ", font=self.font)
        self.long_char.grid(row=0, column=0)

        self.long_char_entry = ttk.Entry(self.main_frame)
        self.long_char_entry.grid(row=0, column=1, padx=5, pady=2)
        

        self.generate_button = ttk.Button(self.main_frame, text="generate",
                                          command=lambda: self.generate_password())
        self.generate_button.grid(row=3, column=0)

        self.result_label = tk.Label(self.main_frame, text="password: ", font=self.font)
        self.result_label.grid(row=3, column=1)


    

    def generate_password(self):
        try:
            char_threshold = float(self.long_char_entry.get())
            alphabet = string.ascii_letters + string.digits
            password = ''.join(secrets.choice(alphabet) for i in range(char_threshold))  # for a 20-character password
        except Exception as e:
            print(e)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()