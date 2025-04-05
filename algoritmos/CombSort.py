class CombSort:
    
    def __init__(self):
        pass

    def comb_sort(self, arr):
        gap = len(arr)
        shrink = 1.3
        sorted_flag = False
        while gap > 1 or not sorted_flag:
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1
            sorted_flag = True
            for i in range(len(arr) - gap):
                if arr[i][1] > arr[i + gap][1]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    sorted_flag = False
        return arr