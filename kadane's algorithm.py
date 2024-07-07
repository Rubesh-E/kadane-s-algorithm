def max_array(arr):
    current_max = current_global = arr[0]
    for i in arr[1:]:
        current_max = max(i,current_max+i)
        if current_max > current_global:
            current_global = current_max

    return current_global


arr = []
for _ in range(5):
    num = int(input())
    arr.append(num)

print("maximum subarray",max_array(arr))
