#Inicio class nodo ----------------------------------------
class nodo():
    def __init__(self, valor):
        self.valor = valor
        self.left = None 
        self.right = None
        pass
    
    def getThree(self):
        strout = ""
        strout += f" NP[{self.valor}] "
        if type(self.left) != type(None):
            strout += f" [{self.valor}]->[{self.left}] "
        if self.right is not None:
            strout += f" [{self.valor}]->[{self.right}] "
    
    def __str__(self): 
        return f"Valor: {self.valor}"
    
    pass
#Fin class nodo -------------------------------------------