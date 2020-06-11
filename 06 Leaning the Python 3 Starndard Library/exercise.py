def multi_add(*args):
    print(type(args))
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(4,5,10,4))