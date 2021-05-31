def binary_search(arr, num, left, right):
    mid = (left + right) // 2

    # unsorted
    if left > right:
        return -1

    if arr[mid] == num:
        return mid

    if arr[mid] < num:
        return binary_search(arr, num, mid + 1, right)
    else:
        return binary_search(arr, num, left, mid - 1)
