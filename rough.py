num = [5]

def all_num(num):
    for i in range(0,num[0]):
        yield i

print(all_num(num))