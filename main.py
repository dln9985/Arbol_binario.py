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
print(inOrderArr)

VLR(nodo1, PreOrderArr)
print(PreOrderArr)

LRV(nodo1, PostOrderArr)
print(PostOrderArr)

print("") 

