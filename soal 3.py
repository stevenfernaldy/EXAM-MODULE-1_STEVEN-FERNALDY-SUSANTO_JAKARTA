def sort_odd_even(num):
    ganjil = []
    genap = []

    for i in num:
        if i % 2 != 0:
            ganjil.append(i)
        else:
            genap.append(i)
            
    for a in range(len(ganjil)):
        for b in range(a + 1, len(ganjil)):
            if ganjil[a] > ganjil[b]:
                temp = ganjil[a]
                ganjil[a] = ganjil[b]
                ganjil[b] = temp
    
    for c in range(len(genap)):
        for d in range(c + 1, len(genap)):
            if genap[c] < genap[d]:
                temp = genap[c]
                genap[c] = genap[d]
                genap[d] = temp

    num[0] = ganjil[0]
    num[1] = ganjil[1]
    num[4] = ganjil[2]
    num[2] = genap[0]
    num[3] = genap[1]
    num[5] = genap[2]

    return num

print(sort_odd_even([5, 3, 2, 8, 1, 4]))





