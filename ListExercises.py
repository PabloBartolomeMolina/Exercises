# File with functions representing each a different little exercise or problem


# Generate a 3d List, with the size indicated through the parameters
def generate_3d_list(x: int, y: int, z: int):
    # 1D list case
    dimA = ['*' for col in range(x)]
    print('dimA ', dimA)
    # 2D list case
    if x == 0:
        dimB = ['*' for col in range(y)]    # 1D list
    else:
        dimB = [dimA for col in range(y)]    # 2D list
    print('dimB ', dimB)
    # 3D list case
    if x == 0 and y == 0:
        new_list = ['*' for col in range(z)]    # 1D list
    elif x == 0:
        new_list = [dimB for col in range(z)]    # 2D list
    elif y == 0:
        new_list = [dimA for col in range(z)]    # 2D list
    else:
        new_list = [dimB for col in range(z)]    # 3D list
    print('new_list ', new_list)


# Compare two different lists.
def compare_lists(list1, list2):
    flag_discrepancy = False
    if len(list1) != len(list2):
        print("Lists have different length, they cannot be identical")
    else:
        length = len(list1)
        for i in range(length):
            if list1[i] == list2[i]:
                pass
            else:
                print("Discrepancy found! Lists are not identical")
                flag_discrepancy = True
                break
        if not flag_discrepancy:
            print("Both lists are identical!!")


# Get the differences between two given lists
def different_lists(list1, list2):
    list3 = [("list1 elements", "list2 elements")]
    if len(list1) != len(list2):
        print("Length of first list: ", len(list1))
        print("Length of second list: ", len(list2))
        list3.append((list1, list2))
    else:
        length = len(list1)
        for i in range(length):
            if list1[i] == list2[i]:
                list3.insert(len(list3), (list1[i], list2[i]))
            else:
                list3.append((list1[i], list2[i]))
    print(list3)


# Check if a given list is shorted or not.
def shorted_list(input_list):
    flagged = False
    for i in range(len(input_list)-1):
        if input_list[i] > input_list[i + 1]:
            print("List is not shorted!")
            flagged = True
            break
        else:
            pass
    if not flagged:
        print("List is properly shorted")

