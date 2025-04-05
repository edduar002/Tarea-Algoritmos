class QuickSort:
    
    def __init__(self):
        pass

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x[1] < pivot[1]]
        middle = [x for x in arr if x[1] == pivot[1]]
        right = [x for x in arr if x[1] > pivot[1]]
        return self.quick_sort(left) + middle + self.quick_sort(right)