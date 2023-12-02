my_dict = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as p_log:
    data = p_log.readlines()

    for i in data:
        k = i.removesuffix('\n').split(' ')
        a = k[0]
        b = k[1]
        my_dict[a] = b

print(my_dict)


