n = 5

for i in range(1,11):
    # we want to skip the 5th iteration
    if i == 5:
        continue
    print(n,"x",i,"=", n*i)