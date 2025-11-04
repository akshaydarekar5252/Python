def even_generator(limit):
    for i in range(2, limit+1, 2):
        # return i
        yield i # it store the value and its state in memory

for num in even_generator(10):
    print(num)