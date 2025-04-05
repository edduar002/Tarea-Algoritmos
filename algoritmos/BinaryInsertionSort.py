class BinaryInsertionSort:
    
    def __init__(self):
        pass

    def binary_insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            left, right = 0, i - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][1] < key[1]:
                    left = mid + 1
                else:
                    right = mid - 1
            arr = arr[:left] + [key] + arr[left:i] + arr[i+1:]
        return arr