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
           