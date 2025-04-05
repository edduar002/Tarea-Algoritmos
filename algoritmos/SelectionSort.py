class SelectionSort:
    
    def __init__(self):
        pass

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j][1] < arr[min_idx][1]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr