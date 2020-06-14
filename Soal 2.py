# Soal 2

my_list_number = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 0]

def create_phone_number(number):
    a = []
    for i in number[0:3]:
        a.append(str(i))
    a = "".join(a)
    
    b = []
    for j in number[3:6]:
        b.append(str(j))
    b = "".join(b)
        
    c = []
    for k in number[6:10]:
        c.append(str(k))
    c = "".join(c)

    return "({}) {}-{}".format(a, b, c)

print(create_phone_number(my_list_number))
    