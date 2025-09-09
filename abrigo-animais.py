# ============FUNCOES===========
def procREX():
    cod = 1
    brinquedo1 = BrinqP1.find("RATO")
    brinquedo2 = BrinqP1.find("BOLA")
    brinquedo3 = BrinqP2.find("RATO")
    brinquedo4 = BrinqP2.find("BOLA")
    animal = Animal.find("REX")

    if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)) and ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0))):
        print("Rex - Abrigo")

    else:
        if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)):
            print("Rex - pessoa 1")
        if ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0)):
            print("Rex - pessoa 2")
# =================================================


def procMIMI():  # GATO
    cod = 2
    tipoanimal = "GATO"
    brinquedo1 = BrinqP1.find("BOLA")
    brinquedo2 = BrinqP1.find("LASER")
    brinquedo3 = BrinqP2.find("BOLA")
    brinquedo4 = BrinqP2.find("LASER")
    animal = Animal.find("MIMI")

    if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)) and ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0))):
        print("Mimi - Abrigo")

    else:
        if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)):
            print("Mimi - pessoa 1")

        if ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0)):
            print("Mimi - pessoa 2")

# =====================================================


def procFOFO():  # GATO
    cod = 3
    tipoanimal = "GATO"
    brinquedo1 = BrinqP1.find("BOLA")
    brinquedo2 = BrinqP1.find("RATO")
    brinquedo3 = BrinqP1.find("LASER")
    brinquedo4 = BrinqP2.find("BOLA")
    brinquedo5 = BrinqP2.find("RATO")
    brinquedo6 = BrinqP2.find("LASER")
    animal = Animal.find("FOFO")

    if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo3 >= 0) and (brinquedo1 < brinquedo2) and (brinquedo2 < brinquedo3) and (animal >= 0)) and ((brinquedo4 >= 0) and (brinquedo5 >= 0) and (brinquedo6 >= 0) and (brinquedo4 < brinquedo5) and (brinquedo5 < brinquedo6) and (animal >= 0))):
        print("Fofo - Abrigo")

    else:
        if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo3 >= 0) and (brinquedo1 < brinquedo2) and (brinquedo2 < brinquedo3) and (animal >= 0)):
            print("Fofo - pessoa 1")
        if ((brinquedo4 >= 0) and (brinquedo5 >= 0) and (brinquedo6 >= 0) and (brinquedo4 < brinquedo5) and (brinquedo5 < brinquedo6) and (animal >= 0)):
            print("Fofo - pessoa 2")
# ====================================================


def procZERO():  # GATO
    cod = 4
    tipoanimal = "GATO"
    brinquedo1 = BrinqP1.find("RATO")
    brinquedo2 = BrinqP1.find("BOLA")
    brinquedo3 = BrinqP2.find("RATO")
    brinquedo4 = BrinqP2.find("BOLA")
    animal = Animal.find("ZERO")

    if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)) and ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0))):
        print("Zero - Abrigo")

    else:
        if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)):
            print("Zero - pessoa 1")

        if ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0)):
            print("Zero - pessoa 2")

# =====================================================


def procBOLA():
    cod = 5
    brinquedo1 = BrinqP1.find("CAIXA")
    brinquedo2 = BrinqP1.find("NOVELO")
    brinquedo3 = BrinqP2.find("CAIXA")
    brinquedo4 = BrinqP2.find("NOVELO")
    animal = Animal.find("BOLA")

    if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)) and ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0))):
        print("Bola - Abrigo")

    else:
        if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)):
            print("Bola - pessoa 1")
        if ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0)):
            print("Bola - pessoa 2")
# ======================================================


def procBEBE():
    cod = 6
    brinquedo1 = BrinqP1.find("LASER")
    brinquedo2 = BrinqP1.find("RATO")
    brinquedo3 = BrinqP1.find("BOLA")
    brinquedo4 = BrinqP2.find("LASER")
    brinquedo5 = BrinqP2.find("RATO")
    brinquedo6 = BrinqP2.find("BOLA")
    animal = Animal.find("BEBE")

    if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo3 >= 0) and (brinquedo1 < brinquedo2) and (brinquedo2 < brinquedo3) and (animal >= 0)) and ((brinquedo4 >= 0) and (brinquedo5 >= 0) and (brinquedo6 >= 0) and (brinquedo4 < brinquedo5) and (brinquedo5 < brinquedo6) and (animal >= 0))):
        print("Bebe - Abrigo")

    else:
        if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo3 >= 0) and (brinquedo1 < brinquedo2) and (brinquedo2 < brinquedo3) and (animal >= 0)):
            print("Bebe - pessoa 1")
        if ((brinquedo4 >= 0) and (brinquedo5 >= 0) and (brinquedo6 >= 0) and (brinquedo4 < brinquedo5) and (brinquedo5 < brinquedo6) and (animal >= 0)):
            print("Bebe - pessoa 2")
# ======================================================


def procLOCO():
    cod = 7
    brinquedo1 = BrinqP1.find("SKATE")
    brinquedo2 = BrinqP1.find("RATO")
    brinquedo3 = BrinqP2.find("SKATE")
    brinquedo4 = BrinqP2.find("RATO")
    animal = Animal.find("LOCO")

    if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)) and ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0))):
        print("Loco - Abrigo")

    else:
        if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)):
            print("Loco - pessoa 1")
        if ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0)):
            print("Loco - pessoa 2")


def ALLexecute():
    procREX()
    procMIMI()  # gato
    procFOFO()  # gato
    procZERO()  # gato
    procBOLA()
    procBEBE()
    procLOCO()  # jabuti


# ==============================
# DECLARACAO DE VARIAVEIS GLOBAIS=====
contagem = 1
MIMI = "GATO"
FOFO = "GATO"
ZERO = "GATO"
animalvalido = ["REX", "MIMI", "FOFO", "ZERO", "BOLA", "BEBE", "LOCO"]
brinquedovalido = ["RATO", "BOLA", "LASER", "CAIXA", "NOVELO", "SKATE"]
countP1 = 0
countP2 = 0
# ======================================
while contagem < 7:
    print("Os animais que estao pra adocao sao: ", animalvalido)
    print("Primeira Pessoa...")
    BrinqP1 = input("Digite seus brinquedos: ")
    BrinqP1 = BrinqP1.upper()
    BrinqP1 = (BrinqP1.replace(" ", ","))
    count1 = len(BrinqP1)
    print(BrinqP1)
    contRATO = BrinqP1.count("RATO")
    contBOLA = BrinqP1.count("BOLA")
    contLASER = BrinqP1.count("LASER")
    contCAIXA = BrinqP1.count("CAIXA")
    contNOVELO = BrinqP1.count("NOVELO")
    contSKATE = BrinqP1.count("SKATE")

    print("Segunda Pessoa...")
    BrinqP2 = input("Digite seus brinquedos: ")
    BrinqP2 = BrinqP2.upper()
    BrinqP2 = (BrinqP2.replace(" ", ","))
    count2 = len(BrinqP2)
    print(BrinqP2)
    contRATO2 = BrinqP2.count("RATO")
    contBOLA2 = BrinqP2.count("BOLA")
    contLASER2 = BrinqP2.count("LASER")
    contCAIXA2 = BrinqP2.count("CAIXA")
    contNOVELO2 = BrinqP2.count("NOVELO")
    contSKATE2 = BrinqP2.count("SKATE")

    # DIGITAR OS ANIMAIS A SEREM ESCOLHIDOS
    Animal = input("Digite os animais: ")
    Animal = Animal.upper()
    Animal = (Animal.replace(" ", ","))
    print(Animal)
    print(contRATO)
    # codigo principal===============  ZERO  ==================================

    if (Animal.find("ZERO") != -1) and ((BrinqP1.find("RATO") != -1) and ((BrinqP1.find("BOLA") != -1))) or (Animal.find("ZERO") != -1) and ((BrinqP2.find("RATO") != -1) and ((BrinqP2.find("BOLA") != -1))):

        brinquedo1 = BrinqP1.find("RATO")
        brinquedo2 = BrinqP1.find("BOLA")
        brinquedo3 = BrinqP2.find("RATO")
        brinquedo4 = BrinqP2.find("BOLA")
        animal = Animal.find("ZERO")

        if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)) and ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0))):
            print("Zero - Abrigo")

        else:
            if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)):
                print("Zero - pessoa 1")
                animalvalido.remove("ZERO")
                countP1 += 1
            if ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0)):
                print("Zero - pessoa 2")
                countP2 += 1
                animalvalido.remove("ZERO")
        # ===============================    MIMI    ============================================
    elif (Animal.find("MIMI") != -1) and ((BrinqP1.find("BOLA") != -1) and ((BrinqP1.find("LASER") != -1))) or (Animal.find("MIMI") != -1) and ((BrinqP2.find("BOLA") != -1) and ((BrinqP2.find("LASER") != -1))):
        brinquedo1 = BrinqP1.find("BOLA")
        brinquedo2 = BrinqP1.find("LASER")
        brinquedo3 = BrinqP2.find("BOLA")
        brinquedo4 = BrinqP2.find("LASER")
        animal = Animal.find("MIMI")

        if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)) and ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0))):
            print("Mimi - Abrigo")

        else:
            if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)):
                print("Mimi - pessoa 1")
                animalvalido.remove("MIMI")
            if ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0)):
                print("Mimi - pessoa 2")
                animalvalido.remove("MIMI")
        # ==============================    FOFO    =============================================
    elif ((Animal.find("FOFO") != -1) and (BrinqP1.find("BOLA") != -1) and (BrinqP1.find("RATO") != -1) and (BrinqP1.find("LASER") != -1)) or ((Animal.find("FOFO") != -1) and (BrinqP2.find("BOLA") != -1) and (BrinqP2.find("RATO") != -1) and (BrinqP2.find("LASER") != -1)):
        brinquedo1 = BrinqP1.find("BOLA")
        brinquedo2 = BrinqP1.find("RATO")
        brinquedo3 = BrinqP1.find("LASER")
        brinquedo4 = BrinqP2.find("BOLA")
        brinquedo5 = BrinqP2.find("RATO")
        brinquedo6 = BrinqP2.find("LASER")
        animal = Animal.find("FOFO")

        if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo3 >= 0) and (brinquedo1 < brinquedo2) and (brinquedo2 < brinquedo3) and (animal >= 0)) and ((brinquedo4 >= 0) and (brinquedo5 >= 0) and (brinquedo6 >= 0) and (brinquedo4 < brinquedo5) and (brinquedo5 < brinquedo6) and (animal >= 0))):
            print("Fofo - Abrigo")

        else:
            if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo3 >= 0) and (brinquedo1 < brinquedo2) and (brinquedo2 < brinquedo3) and (animal >= 0)):
                print("Fofo - pessoa 1")
                animalvalido.remove("FOFO")
            if ((brinquedo4 >= 0) and (brinquedo5 >= 0) and (brinquedo6 >= 0) and (brinquedo4 < brinquedo5) and (brinquedo5 < brinquedo6) and (animal >= 0)):
                print("Fofo - pessoa 2")
                animalvalido.remove("FOFO")
        # ==============================   REX      =========================================================
    if (Animal.find("REX") != -1) and ((BrinqP1.find("RATO") != -1) and ((BrinqP1.find("BOLA") != -1))) or (Animal.find("REX") != -1) and ((BrinqP2.find("RATO") != -1) and ((BrinqP2.find("BOLA") != -1))):
        brinquedo1 = BrinqP1.find("RATO")
        brinquedo2 = BrinqP1.find("BOLA")
        brinquedo3 = BrinqP2.find("RATO")
        brinquedo4 = BrinqP2.find("BOLA")
        animal = Animal.find("REX")

        if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)) and ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0))):
            print("Rex - Abrigo")

        else:
            if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)):
                print("Rex - pessoa 1")
                animalvalido.remove("REX")
            if ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0)):
                print("Rex - pessoa 2")
                animalvalido.remove("REX")
        # =============================    BOLA     ==========================================================
    if (Animal.find("BOLA") != -1) and ((BrinqP1.find("CAIXA") != -1) and ((BrinqP1.find("NOVELO") != -1))) or (Animal.find("BOLA") != -1) and ((BrinqP2.find("CAIXA") != -1) and ((BrinqP2.find("NOVELO") != -1))):
        brinquedo1 = BrinqP1.find("CAIXA")
        brinquedo2 = BrinqP1.find("NOVELO")
        brinquedo3 = BrinqP2.find("CAIXA")
        brinquedo4 = BrinqP2.find("NOVELO")
        animal = Animal.find("BOLA")

        if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)) and ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0))):
            print("Bola - Abrigo")

        else:
            if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)):
                print("Bola - pessoa 1")
                animalvalido.remove("BOLA")
            if ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0)):
                print("Bola - pessoa 2")
                animalvalido.remove("BOLA")
        # =============================    BEBE     ==========================================================
    if ((Animal.find("BEBE") != -1) and (BrinqP1.find("LASER") != -1) and (BrinqP1.find("RATO") != -1) and (BrinqP1.find("BOLA") != -1)) or ((Animal.find("BEBE") != -1) and (BrinqP2.find("LASER") != -1) and (BrinqP2.find("RATO") != -1) and (BrinqP2.find("BOLA") != -1)):
        brinquedo1 = BrinqP1.find("LASER")
        brinquedo2 = BrinqP1.find("RATO")
        brinquedo3 = BrinqP1.find("BOLA")
        brinquedo4 = BrinqP2.find("LASER")
        brinquedo5 = BrinqP2.find("RATO")
        brinquedo6 = BrinqP2.find("BOLA")
        animal = Animal.find("BEBE")

        if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo3 >= 0) and (brinquedo1 < brinquedo2) and (brinquedo2 < brinquedo3) and (animal >= 0)) and ((brinquedo4 >= 0) and (brinquedo5 >= 0) and (brinquedo6 >= 0) and (brinquedo4 < brinquedo5) and (brinquedo5 < brinquedo6) and (animal >= 0))):
            print("Bebe - Abrigo")

        else:
            if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo3 >= 0) and (brinquedo1 < brinquedo2) and (brinquedo2 < brinquedo3) and (animal >= 0)):
                print("Bebe - pessoa 1")
                animalvalido.remove("BEBE")
            if ((brinquedo4 >= 0) and (brinquedo5 >= 0) and (brinquedo6 >= 0) and (brinquedo4 < brinquedo5) and (brinquedo5 < brinquedo6) and (animal >= 0)):
                print("Bebe - pessoa 2")
                animalvalido.remove("BEBE")
        # ============================     LOCO     ===========================================================
    if (Animal.find("LOCO") != -1) and ((BrinqP1.find("SKATE") != -1) and ((BrinqP1.find("RATO") != -1))) or (Animal.find("LOCO") != -1) and ((BrinqP2.find("SKATE") != -1) and ((BrinqP2.find("RATO") != -1))):
        brinquedo1 = BrinqP1.find("SKATE")
        brinquedo2 = BrinqP1.find("RATO")
        brinquedo3 = BrinqP2.find("SKATE")
        brinquedo4 = BrinqP2.find("RATO")
        animal = Animal.find("LOCO")

        if (((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)) and ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0))):
            print("Loco - Abrigo")

        else:
            if ((brinquedo1 >= 0) and (brinquedo2 >= 0) and (brinquedo1 < brinquedo2) and (animal >= 0)):
                print("Loco - pessoa 1")
                animalvalido.remove("LOCO")
            if ((brinquedo3 >= 0) and (brinquedo4 >= 0) and (brinquedo3 < brinquedo4) and (animal >= 0)):
                print("Loco - pessoa 2")
                animalvalido.remove("LOCO")

# =======================================================================================
    contagem += 1
    print(animalvalido)
    print(contagem)
#####################################
