from decimal import Decimal
from calculations import *

hours = 20
val_24 = twentyfourbits('0.1')#we convert 0.1 to binary
bin_24 = twentyfbits(val_24)#we convert the 24-bit binary representation of 
#0.1 back to decimal to calculate the drift later on, we use the 
# 24-bit binary representation as the input for this function 
# because we want to see how much drift we get from using a 
# 24-bit representation of 0.1 compared to the target value of 0.1

#for the 64bit simulation
val_64 = doubleprecision('0.1')
bin_64 = sixtyfourbits(val_64)
#drift calculation
target = Decimal('0.1')#the target value we want to reach, which is 0.1 in this case, we will compare the binary representation of 0.1 in 24-bit and 64-bit to this target value to calculate the drift
total_ticks = hours * 3600 * 10 #Multiplying by 3,600 converts the Hours to seconds * 10 because 10 ticks per second

drift_24 = abs(target - Decimal(str(bin_24))) * total_ticks
drift_64 = abs(target - Decimal(str(bin_64))) * total_ticks

print(f"Drift for 24-bit representation: {drift_24} seconds")
print(f"Drift for 64-bit representation: {drift_64} seconds")
print(f"{val_24} in 24-bit representation")
print(f"{val_64} in 64-bit representation")
print(f"Decimal value of 24-bit binary: {Decimal(str(bin_24))}")
print(f"Decimal value of 64-bit binary: {Decimal(str(bin_64))}")
print(f"{target} is the target value we want to reach, which is 0.1 in this case")
print(f"{target - Decimal(str(bin_24))} 24 bit")
print(f"{target - Decimal(str(bin_64))} 64 bit")
