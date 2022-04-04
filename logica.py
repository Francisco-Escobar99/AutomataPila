import re
from PilaAutomata import pilaAutomata

pila = pilaAutomata()
result = pilaAutomata()
grama = ['NombreLista','.','Metodos']
list_Metodos = ['append','extend','remove','index','count','reverse','pop','clear','sort','copy','insert']
PALABRAS = '^[A-Z|a-z]+$'
GRAMATICA2 = '^[0-9]+$|^[A-Z|a-z]{1}$|^[\"A-Z|a-z\"]+$|^[A-Z|a-z]+$'
GRAMATICA3 = '^[0-9]+$|^[A-Z|a-z]+$|^[\"A-Z|a-z\"]+$'
GRAMATICA4 = '^[0-9]+$'

class Logica:
    def PrimerEstado(self, gramatica, posicion):
        print('-------- ESTADO Q0 --------')
        pila.limpiarPila()
        pila.Agregar(grama[2])
        pila.Agregar(grama[1])
        pila.Agregar(grama[0])
        pila.MostrarPila()

        if pila.eliminar() == grama[0]:
            inicio = pila.proceso(PALABRAS)
            inicio2 = re.search(inicio, gramatica[0])
            print('Estado Q0: ', inicio2)

            if inicio2 is None:
                print('Entro a Error')
                pila.error(inicio)
                self.segundoEstado(gramatica,posicion)
            else:
                posicion -= 2
                pila.MostrarPila()
                self.segundoEstado(gramatica,posicion)
        else:
            pila.Agregar('null')
    
    def segundoEstado(self, gramatica, posicion):

        print('-------- ESTADO Q1 --------')
        if pila.eliminar() == grama[1]:
            segundo = pila.proceso('.')
            if segundo == gramatica[1]:
                posicion -= 2
                pila.MostrarPila()
                self.tercerEstado(gramatica, posicion)
            else:
                print('Entro a Error')
                pila.error(segundo)
                self.tercerEstado(gramatica, posicion)
        else:
            pila.Agregar('null')      
    
    def tercerEstado(self, gramatica, posicion):
        print('-------- ESTADO Q2 --------')
        pila.MostrarPila()
        subcadena = gramatica[2].split('(')
        subcadena.insert(1,'('+subcadena[1])
        subcadena.pop(2)
        valor = str(subcadena[1]).replace('(','').replace(')','')
        subcadena2 = ['(',valor,')']

        if pila.eliminar() == grama[2]:
            if subcadena[0] == list_Metodos[0]:
                pila.error(list_Metodos[0] + '(' + GRAMATICA2 + ')')
                decision = re.search(GRAMATICA2,subcadena2[1])
                print(decision)
                if  decision is None:
                    pila.error('-')
                    print('Valor Incorrecto: ', valor)
                else:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)

            elif subcadena[0] == list_Metodos[1]:
                pila.error(list_Metodos[1] + '(' + PALABRAS + ')')
                decision = re.search(PALABRAS,subcadena2[1])
                print(decision)
                if  decision is None:
                    pila.error('-')
                    print('Valor Incorrecto: ', valor)
                else:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)

            elif subcadena[0] == list_Metodos[2]:
                pila.error(list_Metodos[2] + '(' + GRAMATICA3 + ')')
                decision = re.search(GRAMATICA3,subcadena2[1])
                print(decision)
                if  decision is None:
                    pila.error('-')
                    print('Valor Incorrecto: ', valor)
                else:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)
            
            elif subcadena[0] == list_Metodos[3]:
                pila.error(list_Metodos[3] + '(' + GRAMATICA3 + ')')
                decision = re.search(GRAMATICA3,subcadena2[1])
                print(decision)
                if  decision is None:
                    pila.error('-')
                    print('Valor Incorrecto: ', valor)
                else:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)
            
            elif subcadena[0] == list_Metodos[4]:
                pila.error(list_Metodos[4] + '(' + GRAMATICA3 + ')')
                decision = re.search(GRAMATICA3,subcadena2[1])
                print(decision)
                if  decision is None:
                    pila.error('-')
                    print('Valor Incorrecto: ', valor)
                else:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)

            elif subcadena[0] == list_Metodos[5]:
                pila.error(list_Metodos[5] + '(' ')' )
                decision = re.search(PALABRAS,subcadena2[1])
                print(decision)
                if  decision is None:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)
                else:
                    pila.error('-')
                    print('Valor Incorrecto: ', valor)

            elif subcadena[0] == list_Metodos[6]:
                pila.error(list_Metodos[6] + '(' ')')
                decision = re.search(GRAMATICA4,subcadena2[1])
                print(decision)
                if  decision is None:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)
                else:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)
            
            elif subcadena[0] == list_Metodos[7]:
                pila.error(list_Metodos[7] + '(' ')')
                decision = re.search(PALABRAS,subcadena2[1])
                print(decision)
                if  decision is None:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)
                else:
                    pila.error('-')
                    print('Valor Incorrecto: ', valor)

            elif subcadena[0] == list_Metodos[8]:
                pila.error(list_Metodos[8] + '(' ')' )
                decision = re.search(PALABRAS,subcadena2[1])
                print(decision)
                if  decision is None:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)
                else:
                    pila.error('-')
                    print('Valor Incorrecto: ', valor)
            
            elif subcadena[0] == list_Metodos[9]:
                pila.error(list_Metodos[9] + '(' ')' )
                decision = re.search(PALABRAS,subcadena2[1])
                print(decision)
                if  decision is None:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)
                else:
                    pila.error('-')
                    print('Valor Incorrecto: ', valor)

            elif subcadena[0] == list_Metodos[10]:
                pila.error(list_Metodos[10] + '(' + GRAMATICA4 + ')')
                decision = re.search(GRAMATICA3,subcadena2[1])
                print(decision)
                if  decision is None:
                    pila.error('-')
                    print('Valor Incorrecto: ', valor)
                else:
                    posicion = 0
                    pila.eliminar()
                    pila.MostrarPila()
                    self.final(posicion)
        else:
            pila.Agregar('NULL')

    def final(self, posicion):
        if pila.longitudPila():
            if posicion == 0:
                estado = 'cumple'
                result.Agregar('Cumple')
                return estado
            else:
                estado = 'vacio'
                result.Agregar('Vacio')
                return estado
        else:
            estado = 'vacio'
            result.Agregar('Vacio')
            return estado

    def respuesta(self):
        pila.longitudPila()
        return result
                



