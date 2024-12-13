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
    #print(centre_element)
    #print(calculating_array)
    if centre_element < target_value:
        calculating_array = calculating_array[((len(calculating_array)) // 2):]
    else:
        calculating_array = calculating_array[:((len(calculating_array)) // 2)]
        #print(calculating_array)

calculating_value = calculating_array[(len(calculating_array)) // 2]

# print("Index target in array:", str(len(calculating_array) // 2))
if target_value != calculating_array[((len(calculating_array)) // 2)]:
    print("Index unavaliable in array №1")
else:
    print("Index target in array №1:", user_array.index(calculating_value))

#print(user_array)
#print(calculating_array)


#arrayy = [1, 2, 3, 4, 5, 6, 7]
#print(arrayy[1:3], "sliceeeeeeeeeeeee")

def binary_calculating_value(target: int, array: list, position1: int, position2: int):
   # centre = lenght // 2
   # last_element = centre // 2 - (len(array) - 1)
   # array.sort()
   # last_element = lenght - 1
   # first_elemant = 0
   # centre = (first_elemant + last_element) // 2
   # centre = len(slice_array) // 2
   # postiton1 = slice_array[0]
    array.sort()
    if position2 < position1:
        return None
    print(position1, "position1")
   # position2 = len(slice_array) - 1
    print(position2, "position2")
    centre_position = (position1 + position2) // 2
    print(centre_position, "centre_position")
   # first_element_slice = 
   # last_element_clise = 
   # first_element = array[0]
   # last_element = lenght - 1=    centre = 

    if array[centre_position] == target:
        print(centre_position, "centreeee")
        return centre_position
    elif array[centre_position] > target:
      #  print(slice_array[0:position], "sliceeee >")
        return binary_calculating_value(target, array, position1, centre_position - 1)
    else: 
      #  print(slice_array[position + 1:len(slice_array)], "sliceeeee <")
        return binary_calculating_value(target, array, centre_position + 1, position2)

user_array = [3, 1, 2, 5, 4, 7, 8]
user_target = target = 7
#user_lenght = 5
target_value2 = binary_calculating_value(user_target, user_array, position1=0, position2=len(user_array) - 1)
if target_value2 == None:
    print("Index unavaliable in array №2")
else:
    print("Index target in array №2:", target_value2)
