#Calculadora para converter de binário para decimal
import tkinter as tk
from tkinter import messagebox

class calculadora:
    #Inicia a função
    def __init__(self, root):
        self.root = root    #inicializa a janela principal
        self.root.title("Calculadora Básica")
        
        # Variável para armazenar o valor atual
        self.current_value = tk.StringVar()
        
        # Entry para mostrar os valores
        self.display = tk.Entry(root, textvariable=self.current_value, justify="right", font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)
        
        # Botões da calculadora
        button_dec_to_binary =  tk.Button(root, text="Decimal to Binary", padx=10, pady=10, font=('Arial', 12), command=self.convert_dec_to_bin)
        button_binary_to_dec = tk.Button(root, text="Binary to Decimal", padx=10, pady=10, font=('Arial', 12), command=self.convert_bin_to_dec)
        button_dec_to_oct = tk.Button(root, text="Decimal to Octal", padx=10, pady=10, font=('Arial', 12), command=self.convert_dec_to_oct)
        button_oct_to_dec = tk.Button(root, text="Octal to Decimal", padx=10, pady=10, font=('Arial', 12), command=self.convert_oct_to_dec) 
        button_dec_to_hex = tk.Button(root, text="Decimal to Hexadecimal", padx=10, pady=10, font=('Arial', 12), command=self.convert_dec_to_hex)
        button_hex_to_dec = tk.Button(root, text="Hexadecimal to Decimal", padx=10, pady=10, font=('Arial', 12), command=self.convert_hex_to_dec)   
        button_clear = tk.Button(root, text="Clear", padx=10, pady=10, font=('Arial', 12), command=self.clear_display)
        button_exit = tk.Button(root, text="Exit", padx=10, pady=10, font=('Arial', 12), command=self.root.quit)
        
        buttons = [
            button_dec_to_binary, button_binary_to_dec, 
            button_dec_to_oct, button_oct_to_dec, button_dec_to_hex, 
            button_hex_to_dec, button_clear, button_exit ]
        
        row = 1
        col = 0
        
        for button in buttons:
            self.create_button(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1
    def create_button(self, button, row, col):
        button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5) 
    def button_click(self, text):
        current = self.current_value.get()
        new_value = current + str(text)
        self.current_value.set(new_value)   
    def clear_display(self):
        self.current_value.set("")
    def convert_dec_to_bin(self):
        try:
            dec = int(self.current_value.get())
            if dec < 0:
                messagebox.showerror("Erro", "Por favor, insira um número decimal não negativo.")
                return
            binary = bin(dec)[2:]  # Converte para binário e remove o prefixo '0b'
            self.current_value.set(binary)
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida. Por favor, insira um número decimal válido.") 
    def convert_bin_to_dec(self):
        try:
            binary = self.current_value.get()
            if not all(bit in '01' for bit in binary):
                messagebox.showerror("Erro", "Por favor, insira um número binário válido.")
                return
            decimal = int(binary, 2)  # Converte de binário para decimal
            self.current_value.set(str(decimal))
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida. Por favor, insira um número binário válido.")
    def convert_dec_to_oct(self):
        try:
            dec = int(self.current_value.get())
            if dec < 0:
                messagebox.showerror("Erro", "Por favor, insira um número decimal não negativo.")
                return
            octal = oct(dec)[2:]  # Converte para octal e remove o prefixo '0o'
            self.current_value.set(octal)
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida. Por favor, insira um número decimal válido.")
    def convert_oct_to_dec(self):
        try:
            octal = self.current_value.get()
            if not all(digit in '01234567' for digit in octal):
                messagebox.showerror("Erro", "Por favor, insira um número octal válido.")
                return
            decimal = int(octal, 8)  # Converte de octal para decimal
            self.current_value.set(str(decimal))
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida. Por favor, insira um número octal válido.")
    def convert_dec_to_hex(self):
        try:
            dec = int(self.current_value.get())
            if dec < 0:
                messagebox.showerror("Erro", "Por favor, insira um número decimal não negativo.")
                return
            hexadecimal = hex(dec)[2:].upper()  # Converte para hexadecimal e remove o prefixo '0x'
            self.current_value.set(hexadecimal)
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida. Por favor, insira um número decimal válido.")
    def convert_hex_to_dec(self):
        try:
            hexadecimal = self.current_value.get()
            if not all(char in '0123456789ABCDEF' for char in hexadecimal.upper()):
                messagebox.showerror("Erro", "Por favor, insira um número hexadecimal válido.")
                return
            decimal = int(hexadecimal, 16)  # Converte de hexadecimal para decimal
            self.current_value.set(str(decimal))
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida. Por favor, insira um número hexadecimal válido.")

