class pilaAutomata:
    def __init__(self):
        self.pila = []
    
    def Agregar(self, valor):
        self.pila.append(valor)

    def eliminar(self):
        if len(self.pila) == 0:
            return None
        else:
            return self.pila.pop()
    
    def cabeceraPila(self):
        if len(self.pila) == 0:
            print('Borrado')
            return None
        else:
            return self.pila[-1]
    
    def longitudPila(self):
        return len(self.pila)==0
    
    def MostrarPila(self):
        print("PILA: ", self.pila)
        return self.pila

    def proceso(self, cadena):
        self.MostrarPila()
        self.Agregar(cadena)
        self.MostrarPila()
        return self.eliminar()
    
    def error(self, cadena):
        self.Agregar(cadena)
        self.MostrarPila()

    def limpiarPila(self):
        for x in range(len(self.pila)):
            self.eliminar()
