# 과제 32
a = {1, 3, 7, 13, 15} 
b = {1, 24, 365, 3, 7}

union_set = a | b
intersection_set = a & b

print(union_set, intersection_set)

# 과제 33
a = {1, 3, 7, 13, 15} 
b = {1, 24, 365, 3, 7}

difference_set = a - b
symmentric_difference_set = a ^ b

print(difference_set, symmentric_difference_set)

# 과제 34
a = {1, 3, 7, 13, 15} 
a.update({100})
print(a)

# 과제 35
a = {100, 200, 300, 400, 500}

a.intersection_update({400, 500, 600, 700, 800})
a.difference_update({400, 500, 600, 700, 800})
a.symmetric_difference_update({400, 500, 600, 700, 800})

print(a)

# 과제 36
a = {100, 200, 300, 400, 500}

if a.issuperset({100, 200, 300, 400, 500}) and a.issubset({100, 200, 300, 400, 500}):
    print("동시")
elif a.issuperset({100, 200, 300, 400, 500}):
    print("상위")
elif a.issubset({100, 200, 300, 400, 500}):
    print("부분")

# 과제 37
a = {1, 3, 7, 13, 15}
a.add(1000)
a.remove(1000)
print(a)

# 과제 38
multiples = {x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0}
print(multiples)