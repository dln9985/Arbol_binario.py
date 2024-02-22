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