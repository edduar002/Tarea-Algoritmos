class BubbleSort:
    
    def __init__(self):
        pass

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j][1] > arr[j+1][1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr