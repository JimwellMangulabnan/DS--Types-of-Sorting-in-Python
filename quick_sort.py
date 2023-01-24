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


