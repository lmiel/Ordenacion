
def binay_search(arr, start, end, n):
    mid = int((start + end) / 2)
    if start >= end:
        return mid is False
    elif arr[mid] < n:
        return binay_search(arr, mid + 1, end, n)
    elif arr[mid] > n:
        return binay_search(arr, start, mid, n)
    else:
        while arr[mid] == n and mid != 0:
            mid -= 1
        return (mid + 1, True)

def binary_search_insert(arr, n):
    pos, exists = binay_search(arr, 0, len(arr), n)
    if not exists:
        arr.insert(pos, n)
        
(kids, max_weight) = list(map(int, input().split()))
weights = list(map(int, input().split()))

sorted_weights = []
for weight in weights:
    binary_search_insert(sorted_weights, weight)
    
gondolas = 0
right_index = kids - 1
left_index = 0

while left_index <= right_index:
    gondolas += 1
    if sorted_weights[right_index] + sorted_weights[left_index] <= max_weight:
        left_index += 1
    right_index -= 1
    print(gondolas)
    