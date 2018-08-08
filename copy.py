import copy
# Experimenting with python shallow copy and deepcopy
# Different kind of copying in python

def main():
    old_list = [[1, 2, 3], [4, 2, 7], [3, 7, 1]]
    print(old_list)

    # Copy the old_list into new_list
    new_list = old_list
    print(new_list)

    # Make changes to old_list and monitor effect on new_list
    old_list.append([2, 1, 2])
    print(old_list)
    print(new_list) #confirmed new_list stores a reference of the old list

    line_separator = "-----------------------------------"
    print(line_separator)

    # SHALLOW COPY
    # we already have our old list variable no need to recreate/initialize
    new_list = old_list.copy()
    print(old_list)
    print(new_list)

    # make changes to old list
    old_list.append([3, 7, 8])
    print(old_list)
    print(new_list)

    print(line_separator)

    # when you change an element in old_list everything updates
    old_list[0][2] = 'WW'
    print(old_list)
    print(new_list)

    # use deepcopy to recurse over all elements and copy them
    new_list = copy.deepcopy(old_list)
    print(old_list)
    print(new_list)

    # copy.deepcopy(copies an entire list)

if __name__=="__main__":
    main()