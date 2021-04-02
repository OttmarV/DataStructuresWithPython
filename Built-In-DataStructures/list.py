"""
Mutable
Indexing
Not homogeneous
Allows duplicates
"""


hello=[1,20,0.5,10]

# Adding Elements(append,insert,extend)
# Deleting Elements(remove,pop,clear)
# Other Functions(index,count,sort)

print(hello.index(10))
hello.append([10,29]) #agrega como tal la lista proporcionada
print(hello)
hello.insert(0 , 30) #inserta el valor en el indice que le pasemos
print(hello)
hello.extend([91,22]) #agrega cada elemento proporcionado
print(hello)
hello.extend(["hello"]) #agrega cada elemento proporcionado
print(hello)
hello.pop() #elimina el ultimo valor
print(hello)
hello.remove([10,29]) #quita eleemento de la lista
print(hello)
#hello.clear()
#print(hello)
hello.sort() #ordena elementos
print(hello)
print(hello.count(20)) #cuenta las veces que aparece el elemento en la lista



