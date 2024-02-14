import os
from colorama import Fore, init

os.system('cls' if os.name == 'nt' else 'clear')
init()

#Colores para Dinujar
fVerde = Fore.GREEN
fAzul = Fore.BLUE 

fila = []

fila.append("item1")
fila.append("item2")
fila.append("item3")
fila.append("item4")

print(f"Fila: {fila}")

clienteAtendido = fila.pop(0)


print(f"Cliente Atendido {clienteAtendido}")

print(f"Cliente Atendido {fila}")
