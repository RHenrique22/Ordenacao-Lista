import random 
import time

def BubbleSort (lista):

  tam = len(lista)

  for i in range(tam - 1):
    for j in range(0, tam - i - 1):
      if lista[j] > lista[j + 1] :
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
  
  print(lista)
  print()

def InsertionSort (lista):

  tam = len(lista)

  for i in range (1, tam):
    key = lista[i]
    j = i - 1
    while j >= 0 and key < lista[j] :
      lista[j + 1] = lista[j]
      j -= 1
    
    lista[j + 1] = key

  print(lista)
  print()

def ShellSort (lista):

  tam = len(lista)
  gap = tam // 2

  while gap > 0:
    for i in range(gap, tam):
      temp = lista[i]
      j = i

      while  j >= gap and lista[j - gap] > temp:
        lista[j] = lista[j - gap]
        j -= gap

      lista[j] = temp

    gap //= 2
  
  print(lista)
  print()

def MergeSort (lista):
  if len(lista) > 1:
    mid = len(lista) // 2

    L = lista[:mid]

    R = lista[mid:]

    MergeSort(L)

    MergeSort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        lista[k] = L[i]
        i += 1
      else:
        lista[k] = R[j]
        j += 1
      k += 1

    while i < len(L):
      lista[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      lista[k] = R[j]
      j += 1
      k += 1


def partition(lista, low, high):
  i = (low - 1)         
  pivot = lista[high]     

  for j in range(low, high):
    if lista[j] <= pivot:
      i = i + 1
      lista[i], lista[j] = lista[j], lista[i]

  lista[i + 1], lista[high] = lista[high], lista[i + 1]
  return (i + 1)

def QuickSort (lista, low, high):
  if (len(lista) == 1):
    return lista
  if (low < high):
    pi = partition(lista, low, high)
    QuickSort(lista, low, pi - 1)
    QuickSort(lista, pi + 1, high)

lista = []

for i in range(20000):
  lista.append(random.randint(1, 5000))
  
def imprimeMenu():
  print(f'''
                OPÇÕES DE ORDENAÇÃO!

      |  [1]          BubbleSort            |
      |  [2]         InsertionSort          |
      |  [3]          ShellSort             |
      |  [4]          MergeSort             |
      |  [5]          QuickSort             |
      |  [6]             Sair               |\n''')

imprimeMenu()
interacao = int(input("Digite qual opção você deseja acessar: "))

while True:
  if (interacao == 1):
    listafake = lista.copy()
    print(f"\n{lista}\n")
    inicio = time.time()
    BubbleSort(listafake)
    fim = time.time()
    total = (fim - inicio)
    print(f"Tempo levado com o BubbleSort {total}s")
    acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

    if (acessarMenu == 1):
      imprimeMenu()
      interacao = int(input("Digite qual opção você deseja acessar: "))
    else:
      interacao = int(input("Digite qual opção você deseja acessar: "))
  
  elif (interacao == 2):
    listafake = lista.copy()
    print(f"\n{lista}\n")
    inicio = time.time()
    InsertionSort(listafake)
    fim = time.time()
    total = (fim - inicio)
    print(f" Tempo levado com o InsertionSort {total}s")
    acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

    if (acessarMenu == 1):
      imprimeMenu()
      interacao = int(input("Digite qual opção você deseja acessar: "))
    else:
      interacao = int(input("Digite qual opção você deseja acessar: "))
  
  elif (interacao == 3):
    listafake = lista.copy()
    print(f"\n{lista}\n")
    inicio = time.time()
    ShellSort(listafake)
    fim = time.time()
    total = (fim - inicio)
    print(f"Tempo levado com o ShellSort {total}s")
    acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

    if (acessarMenu == 1):
      imprimeMenu()
      interacao = int(input("Digite qual opção você deseja acessar: "))
    else:
      interacao = int(input("Digite qual opção você deseja acessar: "))
  
  elif (interacao == 4):
    listafake = lista.copy()
    print(f"\n{lista}\n")
    inicio = time.time()
    MergeSort(listafake)
    fim = time.time()
    print()
    print(f"{listafake}")
    print()
    total = (fim - inicio)
    print(f"Tempo levado com o MergeSort {total}s")
    acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

    if (acessarMenu == 1):
      imprimeMenu()
      interacao = int(input("Digite qual opção você deseja acessar: "))
    else:
      interacao = int(input("Digite qual opção você deseja acessar: "))
  
  elif (interacao == 5):
    listafake = lista.copy()
    print(f"\n{lista}\n")
    inicio = time.time()
    QuickSort(listafake, 0, len(listafake) - 1)
    fim = time.time()
    print()
    print(f"{listafake}")
    print()
    total = (fim - inicio)
    print(f"Tempo levado com o QuickSort {total}s")
    acessarMenu = int(input('\nDeseja voltar ao menu (1-SIM ou 2-NÃO): '))

    if (acessarMenu == 1):
      imprimeMenu()
      interacao = int(input("Digite qual opção você deseja acessar: "))
    else:
      interacao = int(input("Digite qual opção você deseja acessar: "))
  
  else:
    break