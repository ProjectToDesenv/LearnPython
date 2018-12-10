lista = [2,4,5,6,8,9,10]
print(len(lista))

print(lista)

# Lista é mutável diferente de String
lista02 = [2,5,9,15,78,100]
cont = 0
while cont < len(lista):
    print(lista[cont],end= ' ')
    cont += 1


lista03 = [0,2,3,7,8,9]
print(lista[-3:])    

lista04 = [1,2,3,4,5,6]
lista05 = lista04
lista05[0] = 10
print(lista04)
# Em python tudo é objeto

# Uma nova cópia da lista
lista05 = lista04[:]
lista05[0] = 10
print(lista04)

lista.append('Marcelo')
print(lista)

# pop --> Remove pela posição
# remove --> remove pelo elemento
