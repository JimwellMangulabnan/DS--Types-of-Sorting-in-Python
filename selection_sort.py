print("\n\t*********  PROGRAMMED BY  ********")
print("\t***** JIMWELL L. MANGULABNAN *****")
print("\t********** BSCOE 2-2 *************")
print()

number = [7, 62, 85, 72, 45, 77, 63, 5, 88, 30]

def sort(number):
    for i in range(7):
        minimum_position = i
        for j in range(i,10):
            if number[j] < number[minimum_position]:
                minimum_position = j

        swap = number[i]
        number[i] = number[minimum_position]
        number[minimum_position] = swap

        print(number)

sort(number)

print(number)