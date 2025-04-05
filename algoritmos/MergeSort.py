class MergeSort:    

    def __init__(self):
        pass

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self._merge(left, right)

    def _merge(self, left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
