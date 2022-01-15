# File with functions representing each a different little exercise or problem


# Generate a 3d List, with the size indicated through the parameters
def generate_3D_list(x: int, y: int, z: int):
    #new_list = [[['*' for col in range(x)] for col in range(y)] for col in range(z)]

    # 1D list case
    dimA = ['*' for col in range(x)]
    # 2D list case
    if x == 0:
        dimB = ['*' for col in range(y)]    # 1D list
    else:
        dimB = [dimA for col in range(y)]    # 2D list
    # 3D list case
    if x == 0 and y == 0:
        new_list = ['*' for col in range(z)]    # 1D list
    elif x == 0:
        new_list = [dimB for col in range(z)]    # 2D list
    elif y == 0:
        new_list = [dimA for col in range(z)]    # 2D list
    else:
        new_list = [dimB for col in range(z)]    # 3D list
    print(new_list)
