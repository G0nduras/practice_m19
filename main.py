target_value = int(input("Enter value target: "))
lenght_array = int(input("Enter length: "))
user_array = []
calculating_array = []
# print(type(target_value))
n = 0
while n < lenght_array:
    added_element = "Enter element №" + str(n + 1) + ": "
    user_array.append(int(input(added_element)))
    n += 1

user_array.sort()

# print(type(user_array[(len(user_array)) // 2]))
# print(user_array)
# print(user_array[(len(user_array)) // 2])
# def centre_element_array(n: list):
    # if len(n) % 2 == 0:


calculating_array = user_array
#print(user_array)
#print(calculating_array)

while (target_value != calculating_array[((len(calculating_array)) // 2)]) and (len(calculating_array) != 1):
    centre_element = calculating_array[((len(calculating_array)) // 2)]
    print(len(calculating_array), "lennh")
    print(centre_element)
    print(calculating_array)
    if centre_element < target_value:
        calculating_array = calculating_array[((len(calculating_array)) // 2):]
    else:
        calculating_array = calculating_array[:((len(calculating_array)) // 2)]
        print(calculating_array)

calculating_value = calculating_array[(len(calculating_array)) // 2]

# print("Index target in array:", str(len(calculating_array) // 2))
if target_value != calculating_array[((len(calculating_array)) // 2)]:
    print("Index unavaliable in array")
else:
    print("Index target in array:", user_array.index(calculating_value))

#print(user_array)
#print(calculating_array)
# print(user_array)
