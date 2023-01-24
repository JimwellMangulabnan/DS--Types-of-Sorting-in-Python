print("\n\t\t\t*************  PROGRAMMED BY  ************")
print("\t\t\t*********** JIMWELL L. MANGULABNAN *******")
print("\t\t\t*************** BSCOE 2-2 ****************")
print()

print("\t\t\t============This is Merge Sort============")
print()

number = [7, 62, 85, 72, 45, 77, 63, 5, 88, 30]

print("\t\t\tArray:",number)
def mergeSort(number):
    if len(number) > 1:
        mid = len(number) // 2
        left = number[:mid]
        right = number[mid:]
        print("\n\t\t\tLeft: ",left,"\tRight: ",right)

        mergeSort(left)
        mergeSort(right)

       