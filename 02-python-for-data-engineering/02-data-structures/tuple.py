#tuples are immutable , iterable and heterogeneous

tuple_example = (100, "banana", 55.4)

print(type(tuple_example))

#python throws error when you try to update it
#tuple_example[0] = 102  <- won't work

for i in tuple_example:
    print(i)  #iterable like list

print(tuple_example[::-1]) #slicing works in tuple as well

empty_tuple = ()
empty_tuple2 = tuple()
price1=(10,) #use comma at end to create a tuple with single element
price2=(10) #or else it will be considered as integer

print(f"price1's type: {type(price1)}")
print(f"price2's type: {type(price2)}")
