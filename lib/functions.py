from .classes import *

def linkHijo( nodoPadre, nodoHijoIz= None , nodoHIjoDer= None ):
    if nodoHijoIz is not None:
        nodoPadre.left = nodoHijoIz
    if nodoHIjoDer is not None:
        nodoPadre.right = nodoHIjoDer
    pass

def LVR( Nodo, inOrderArr ):
    if Nodo is not None:
        nodoPadre = Nodo
        
        LVR ( nodoPadre.left, inOrderArr )

        inOrderArr.append(nodoPadre.valor)

        LVR ( nodoPadre.right, inOrderArr )
        
    return inOrderArr

def VLR( Nodo, PreOrderArr ):
    if Nodo is not None:
        nodoPadre = Nodo
        
        PreOrderArr.append(nodoPadre.valor)
        
        VLR ( nodoPadre.left, PreOrderArr )

        VLR ( nodoPadre.right, PreOrderArr )
        
    return PreOrderArr

def LRV( Nodo, PostOrderArr ):
    if Nodo is not None:
        nodoPadre = Nodo
        
        LRV ( nodoPadre.left, PostOrderArr )

        LRV ( nodoPadre.right, PostOrderArr )
        
        PostOrderArr.append(nodoPadre.valor)
        
    return PostOrderArr

def NodosOrdenados(nodoFather, newNodo):
    if newNodo.valor < nodoFather.valor:
        if nodoFather.left is None:
            nodoFather.left = newNodo
        else:
            NodosOrdenados(nodoFather.left, newNodo)
        
    if newNodo.valor > nodoFather.valor:
        if nodoFather.right is None:
            nodoFather.right = newNodo
        else:
            NodosOrdenados(nodoFather.right, newNodo)  
    pass

def printThree( Nodo ):
    if Nodo is not None:
        nodoPadre = Nodo
        
        print(nodoPadre.getThree())
        
        printThree( nodoPadre.left)
        
        printThree( nodoPadre.right)
        
def agregaNodos(currentNodo, nuevoNum):
    cola=[]
    cola.append(currentNodo)
    
    while cola:
        currentNodo = cola.pop(0)
        
        if currentNodo.left is None:
           currentNodo.left = nodo( nuevoNum )
           return 0

        if currentNodo.right is None:
           currentNodo.right = nodo( nuevoNum )
           return 0
    
        cola.append(currentNodo.left)
        cola.append(currentNodo.right)
        
    return 0


         