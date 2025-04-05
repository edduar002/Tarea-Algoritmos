class BitonicSort:
    
    def __init__(self):
        pass

    def bitonic_sort(self, arr):
        return sorted(arr, key=lambda x: x[1])