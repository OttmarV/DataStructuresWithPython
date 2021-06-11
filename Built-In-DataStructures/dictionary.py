"""
Mutable 
key-value pairs
"""

book={1:'intro',2:'blogs',3:'content',4:'end'}
print(book)
okay = dict([(0,2),(1,3)])
print(okay)

# Other Functions keys(),values(),get(),items()

print(book.keys())
print(book.values())
print(book.items())

#delete element
book.pop(2)
print(book)

#limpiar diccionario
#book.clear()
#print(book)










