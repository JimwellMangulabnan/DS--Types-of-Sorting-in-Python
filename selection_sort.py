print("\n\t\t\t\t*********  PROGRAMMED BY  ********")
print("\t\t\t\t***** JIMWELL L. MANGULABNAN *****")
print("\t\t\t\t********** BSCOE 2-2 *************")
print()

print("\t\t\t===========This is Selection Sort============")
print()

number = [7, 62, 85, 72, 45, 77, 63, 5, 88, 30]
print("\t\t\tArray: ", number)
print()

def sort(number):
    for i in range(9):
        minimum_position = i
        for j in range(i,10):
            if number[j] < number[minimum_position]:
                minimum_position = j

        swap = number[i]
        number[i] = number[minimum_position]
        number[minimum_position] = swap

        print("\t\t\tThis is step by step process in selection sort: \n\n\t\t\t====>",number,"\n")

sort(number)

print("\n\t\t\t---> This is the Final Sorting in Selection <--- \n\n\t\t\t====>",number)