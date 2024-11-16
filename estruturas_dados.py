import time
import tracemalloc
from collections import deque
from queue import LifoQueue, Queue


# Função para medir tempo e memória
def measure_operation(func, *args):
    start_time = time.perf_counter()
    tracemalloc.start()
    result = func(*args)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()
    return result, end_time - start_time, peak


# Operações em diferentes estruturas
def retrieve_elements(data_structure):
    positions = [0, 99, 999, 4999, len(data_structure) - 1]
    return [data_structure[i] for i in positions if i < len(data_structure)]


def test_hashtable(data):
    hashtable = {i: data[i] for i in range(len(data))}
    _, time_retrieve, memory_retrieve = measure_operation(retrieve_elements, list(hashtable.values()))
    print(f"Hashtable - Recuperação: Tempo: {time_retrieve:.4f}s, Memória: {memory_retrieve / 1024:.2f} KB")

    _, time_add, memory_add = measure_operation(lambda: hashtable.update({len(hashtable): "novo_arquivo"}))
    _, time_remove, memory_remove = measure_operation(lambda: hashtable.pop(len(hashtable) - 1))
    print(f"Hashtable - Adição: Tempo: {time_add:.4f}s, Memória: {memory_add / 1024:.2f} KB")
    print(f"Hashtable - Remoção: Tempo: {time_remove:.4f}s, Memória: {memory_remove / 1024:.2f} KB")


def test_stack(data):
    stack = LifoQueue()
    for item in data:
        stack.put(item)

    _, time_retrieve, memory_retrieve = measure_operation(retrieve_elements, list(stack.queue))
    print(f"Pilha - Recuperação: Tempo: {time_retrieve:.4f}s, Memória: {memory_retrieve / 1024:.2f} KB")

    _, time_add, memory_add = measure_operation(lambda: stack.put("novo_arquivo"))
    _, time_remove, memory_remove = measure_operation(lambda: stack.get())
    print(f"Pilha - Adição: Tempo: {time_add:.4f}s, Memória: {memory_add / 1024:.2f} KB")
    print(f"Pilha - Remoção: Tempo: {time_remove:.4f}s, Memória: {memory_remove / 1024:.2f} KB")


def test_queue(data):
    queue = Queue()
    for item in data:
        queue.put(item)

    _, time_retrieve, memory_retrieve = measure_operation(retrieve_elements, list(queue.queue))
    print(f"Fila - Recuperação: Tempo: {time_retrieve:.4f}s, Memória: {memory_retrieve / 1024:.2f} KB")

    _, time_add, memory_add = measure_operation(lambda: queue.put("novo_arquivo"))
    _, time_remove, memory_remove = measure_operation(lambda: queue.get())
    print(f"Fila - Adição: Tempo: {time_add:.4f}s, Memória: {memory_add / 1024:.2f} KB")
    print(f"Fila - Remoção: Tempo: {time_remove:.4f}s, Memória: {memory_remove / 1024:.2f} KB")


# Função principal
def main():
    # Ler a listagem do arquivo de texto
    with open('listagem.txt', 'r') as file:
        file_list = file.read().splitlines()

    # Testar cada estrutura de dados
    test_hashtable(file_list)
    test_stack(file_list)
    test_queue(file_list)


if __name__ == "__main__":
    main()

