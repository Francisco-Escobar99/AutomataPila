import tkinter as tk
from tkinter import messagebox as ms
from logica import Logica

automata = Logica()

class interfaz:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Lenguajes & Automatas")
        self.ventana.geometry("1000x600")
        self.ventana.config(background="#D5E6DD")
        
        self.labelTitulo=tk.Label(self.ventana, text="Verificacion de un Metodo lista", width=68, height=2, background="#2A5F61" ,foreground="#FCF9F9", font=("Tahoma", 22,)).place(x=0,y=45)
        imagen=tk.PhotoImage(file="Logo.png")
        etiqueta=tk.Label(image=imagen, background="#2A5F61")
        etiqueta.place(x=76, y=45, width=158, height=75)

        self.labelSubTitulo=tk.Label(self.ventana, text="Metodo a evaluar:", background="#D5E6DD", foreground="#365548", font=("Arial", 18)).place(x=150,y=200)
        self.CajaTexto=tk.Entry(self.ventana, highlightbackground="#2A5F61",highlightthickness = 1, bd=0, font=("Arial", 13))
        self.CajaTexto.place(x=374,y=201,width=315, height=36)
        self.btn=tk.Button(self.ventana, text="Verificar", command=lambda:self.validacion(self.CajaTexto.get()) ,background="#2A5F61", foreground="#FCF9F9", font=("Arial", 14))
        self.btn.place(x=710,y=201, width=150, height=35)

        
        self.labelTitulo2=tk.Label(self.ventana, text="Resultado", width=64, height=1,  background="#2A5F61", foreground="#FCF9F9", font=("Arial", 15,)).place(x=208,y=300, width=600)
        self.cuadro=tk.Label(self.ventana, background="#9AA8A8", highlightbackground="#2A5F61",highlightthickness =1, bd=0)
        self.cuadro.place(x=208,y=329, width=600, height=160)

       
        self.btnUdate=tk.Button(self.ventana, text="Limpiar",background="#2A5F61", foreground="#FCF9F9", font=("Arial", 14))
        self.btnUdate.place(x=298,y=520, width=180, height=30)

        self.btnMetodos=tk.Button(self.ventana, text="Metodos Existentes",background="#2A5F61", foreground="#FCF9F9", font=("Arial", 14), command= lambda:self.NuevaVentana())
        self.btnMetodos.place(x=548,y=520, width=180, height=30)
        self.ventana.mainloop()
        
    def validacion(self, cadena):
        print(cadena)

        if len(cadena) == 0:
            ms.showwarning('Advertencia', 'Campos Vacios')
        else:
            gramaticas = cadena.split(sep='.')
            gramaticas.insert(1,'.')
            posiciones = len(gramaticas)
            print('\n\nEntrada: ', gramaticas)

            automata.PrimerEstado(gramaticas, posiciones)
            resultado = automata.respuesta()

            if resultado.eliminar() == 'Cumple':
                tk.Label(self.ventana, text="Si Cumple", width=64, height=1,  background="#2A5F61", foreground="#FCF9F9", font=("Arial", 15,)).place(x=210,y=300, width=600)
            else:
                tk.Label(self.ventana, text="No Cumple", width=64, height=1,  background="#2A5F61", foreground="#FCF9F9", font=("Arial", 15,)).place(x=210,y=300, width=600)



    def NuevaVentana(self):
        self.ventanaNueva = tk.Tk()
        self.ventanaNueva.title("Metodos Existentes")
        self.ventanaNueva.geometry("650x350")
        self.ventanaNueva.config(background="#D5E6DD")

        self.labelTitulo2=tk.Label(self.ventanaNueva, text="Metodos existentes", width=45, height=1, background="#2A5F61", foreground="#FCF9F9", font=("Tahoma", 22,)).place(x=0,y=25)
        
        self.labelTituloMetodo=tk.Label(self.ventanaNueva, text="Metodos", width=64, height=1,  background="#2A5F61", foreground="#FCF9F9", font=("Arial", 15,)).place(x=133,y=100, width=400)
        self.cuadro2=tk.Label(self.ventanaNueva, background="#9AA8A8", highlightbackground="#2A5F61",highlightthickness =1, bd=0).place(x=133,y=129, width=400, height=180)
        self.labelSubTitulo2=tk.Label(self.ventanaNueva, text="append()", background="#9AA8A8", foreground="#2A5F61", font=("Arial", 14)).place(x=167,y=150)
        self.labelSubTitulo3=tk.Label(self.ventanaNueva, text="insert()", background="#9AA8A8", foreground="#2A5F61", font=("Arial", 14)).place(x=167,y=180)
        self.labelSubTitulo4=tk.Label(self.ventanaNueva, text="index()", background="#9AA8A8", foreground="#2A5F61", font=("Arial", 14)).place(x=167,y=210)
        self.labelSubTitulo2=tk.Label(self.ventanaNueva, text="remove()", background="#9AA8A8", foreground="#2A5F61", font=("Arial", 14)).place(x=167,y=240)
        self.labelSubTitulo3=tk.Label(self.ventanaNueva, text="pop()", background="#9AA8A8", foreground="#2A5F61", font=("Arial", 14)).place(x=293,y=150)
        self.labelSubTitulo4=tk.Label(self.ventanaNueva, text="clear()", background="#9AA8A8", foreground="#2A5F61", font=("Arial", 14)).place(x=293,y=180)
        self.labelSubTitulo2=tk.Label(self.ventanaNueva, text="short()", background="#9AA8A8", foreground="#2A5F61", font=("Arial", 14)).place(x=293,y=210)
        self.labelSubTitulo3=tk.Label(self.ventanaNueva, text="copy()", background="#9AA8A8", foreground="#2A5F61", font=("Arial", 14)).place(x=293,y=240)
        self.labelSubTitulo4=tk.Label(self.ventanaNueva, text="count()", background="#9AA8A8", foreground="#2A5F61", font=("Arial", 14)).place(x=400,y=150)
        self.labelSubTitulo2=tk.Label(self.ventanaNueva, text="reverse()", background="#9AA8A8", foreground="#2A5F61", font=("Arial", 14)).place(x=400,y=180)
        self.labelSubTitulo3=tk.Label(self.ventanaNueva, text="extend()", background="#9AA8A8", foreground="#2A5F61", font=("Arial", 14)).place(x=400,y=210)
        


Principal = interfaz()