def TelDoelParen():
    n = len(nummers)
    count = 0
    for getal in range(n):
        for getal2 in range(getal + 1):
            if nums[getal] + nums[getal2] < doel :
                tel += 1
    return tel
nummers = [1 ,2, 3, 4, 5]
doel = 6
print(TelDoelParen(nummers, doel))
