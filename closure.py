"""import asyncio


def outer(x):

    def inner():
        return x

    return inner


f = outer(10)

#print(f())     # 10

# async or await concept in python
async def hello():
    print("Hello")
hello()"""

"""nums = [1, 2, 3, 4]
mp = {}

for i, x in enumerate(nums):
    if x not in mp:
        mp[x] = []
    mp[x].append(i+1)
print(mp)"""
nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, x in enumerate(nums):
    need = target - x

    if need in seen:
        print(seen[need], i)

    seen[x] = i