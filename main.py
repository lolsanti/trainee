# my_str = "i like latinos"
# sab = "like, like, slime, live"
# print(my_str[2])
# print(my_str[-2])
# print(my_str[:5])
# print(my_str[:-2])
# print(my_str[1::2])
# print(my_str[::-1])
# print(len(my_str))

# print(my_str.count(" "))
# print(len(my_str))

# print(sab.count("l"))

# s = 'ahhhhha'

# first_h = s.find('h')
# last_h = s.rfind('h')

# result = s[:first_h+1] + s[first_h+1:last_h].upper() + s[last_h:]
# print(result)

# my_list = [1, 200, 2, 300, 3, 400]
# result = []
# for item in my_list:
# if item > 100:
# print(item)

# for item in my_list:
# if item > 100:
# result.append(item)

# print(result)


# my_list = [1, 200, 2, 300, 3, 400]

# if len(my_list) < 2:
# my_list.append(0)
# else:
# (my_list.append(my_list[-1] + my_list[-2]))

# print(my_list)


# value = 1003000
# val_str = str(value)
# last_zero = len(val_str) - len(val_str.rstrip('0'))
# print(last_zero)


first_list = [1, 2, 3, 4]
second_list = [5, 6, 7, 8]
result = []

for item in first_list[1::2] + second_list[1::2]:
    result.append(item)

print(result)