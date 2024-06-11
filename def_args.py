def sum_all(*args):
    print(args) # print tuples

    # manual handling *args
    for i in args:
        print(i ** 3)
    return sum(args)

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,5))
print(sum_all(1,2,3,6,7,10))