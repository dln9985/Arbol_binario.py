class nodo():
    def __init__(self, valor):
        self.valor = valor
        self.left = None 
        self.right = None
        pass
    
    def __str__(self):
        return f"Valor: {self.valor}, Izq: {self.left}, Der: {self.right}"
    
    
    pass