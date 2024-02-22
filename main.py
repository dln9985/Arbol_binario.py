from lib import *

print("")

inOrderArr = []
PreOrderArr = []
PostOrderArr = []

nodo1=nodo(1)
nodo2=nodo(2)
nodo3=nodo(3)
nodo4=nodo(4)
nodo5=nodo(5)
nodo6=nodo(6)
nodo7=nodo(7)

linkHijo(nodo1, nodo2, nodo3)
linkHijo(nodo2, nodo4, nodo5)
linkHijo(nodo3, nodo6, nodo7)

LVR(nodo1, inOrderArr)
print("In Order:", end=" ")
print(inOrderArr)

VLR(nodo1, PreOrderArr)
print("PreOrder:", end=" ")
print(PreOrderArr)

LRV(nodo1, PostOrderArr)
print("PostOrder:", end=" ")
print(PostOrderArr)

print("---------------------------------------")
print("") 

arrNodos=[16,5,7,12,9,20,18,3,10,14]
nodoraiz = None

for i in range(0, len(arrNodos), 1):
    if i == 0:
        nodoraiz = nodo(arrNodos[i])
    else:
        NodosOrdenados(nodoraiz, nodo(arrNodos[i]))
    pass

def printThree( Nodo ):
    if Nodo is not None:
        nodoPadre = Nodo
        
        print(nodoPadre.getThree())
        printThree( nodoPadre.left)
        printThree( nodoPadre.right)

printThree(nodoraiz)


print("")