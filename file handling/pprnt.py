import pprint
data = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
result = pprint.pprint(data)
print(result)
print(type(result))

result2 = pprint.pformat(data)
print(result2)
print(type(result2))

