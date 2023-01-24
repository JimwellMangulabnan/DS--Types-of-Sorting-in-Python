print("\n\t\t\t***************  PROGRAMMED BY  **********")
print("\t\t\t*********** JIMWELL L. MANGULABNAN *******")
print("\t\t\t**************** BSCOE 2-2 ***************")
print()

print("\t\t\t===========This is Bubble Sort============")
print()

number = [7, 62, 85, 72, 45, 77, 63, 5, 88, 30]

def BubbleSort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            print("\n\t\t\tThe index value of first element is: ", j)
            print("\t\t\tThe index value of second element is: ",j+1)
            print("\t\t\tThis is current arrangement of array: \n\t\t\t====>",numbers,"\n")
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                print("\n\t\t\t\tThe first element will be switched \n\t\t\tbecause it is greater than the second element.")
                print("\n\t\t\tThis is the array that has been updated.: \n\t\t\t====>",numbers)

