from random import randint
import time

lista = [x for x in range(0, 1000001)]
lista_tuple = []
def for_loop(lista):
    start = time.time()
    for i in lista:
        if i % 2 == 0:
            lista_tuple.append((i, i^2))
    end = time.time()
    sorted_lista = (sorted(lista_tuple, key= lambda x:x[1]))
    return [end - start, sorted_lista]
def list_com(lista):
    start = time.time()
    lista_tuple_comprehention = [(i, i^2) for i in lista if i % 2 == 0]
    end = time.time()
    sorted_lista = (sorted(lista_tuple_comprehention, key=lambda x: x[1]))
    return [end - start, sorted_lista]

# def sort_fukncji(lista):
#     print(sorted(lista_tuple, key= lambda x:x[1]))

if __name__ == '__main__':
    print(f'Czas dla for loop: {for_loop(lista)[0]}')
    print(f'Czas dla list_com: {list_com(lista)[0]}')
    #print(sort_fukncji(lista_tuple))





