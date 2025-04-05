class RadixSort:
    
    def __init__(self):
        pass

    def radix_sort(self, arr):
        max_val = max(arr, key=lambda x: x[1])[1]
        exp = 1
        while max_val // exp > 0:
            arr = sorted(arr, key=lambda x: (x[1] // exp) % 10)
            exp *= 10
        return arr