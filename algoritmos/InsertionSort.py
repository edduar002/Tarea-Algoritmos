class InsertionSort:

    def __init__(self):
        pass

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j][1] > key[1]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
