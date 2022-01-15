# File with functions representing each a different little exercise or problem


# Generate a 3d List, with the size indicated through the parameters
def generate_3D_list(x: int, y: int, z: int):
    new_list = [[['*' for col in range(x)] for col in range(y)] for col in range(z)]
    print(new_list)
