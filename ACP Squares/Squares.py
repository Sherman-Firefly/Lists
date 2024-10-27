def prange(start, end):
    even=[]
    odd=[]

    for number in range(start, end+1):
        square = number ** 2
        if square % 2 == 0:
            even.append(square)
        else:
            odd.append(square)

    return even, odd

startn=1
endn=10
evenn, oddn = prange(startn, endn)

print("Even: ", evenn)
print("Odd: ", oddn)
