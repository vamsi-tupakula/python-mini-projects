def binary_search(ls, key, start, end):
    # base condition
    if end < start:
        return -1

    mid = (start + end)//2
    if ls[mid] == key:
        return mid
    elif key > ls[mid]:
        return binary_search(ls, key, mid+1,end)
    else:
        return binary_search(ls, key, start, mid-1)

print(binary_search([1,2,3,4,5], 3, 0, 4))