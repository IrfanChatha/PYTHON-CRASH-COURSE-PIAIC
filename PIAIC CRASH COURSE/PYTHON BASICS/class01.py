name = "Irfan"
print(name)
print(type(name))  # same as typeof - 'str'
print(id(name))  # physical address
# print(dir(name))
print([i for i in dir(name) if "_" not in i])  # methods and attributes
print("-------------------------")
