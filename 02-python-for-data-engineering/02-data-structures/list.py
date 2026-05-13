#a list
salary = [1000,20000,3300]

#list function takes iterable and converts to list
name = list("spark")
print(name)

#list is heterogeneous and will accept duplicates
diff_types_list=[100,'Jake',False,302.65,100]
print(type(diff_types_list))

#list is an ordered collection of data (order won't change) - use index to access its elements
lst_num = [3,5,7,2,9,1]

print(lst_num[2]) #accessing 3rd element since index starts with 0
print(lst_num[-1]) #accessing last element
print(lst_num[-2]) #accessing 2nd last element

lst_num.sort() #sorts the given list
print(f"sorted list: {lst_num}")

lst_num2 = list(range(1,11,3)) #notice how list accepts iterable element (range)
lst_num.extend(lst_num2)
print(f"list after extend: {lst_num}")

fruit_list = ["apple", "banana", "cherry", "strawberry", "peach", "pineapple", "peach" ]

fruit_list[1] = "watermelon" #we can update list elements

fruit_list.append('orange') #append adds element at the end of the list

fruit_list.insert(1,"mango") #to add new element in given index

print(len(fruit_list)) #to find length of list

fruit_list.remove("apple") #to remove an element from list (first occurrence of given element)

popped_element = fruit_list.pop(2) #pop deletes given element and returns it, if no index is given it will pop last element
print(f"popped element is: {popped_element}")

watermelon_index = fruit_list.index("watermelon") #index provides the index of first occurrence of given element
print(f"index of watermelon is {watermelon_index}")

peach_count = fruit_list.count("peach") #to get count of given elements in list
print(f"count of peach is {peach_count}")

print(f"fruit_list after all list operations: {fruit_list}")

#slicing in python ---------------------------------------------------

print(f"to get every 2nd element from the list starting from index 0 - fruit_list[::2] : {fruit_list[::2]}")
print(f"to get every 2nd element from the list starting from index 1 - fruit_list[1::2] : {fruit_list[1::2]}")
print(f"to get list in reverse order - fruit_list[::-1] : {fruit_list[::-1]}")
print(f"to get every 2nd element from the list in reverse order - fruit_list[::-1][::2] : {fruit_list[::-1][::2]}")

fruit_list.clear() #clears the list
print(f"fruit_list after clear: {fruit_list}")
