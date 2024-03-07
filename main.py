from lib import *
import sys

print("")

arrayNum=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
nodoRaiz = nodo(arrayNum[0])

for i in range(1, len(arrayNum), 1):
    agregaNodos(nodoRaiz,arrayNum[i])
    
#for i in arrayNum:
    #agregaNodos(nodoRaiz, i)
    
#j=1
#while arrayNum:
    #agregaNodos(nodoRaiz, arrayNum[j])
    #j+=1
    
printThree(nodoRaiz)

inOrderArr = []
PreOrderArr = []
PostOrderArr = []

LVR(nodoRaiz, inOrderArr)
print("In Order:", end=" ")
print(inOrderArr)

VLR(nodoRaiz, PreOrderArr)
print("PreOrder:", end=" ")
print(PreOrderArr)

LRV(nodoRaiz, PostOrderArr)
print("PostOrder:", end=" ")
print(PostOrderArr)

sys.exit("Fin del programa")

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

printThree(nodoraiz)

print("")