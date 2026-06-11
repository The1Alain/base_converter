# Code fait par Alain Chidiac
# Code made by Alain Chidiac
# Choix de la langue et de la convertion
# Language and conversion choice
lang_picked = False
conv_picked = False
def lang_choice() :
    global langue, lang_picked
    langue = input('0 -> English  |  1  -> Français')
    if langue == '1':
        langue = "French"
        lang_picked = True
    elif langue == '0':
        langue = "English"
        lang_picked = True
    else :
        lang_choice()
def conv_choice() :
    global conve, conv_picked
    if langue == "French":
        conve = input("0  -> Décimale à binaire | 1 -> Décimale à hexadécimale | 2 -> Héxadécimale à binaire | 3 -> Binaire à décimale | 4 -> Héxadécimale à décimale | 5 -> Binaire à Héxadécimale")
        conv_picked = True
    if langue == "English":
        conve = input("0  -> Decimal to binary | 1 -> Decimal to hexadecimal | 2 -> Hexadecimal to binary | 3 -> Binary to decimal | 4 -> Hexadecimal to decimal | 5 -> Binary to Hexadecimal")
        conv_picked = True
run = True
# Conversion d'un nombre à base 10 à un binaire
# Convertion of a decimal into a binary
def dec_bin():
    bin = "" # Varible that will contain the binary number / La variable qui possèderat la valeur dunombre binaire
    if langue == "French":
        dec = int(input("Met le nombre en base 10 : ")) # Variable qui possède la valeur du nombre décimal
    else :
        dec = int(input("Put the decimal number : ")) #  Variable that contains the value of the dcimal number
    # Repeats euclidien divisions until the decimal number is equal to 0
    # Répétition de division euclidienne jusqu'à que le nombre decimal soit null
    while dec >= 1 :
        modulo = dec % 2
        dec = dec // 2
        # Rajoute le reste de la division euclidienne dans la variable "modulo"
        # Adds the rest of the euclidien division in the "modulo" variable
        if modulo == 1 :
            bin = "1" + bin
        else :
            bin = "0" + bin
    print(bin)
# Conversion d'un nombre en base 10 à un hexadécimale
# Convertion of a decimal into an hexadecimal
def dec_hex():
    try :
        sup = ("A","B","C","D","E","F") # We define the possible values that are over nine / On définit les valeurs au dessus de 9
        hex = ""
        if langue == "French":
            dec = int(input("Met le nombre en base 10 : "))
        else :
            dec = int(input("Put the decimal number : "))
        # Repeats euclidien divisions by 16 until the decimal number is equal to 0
        # Répétition de division euclidiennepar 16 jusqu'à que le nombre decimal soit null
        while dec >= 1 :
            # Rajoute le reste de la division euclidienne dans la variable "modulo"
            # Adds the rest of the euclidien division in the "modulo" variable
            modulo = dec % 16
            dec = dec // 16
            if modulo != 0:
                if modulo < 10 :
                    hex = str(modulo) + hex
                # If the rest of the euclidien division is over 9 we take a letter from the "sup" tuple
                # Si le reste de la division euclidienne est au dessus de 9 on prend une lettre du tuple "sup"
                else :
                    n = 10
                    n_tuple = 0
                    # We go through each letter of the tuple until we find the correct one
                    # On part à travers chaque valeur du tuple jusqu'à qu'on trouve la bonne
                    while n != modulo :
                        n += 1
                        n_tuple += 1
                    fin = sup[n_tuple]
                    hex = str(fin) + hex
            # We add the found value
            # On rajoute la valeur trouvée
            else :
                hex = str(dec) + hex
        print(hex)
    except :
        conv
# Conversion d'un nombre hexadécimale à un binaire
# Conversion of an hexadecimal into a binary
def hex_bin():
    if langue == "French":
        hex = input("Met un nombre en base 16 : ")
    else :
        hex = input("Put the hexadecimal number : ")
    # We define the values over nin
    # On définit les valeurs au dessus de neuf
    sup = ("A","B","C","D","E","F")
    bin = ""
    for t in hex :
        # Try except is used here since if the number contains a letter the program would crash
        # Try except est utilisé ici plus que si le nombre conetein une lettre le programme pourrait se cassé.
        try :
            t = int(t)
            # Temporary variable to add an extra binary nmber
            # Variable temporaire utilisée pour rajouté un nombre binaire
            bin_2 = ""
            # We do the successive euclidien divisionon each digit one by one
            # On fait les division euclidienne succèssive de chaque chiffre un par un
            while t >= 1 :
                modulo = t % 2
                t = t // 2
                if modulo == 1 :
                    bin_2 = "1" + bin_2
                else :
                    bin_2 = "0" + bin_2
            # Adds zeros to numbers that have less than 4 bits
            # Rajoute des zeros à des nombre qui ont moin que 4 bits
            while len(bin_2) < 4 :
                bin_2 = "0" + bin_2
            bin = bin + bin_2 + " "
        # In case the number contains a lettre
        # Dans le cas que le nombre possède une lettre
        except :
            # We convert the letter into a decimal
            n = 0
            bin_3 = ""
            # On part à travers chaque lettre du tuple jusqu'à qu'on trouve la même
            # We go trough each letter of the tuple until we find one that matches
            while sup[n] != t :
                n += 1
            dec = 10 + n
            # On convertit le nombre décimal trouvé en un binaire
            # We convert the found decimal nomber into a binary number
            while dec >= 1 :
                modulo = dec % 2
                dec = dec // 2
                if modulo == 1 :
                    bin_3 = "1" + bin_3
                else :
                    bin_3 = "0" + bin_3
            # On rajoute le nombre binaire trouvé
            bin = bin + bin_3 + " "
    print(bin)
# Conversion d'un nombre binaire à la base 10
# Convertion of a binary into a decimal
def bin_dec():
    dec = 0
    if langue == "French":
        bin = input("Met le nombre binaire : ")
    else :
        bin = input("Put the binary number : ")
    # We define the power
    # On definit la puissance
    puis = len(bin) - 1
    # We go through each bit and multipli it by a power of 2
    # On part à travers chaque bit et on le multiplie part une puissance de 2
    for t in bin :
        bin = int(bin)
        # We give a small warning if the number isn't binary
        # On alert si le nombre n'est pas binaire
        if int(t) > 1 :
            print("Le nombre n'est pas binaire.")
        num = int(t)*2**puis
        dec += num
        puis -= 1
        bin = str(bin)
    print(dec)
# Conversion d'un nombre hexadécimal à la base 10
# Convertion of a hexadecimal into a decimal
def hex_dec():
    dec = 0
    sup = ("A","B","C","D","E","F")
    if langue == "French":
        hex = input("Met le nombre en base 16 : ")
    else :
        hex = input("Put the hexadecimal number : ")
    # We define the power
    # On définit la puissance
    puis = len(hex) - 1
    # We go throught each digit and multiply it by a power of 16
    # On part à travers chaque valeur et on le multiplie par une puissance de 16
    for t in hex :
        # If the digt is below nine we simply multiply it by a power of 16
        # Si le chiffre est inférieur à 9 on le multiplie simplement par une puissance de 16
        try :
            num = int(t)*16**puis
        # If the number is over 10 we convert it like we did previously
        # Si le chiffre est supérieur à 10 ont le convertit en décimal comme dans les codes précedents
        except :
            num = 0
            n = 0
            diz = 10
            while sup[n] != t :
                n += 1
                diz += n
            num = int(diz)*16**puis
        puis -= 1
        dec += num
    print(dec)
# Conversion d'un nombre binaire à un hexadécimale
# Convertion of a binary into an hexadecimal
def bin_hex():
    sup = ("F","E","D","C","B","A")
    hex = ""
    # Variable qui possède le nombre de bit
    # Variable that contains the amount of bits
    n_bit = 0
    if langue == "French":
        bin = input("Met le nombre binaire : ")
    else :
        bin = input("Put the binary number : ")
    for t in bin :
        n_bit += 1
    # Rajoute des 0 pour que nous puission regroupé les chiffres en groupe de 4 bits
    # Adds 0 so that we can group up the digits by 4 bits
    if n_bit % 4 != 0 :
        n_0 = 4 - n_bit % 4
        for i in range(n_0) :
            bin = "0" + bin
    # Nous convertissons en groupes de 4 bits
    # We convert by groups of 4 bits
    for t in range (0, len(bin), 4) :
        bits = bin[t : t+4]
        a, b, c, d = bits
        bin_temp = a + b + c + d
        dec = 0
        puis = len(bin_temp) - 1
        # On convertit le groupe de
        # We convert the group of 4 bits
        for t in bin_temp :
            # On envoi un message si le nombre n'est pas binaire
            # We send a message if the number isn't binary
            if int(t) > 1 :
                print("Le nombre n'est pas binaire.")
            num = int(t)*2**puis
            dec += num
            puis -= 1
            bin_temp = str(bin_temp)
        # On rajoute la valeur trouvée
        # We add the found value
        if dec < 10 :
            hex = hex + str(dec)
        else :
            let = 15 - dec
            hex = hex + sup[let]
    print(hex)
# Fonction qui gère le choix de convertion
# Foncion that deals with the conversion choice
def conv():
    if not lang_picked :
        lang_choice()
    if not conv_picked :
        conv_choice()
    quit_choice = input('press "Q" to quit')
    if quit_choice == "Q":
        quit()
    elif conve == '0':
        dec_bin()
    elif conve == '1':
        dec_hex()
    elif conve == '2':
        hex_bin()
    elif conve == '3':
        bin_dec()
    elif conve == '4':
        hex_dec()
    elif conve == '5':
        bin_hex()
    else :
        conv_choice()
while run == True :
    conv()
