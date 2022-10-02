# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
#    где k принимает значения от 1 до n включительно.

# num = int(input())
# num_list = []

# for i in range(1, num + 1):
#     num_list.append(3 * i + 1)

# print(num_list)

n = int(input("enter n:\r\n"))
dic = {}
for i in range(n):
    dic[i + 1] = 3 * (i + 1) + 1
print(dic)