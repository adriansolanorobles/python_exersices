
string_two_dimensional_lis = raw_input("Enter two digits in the form X,Y: ")

two_dimensional_list = []

rows = int(string_two_dimensional_lis.split(',')[0])
colums = int(string_two_dimensional_lis.split(',')[1])

for i in range(0,rows):
    two_dimensional_list.append(["O"] * colums)

for r in range(rows):
    for c in range(colums):
        two_dimensional_list[r][c] = r*c


print two_dimensional_list

