def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return joinSorted(left, right)


def joinSorted(arr1, arr2):
    output = []
    i = j = k = 0
    while i < len(arr1) or j < len(arr2):
        if i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                output.append(arr1[i])
                i += 1
            else:
                output.append(arr2[j])
                j += 1
        elif i < len(arr1):
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1
        k += 1
    return output
