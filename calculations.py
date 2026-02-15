# Imported from my cse lab 2 activity
# since we need a higher bit, float is not enough so we will use decimal
from decimal import Decimal, getcontext

def bintofloat(n, bit_type, Exp_end, Last, Subtrahend):
    #getting the sofx
    #variables
    S = 0; Exponent = n[1:Exp_end]; Mantissa = n[Exp_end:Last]
    Exp_bias = 0
    #lists for the bits
    E = []; M = []; Power_list = []; Value_list = []
    #getting ths sofx
    if n[0] == '1':
        S = 1

    else:
        S = 0
    print("S: ", S)

    #getting the exponent
    for i in range(len(Exponent)):
        if Exponent[i] == '1':
            E.append(1)
        else:
            E.append(0)
    print("E: ", E)

    #geting Mantissa
    for i in range(len(Mantissa)):
        if Mantissa[i] == '1':
            M.append(1)
        else:
            M.append(0)
    print("M: ", M)

    #for the ebias of e(x)
    for i, bit in enumerate(reversed(E)):
        if bit == 1:
            Exp_bias += 2**i
    print("Exponent bias: ", Exp_bias)

    #for the mantissa value
    for i, bit in enumerate(M):
        if bit == 1:
            Power_list.append("2^" + str (-(i + 1)))
            Value_list.append(2**(-1 * (i + 1)))

    print(f"Bit type: {bit_type}")
    #1st part of the calculation
    print(f"Value(x)= (-1)^{S} X 2^{Exp_bias} - {Subtrahend} X (1.{''.join(map(str, M))})")
    #2nd part of the calculation
    print(f"Value(x)= (-1)^{S} X 2^{Exp_bias} - {Subtrahend} X (1 + {' + '.join(map(str, Power_list))})")
    #3rd part of the calculation
    print(f"Value(x)= (-1)^{S} X 2^{Exp_bias} - {Subtrahend} X (1 + {' + '.join(map(str, Value_list))})")
    #4th part of the calculation
    print(f"Value(x)= (-1)^{S} X 2^{Exp_bias - Subtrahend} X (1 + {' + '.join(map(str, Value_list))})")
    #5th part of the calculation
    print(f"Value(x)= (-1)^{S} X {2**(Exp_bias - Subtrahend)} X ({1 + sum(Value_list)})")
    #the exiting part of the calculation
    print(f"Value(x)= {(-1)**S * (2**(Exp_bias - Subtrahend)) * (1 + sum(Value_list))}")
    print()
    final_value = (-1)**S * (2**(Exp_bias - Subtrahend)) * (1 + sum(Value_list))
    return final_value

def wholetoBinary(whole_number):
    #converting the whole number to binary
    whole_binary = []
    while whole_number > 0:
        whole_binary.append(str(whole_number % 2))
        whole_number = whole_number // 2
    whole_binary.reverse()
    return whole_binary

getcontext().prec = 60

def fractiontobit(Rounded_Fraction,limit):
    #converting the fraction number to binary
    fraction_binary = []  
    current_fraction = Decimal(str(Rounded_Fraction))
    for i in range(limit): #limit the length of the fraction binary to 52 bits 
        prod = current_fraction * 2
        if prod >= 1:
            fraction_binary.append('1')
            current_fraction = prod - 1
        else:#if less than 1 = 0 and remain the fraction
            fraction_binary.append('0')
            current_fraction = prod
    return ''.join(fraction_binary)

def floattobin(n, bit_type, subtrahend, limit, Elimit):
    #create type
    type = {}
    #dividing the whole number and the fraction number
    divided_number = n.split(".")
    whole_number = abs(int(divided_number[0]))
    fraction_number = int(divided_number[1])
    Rounded_Fraction = Decimal(abs(Decimal(n)))%1
    #calling methods to convert the whole number and the fraction number to binary
    whole_binary = wholetoBinary(whole_number)
    fraction_binary = fractiontobit(Rounded_Fraction, limit)
    S = 0
    if "-" in n:
        S = 1
    else:
        S = 0
    #lists
    value_list = [] ; power_list = []; normalized_list = []; result_list = 0
    #whole list
    combined_list = whole_binary + list(fraction_binary); divided = len(whole_binary)
     #msb
    most_significant_bit = combined_list.index('1')#the index of the 1st 1 will always be the msb
    exponent_value = (divided - 1) - most_significant_bit #the exponent value is the distance between the msb and the whole part
    for i, bit in enumerate(combined_list):
        if bit == '1':
            if i < divided:#i will always be less than the divided number for the whole part, so we can just use i to calculate the power of 2
                power_list.append("2^" + str (divided - 1 - i))
                value_list.append( 2**(divided - 1  - i))
                p = divided - 1 - i
            else: # the negative side
                power_list.append("2^" + str (-(i - divided + 1)))
                value_list.append(2**(-(i - divided + 1)))
                p = -(i - divided + 1)

        
            if i == most_significant_bit:
                normalized_list.append('1')
            else: # the negative side
                normalized_list.append("2^" + str (p) + "-" + str(exponent_value))
                result_list += Decimal('2') ** Decimal(p - exponent_value)
 
   #calcu for M
    M = fractiontobit(result_list, 128)
    E = wholetoBinary(exponent_value + subtrahend)
    E_str = ''.join(E).zfill(Elimit)
    #outputs
    print(f"Value for ({bit_type}) : {n} ")
    print(f"Value(x)= (-1)^{S} X ({' + '.join(map(str,value_list))})")#step 1
    print(f"Value(x)= (-1)^{S} X ({' + '.join(map(str,power_list))})")#step 2
    print(f"Exponent value: {exponent_value}")
    print(f"Value(x)= (-1)^{S} X 2^{exponent_value} X ({' + '.join(map(str,normalized_list))})")#step 3
    print(f"Value(x)= {(-1)**S} X 2^ {subtrahend + exponent_value} - {subtrahend} * (1 + {''.join(M[:limit])})")#step 4
    print(f"S(x) : {S}\nE(x) :{subtrahend + exponent_value} : {E_str}\nM(x) : {''.join(M[:limit])}")#step 5
    print(f"Value(x) = {S}{E_str}{''.join(M[:limit])}")#step 6
    print()
    M_part = ''.join(M[:limit])
    final_binary = str(S) + E_str + M_part
    return final_binary

#for float to binary
def twentyfourbits(n): return floattobin(n, "24", 127, 20, 8)
def doubleprecision(n): return floattobin(n, "64", 1023, 52, 11)
def quadprecision(n): return floattobin(n, "128", 16383, 112, 15)
#binary to float
def twentyfbits(n): return bintofloat(n, "24", 9, 24, 127)
def sixtyfourbits(n): return bintofloat(n, "64", 12, 64, 1023)
def onetwoeitybits(n): return bintofloat(n, "128", 16, 128, 16383)


#userinput = str(input("Enter a Decimal/Binary: "))

#try :
    #if "." in userinput:
        #use the float to bin method
        #twentyfourbits(userinput)
        #doubleprecision(userinput)
        #quadprecision(userinput)
    #else:
        #use the float to bin method
        #twentyfbits(userinput)
        #sixtyfourbits(userinput)
        #onetwoeitybits(userinput)
#except:
    #print("invalid input")