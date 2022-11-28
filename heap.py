def min_heapify(heap, heap_size, index):
    left = 2 * index + 1
    right = 2 * index + 2
    minimum_index = index
    if(left < heap_size and heap[minimum_index] > heap[left]) :
        minimum_index = left
    if (right < heap_size and heap[minimum_index] > heap[right]):
        minimum_index = right
    if (minimum_index != index):
        swap(heap, index, minimum_index)
        min_heapify(heap, heap_size, minimum_index)

def build_min_heap(array):
    n = len(array)
    i = n // 2 - 1
    while i >= 0:
        min_heapify(array, n, i)
        i -= 1

def heap_sort(array):
    build_min_heap(array)
    n = len(array)
    i = n - 1
    while i > 0:
        swap(array, 0, i)
        min_heapify(array, i, 0)
        i -= 1
    array.reverse()
    

def swap(heap, i, j):
    temp = heap[j]
    heap[j] = heap[i]
    heap[i] = temp   
