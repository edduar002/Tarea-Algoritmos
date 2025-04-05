class BucketSort:
    
    def __init__(self):
        pass

    def bucket_sort(self, arr):
        max_val = max(arr, key=lambda x: x[1])[1]
        size = max_val // len(arr) + 1
        buckets = [[] for _ in range(size)]
        for term in arr:
            buckets[term[1] // size].append(term)
        for bucket in buckets:
            bucket.sort(key=lambda x: x[1])
        return [item for sublist in buckets for item in sublist]