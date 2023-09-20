
# LIST

# Add
my_list = [1, 2, 3, 4]
element_to_add = 5
my_list.append(element_to_add)
# Alternatively, you can insert at a specific index:
# my_list.insert(index, element_to_add)
print(my_list)  # [1, 2, 3, 4, 5]




# Removes 
my_list = [1, 2, 3, 4, 5]
element_to_remove = 3
if element_to_remove in my_list:
    my_list.remove(element_to_remove)  
# Alternatively, you can remove by index:
# my_list.pop(index)
print(my_list)  # [1, 2, 4, 5]


# Search 
my_list = [1, 2, 3, 4, 5]
element_to_search = 3
if element_to_search in my_list:
    print(f"{element_to_search} found in the list.")
else:
    print(f"{element_to_search} not found in the list.")



# Dict
# Add
my_dict = {"name": "John", "age": 30}
key_to_add = "city"
value_to_add = "New York"
my_dict[key_to_add] = value_to_add
print(my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York'}



# Removes 
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
key_to_remove = 'age'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
# Alternatively, you can use pop to remove an item by key:
# my_dict.pop(key_to_remove)
print(my_dict)  # {'name': 'John', 'city': 'New York'}


# Search 
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
key_to_search = 'age'
if key_to_search in my_dict:
    print(f"{key_to_search} found in the dictionary with value: {my_dict[key_to_search]}")
else:
    print(f"{key_to_search} not found in the dictionary.")





# List of Lists Operations 


list_of_lists = [[1, 2], [3, 4]]
new_list = [5, 6]
list_of_lists.append(new_list)
print(list_of_lists)
# Output: [[1, 2], [3, 4], [5, 6]]



list_of_lists = [[1, 2], [3, 4], [5, 6]]
list_to_remove = [3, 4]
if list_to_remove in list_of_lists:
    list_of_lists.remove(list_to_remove)
print(list_of_lists)
# Output: [[1, 2], [5, 6]]





list_of_lists = [[1, 2], [3, 4], [5, 6]]
list_to_search = [3, 4]
if list_to_search in list_of_lists:
    print(f"{list_to_search} found in the list of lists.")
else:
    print(f"{list_to_search} not found in the list of lists.")



# Dictionary of Dictionaries Operations

dict_of_dicts = {'person1': {'name': 'John', 'age': 30}, 'person2': {'name': 'Alice', 'age': 25}}
key_to_add = 'person3'
value_to_add = {'name': 'Bob', 'age': 35}
dict_of_dicts[key_to_add] = value_to_add
print(dict_of_dicts)
# Output: {'person1': {'name': 'John', 'age': 30}, 'person2': {'name': 'Alice', 'age': 25}, 'person3': {'name': 'Bob', 'age': 35}}




dict_of_dicts = {'person1': {'name': 'John', 'age': 30}, 'person2': {'name': 'Alice', 'age': 25}}
key_to_remove = 'person2'
if key_to_remove in dict_of_dicts:
    del dict_of_dicts[key_to_remove]
print(dict_of_dicts)
# Output: {'person1': {'name': 'John', 'age': 30}}




dict_of_dicts = {'person1': {'name': 'John', 'age': 30}, 'person2': {'name': 'Alice', 'age': 25}}
key_to_search = 'person2'
if key_to_search in dict_of_dicts:
    print(f"{key_to_search} found in the dictionary of dictionaries with value: {dict_of_dicts[key_to_search]}")
else:
    print(f"{key_to_search} not found in the dictionary of dictionaries.")


# List of Dictionaries Operations

list_of_dicts = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]
dict_to_add = {'name': 'Bob', 'age': 35}
list_of_dicts.append(dict_to_add)
print(list_of_dicts)
# Output: [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 35}]


list_of_dicts = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 35}]
dict_to_remove = {'name': 'Alice', 'age': 25}
if dict_to_remove in list_of_dicts:
    list_of_dicts.remove(dict_to_remove)
print(list_of_dicts)
# Output: [{'name': 'John', 'age': 30}, {'name': 'Bob', 'age': 35}]



list_of_dicts = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]
dict_to_search = {'name': 'Alice', 'age': 25}
if dict_to_search in list_of_dicts:
    print(f"{dict_to_search} found in the list of dictionaries.")
else:
    print(f"{dict_to_search} not found in the list of dictionaries.")






try:
    val=int(input("enter the num :"))
except:
    print("error")    




