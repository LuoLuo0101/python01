def evgSplit(sum1, N):
    list1, other = [], sum1 % N
    for i in range(N):
        evg, other = sum1 // N + 1 if other > 0 else sum1 // N, other - 1
        list1.append(evg)
    return list1


list1 = evgSplit(999, 10)
list2 = evgSplit(1001, 10)
list3 = evgSplit(9, 10)

print(list1)
print(list2)
print(list3)

'''
[100, 100, 100, 100, 100, 100, 100, 100, 100, 99]
[101, 100, 100, 100, 100, 100, 100, 100, 100, 100]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
'''
