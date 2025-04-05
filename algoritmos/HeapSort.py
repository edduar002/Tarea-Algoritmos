import heapq

class HeapSort:
    
    def __init__(self):
        pass

    def heap_sort(self, arr):  # Se añade self
        heapq.heapify(arr)
        return [heapq.heappop(arr) for _ in range(len(arr))]