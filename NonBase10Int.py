class NonBase10Int:
    def __init__(self, string, base):
        self.__rootNum = string
        self.__base = base
        sums = []
        currentExp = 0
        if base <= 10:
            for i in range(len(string) - 1, -1, -1):
                sums.append(int(string[i]) * (base ** currentExp))
                currentExp += 1
        elif base == 16:
            for i in range(len(string) - 1, -1, -1):
                if not string[i].isdigit():
                    if string[i].lower() == 'a':
                        currentNum = 10
                    elif string[i].lower() == 'b':
                        currentNum = 11
                    elif string[i].lower() == 'c':
                        currentNum = 12
                    elif string[i].lower() == 'd':
                        currentNum = 13
                    elif string[i].lower() == 'e':
                        currentNum = 14
                    elif string[i].lower() == 'f':
                        currentNum = 15
                else:
                    currentNum = int(string[i])
                sums.append(currentNum * (base ** currentExp))
                currentExp += 1
        self.__base10 = sum(sums)
        
    def convert(self, base):
        if base <= 10:
            remainders = []
            quotient = self.__base10
            while True:
                remainders.append(quotient % base)
                quotient //= base
                if quotient == 0:
                    break
            string = ''
            for i in range(len(remainders) - 1, -1, -1):
                string += str(remainders[i])
            return string
        
        # base 16 - funky letters
        elif base == 16:
            remainders = []
            quotient = self.__base10
            while True:
                remainders.append(quotient % base)
                quotient //= base
                if quotient == 0:
                    break
            string = ''
            for i in range(len(remainders) - 1, -1, -1):
                if remainders[i] == 10:
                    remainders[i] = 'a'
                elif remainders[i] == 11:
                    remainders[i] = 'b'
                elif remainders[i] == 12:
                    remainders[i] = 'c'
                elif remainders[i] == 13:
                    remainders[i] = 'd'
                elif remainders[i] == 14:
                    remainders[i] = 'e'
                elif remainders[i] == 15:
                    remainders[i] = 'f'
                else:
                    remainders[i] = str(remainders[i])
                string += remainders[i]
            return string
        
    # overrides
    def __str__(self):
        return self.__rootNum
    
    # getters
    def getBase10(self):
        return self.__base10