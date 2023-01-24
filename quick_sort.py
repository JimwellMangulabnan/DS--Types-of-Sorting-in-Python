print("\n\t\t\t*************  PROGRAMMED BY  ************")
print("\t\t\t*********** JIMWELL L. MANGULABNAN *******")
print("\t\t\t*************** BSCOE 2-2 ****************")
print()

print("\t\t\t============This is Quick Sort============")
print()


number = [7, 62, 85, 72, 45, 77, 63, 5, 88, 30]
print("\t\t\tArray:",number)

def quickSort(array, left, right):
    if left < right:

        pi = partition(array, left, right)
        quickSort(array, left, pi - 1)
        quickSort(array, pi + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    print("\n\t\t\tThis is the given Pivot: ", pivot)
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
            print("\n\t\t\tIndex value: ", i, "\n\t\t\tThe element is: ", arr[i])
        while j > left and arr[j] >= pivot:
            j -= 1
            print("\n\t\t\tIndex value: ", j, "\n\t\t\tThe element is: ", arr[j])
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            print("\n\t\t\tThis is the array that has been updated: \n\t\t\t---->",arr)

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
        print("\n\t\t\tThis is the array that has been updated: \n\t\t\t---->", arr)
    return i

quickSort(number, 0, len(number) - 1)
print("\n\t\t\t~~~~~~~~This is the Final sorted array~~~~~~~~~\n\t\t\t ====>",number)
print()
