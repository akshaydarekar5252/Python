def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name="akshay", age="20" )
print_kwargs(age="30" )
print_kwargs(name="akshay", age="20", blood= "O+" )
