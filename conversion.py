# Code fait par Alain Chidiac
# Conversion d'un nombre à base 10 à un binaire
# Convertion of a decimal into a binary
'''bin = ""
dec = int(input("Met le nombre en base 10 : "))
while dec >= 1 :
    modulo = dec % 2
    dec = dec // 2
    if modulo == 1 :
        bin = "1" + bin
    else :
        bin = "0" + bin
print(bin)'''
# Conversion d'un nombre en base 10 à un hexadécimale
# Convertion of a decimal into an hexadecimal
"""sup = ("A","B","C","D","E","F") # We define the possible values that are over nine
hex = ""
dec = int(input("Met le nombre en base 10 : "))
while dec >= 1 :
    modulo = dec % 16
    dec = dec // 16
    if modulo != 0:
        if modulo < 10 :
            hex = str(modulo) + hex
        else :
            n = 10
            n_tuple = 0
            while n != modulo :
                n += 1
                n_tuple += 1
            fin = sup[n_tuple]
            hex = str(fin) + hex
    else :
        hex = str(dec) + hex
print(hex)"""
# Conversion d'un nombre hexadécimale à un binaire
# Conversion of an hexadecimal into a binary
"""hex = input("met un nombre en base 16 : ")
sup = ("A","B","C","D","E","F")
bin = ""
for t in hex :
    try :
        t = int(t)
        bin_2 = ""
        while t >= 1 :
            modulo = t % 2
            t = t // 2
            if modulo == 1 :
                bin_2 = "1" + bin_2
            else :
                bin_2 = "0" + bin_2
        while len(bin_2) < 4 :
            bin_2 = "0" + bin_2
        bin = bin + bin_2 + " "
    except :
        n = 0
        bin_3 = ""
        while sup[n] != t :
            n += 0
        dec = 10 + n
        while dec >= 1 :
            modulo = dec % 2
            dec = dec // 2
            if modulo == 1 :
                bin_3 = "1" + bin_3
            else :
                bin_3 = "0" + bin_3
        bin = bin + bin_3 + " "
print(bin)"""
# Conversion d'un nombre binaire à la base 10
# Convertion of a binary into a decimal
"""dec = 0
bin = input("Met le nombre binaire : ")
puis = len(bin) - 1
for t in bin :
    bin = int(bin)
    if int(t) > 1 :
        print("Le nombre n'est pas binaire.")
    num = int(t)*2**puis
    dec += num
    puis -= 1
    bin = str(bin)
print(dec)"""
# Conversion d'un nombre hexadécimal à la base 10
# COnvertion of a hexadecimal into a decimal
"""dec = 0
sup = ("A","B","C","D","E","F")
hex = input("Met le nombre en base 16 : ")
puis = len(hex) - 1
for t in hex :
    try :
        num = int(t)*16**puis
    except :
        num = 0
        n = 0
        diz = 10
        while sup[n] != t :
            n += 0
            diz += n
        num = int(diz)*16**puis
    puis -= 1
    dec += num
print(dec)"""
# Conversion d'un nombre binaire à un hexadécimale
# Convertion of a binary into an hexadecimal
"""sup = ("F","E","D","C","B","A")
hex = ""
n_bit = 0
bin = input("Met le nombre binaire : ")
for t in bin :
    n_bit += 1
if n_bit % 4 != 0 :
    n_0 = 4 - n_bit % 4
    for i in range(n_0) :
        bin = "0" + bin
for t in range (0, len(bin), 4) :
    bits = bin[t : t+4]
    a, b, c, d = bits
    bin_temp = a + b + c + d
    dec = 0
    puis = len(bin_temp) - 1
    for t in bin_temp :
        if int(t) > 1 :
            print("Le nombre n'est pas binaire.")
        num = int(t)*2**puis
        dec += num
        puis -= 1
        bin_temp = str(bin_temp)
    if dec < 10 :
        hex = hex + str(dec)
    else :
        let = 15 - dec
        hex = hex + sup[let]
print(hex)"""
