import tkinter as tk
from Calculadora import calculadora

 # Função principal
def main():
    root = tk.Tk()
    calculator = calculadora(root)
    
    # Configurar o grid para expandir corretamente
    for i in range(4):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)
    
    root.mainloop()

if __name__ == "__main__":
    main()