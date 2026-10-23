def round(num):
    rounded = 0
    i = 0
    
    while i < num - 1:
        i += 1
    
    if num - i < 0.5:
        rounded = i
    else:
        rounded = i + 1
        
    return rounded

def length(list):
    length = 0
    
    for v in list:
        length += 1
    
    return length

def sort(list):
    l = length(list)
    
    for i in range (1, l):            
        if list[i - 1] > list[i]:
            (list[i - 1], list[i]) = (list[i], list[i - 1])
            sort(list)
    
    return list

list = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

for i in range(0, length(list)):
    list[i] = round(list[i])

print(sort(list))