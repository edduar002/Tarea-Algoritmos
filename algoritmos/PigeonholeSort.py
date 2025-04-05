class PigeonholeSort:
    
    def __init__(self):
        pass

    def pigeonhole_sort(self, arr):
        min_val = min(arr, key=lambda x: x[1])[1]
        max_val = max(arr, key=lambda x: x[1])[1]
        size = max_val - min_val + 1
        holes = [[] for _ in range(size)]
        for term in arr:
            holes[term[1] - min_val].append(term)
        return [item for sublist in holes for item in sublist]