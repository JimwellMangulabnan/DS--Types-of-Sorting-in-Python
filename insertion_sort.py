print("\n\t\t\t***************  PROGRAMMED BY  ************")
print("\t\t\t************* JIMWELL L. MANGULABNAN *******")
print("\t\t\t***************** BSCOE 2-2 ****************")
print()

print("\t\t\t===========This is insertion Sort===========")
print()

number = [7, 62, 85, 72, 45, 77, 63, 5, 88, 30]

def insertion(number):
    for a in range(1, len(number)):
        b = a 
        while b > 0 and number[b] < number[b-1]:
            number[b-1], number[b] = number[b], number[b-1]
            b-=1
            print("\n\t\t\tThis is step by step process in insertion sort: \n\n\t\t\t====>", number)

insertion(number)
print("\n\t\t\t__________This is the Final sorted array________\n\t\t\t ====>",number)
print()
