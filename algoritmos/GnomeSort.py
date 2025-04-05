class GnomeSort:
    
    def __init__(self):
        pass

    def gnome_sort(self, arr):
        i = 0
        while i < len(arr):
            if i == 0 or arr[i - 1][1] <= arr[i][1]:
                i += 1
            else:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
        return arr