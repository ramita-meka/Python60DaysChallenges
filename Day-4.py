number_list = []
string_list = []
count_num = 0
count_string = 0
N = int(input("Enter no.of elements in a list: "))
for i in range(N):
    var = input("Enter the elements: ")
    if var == "":
        continue
    if var[0] >= '0' and var[0] <= '9':
        number_list = number_list + [int(var)]
        count_num = count_num + 1
    else:
        string_list = string_list + [var]
        count_string = count_string + 1

found_num = count_num
found_string = count_string
name = input("Enter your name: ")

if len(name)%2 == 0:
    if count_num > 0:
        number_list = number_list[1:]
        count_num = count_num - 1
    if count_string > 0:
        string_list = string_list[1:]
        count_string = count_string - 1
else:
    if count_num > 0:
        number_list = number_list[:-1]
        count_num = count_num - 1
    if count_string > 0:
        string_list = string_list[:-1]
        count_string = count_string - 1

print("Numbers List:", number_list)
print("String List:", string_list)
print("Total Numbers found in List are:", found_num)
print("Total Strings found in List are:", found_string)
print("Total numbers in a list after personalization:", count_num)
print("Total strings in a list after personalization:", count_string)
