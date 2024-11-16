import time
import tracemalloc


# Funções de ordenação
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Função para medir tempo e memória
def measure_sorting_time(sort_func, arr):
    start_time = time.perf_counter()
    tracemalloc.start()
    sort_func(arr.copy())
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()
    return end_time - start_time, peak


# Leitura e ordenação
def main():
    # Ler a listagem do arquivo de texto
    with open('listagem.txt', 'r') as file:
        file_list = file.read().splitlines()

    # Medir tempo e memória para cada algoritmo de ordenação
    for sort_func in [bubble_sort, selection_sort, insertion_sort]:
        time_taken, memory_used = measure_sorting_time(sort_func, file_list)
        print(f"{sort_func.__name__} - Tempo: {time_taken:.4f}s, Memória: {memory_used / 1024:.2f} KB")


if __name__ == "__main__":
    main()
