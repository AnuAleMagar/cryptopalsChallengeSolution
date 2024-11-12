string1="1c0111001f010100061a024b53535009181c"
string2="686974207468652062756c6c277320657965"
binary_string2=''
binary_string1=''
for char in string1:
         integer_value=int(char,16)
         binary_string1+=bin(integer_value)[2:].zfill(4)
for char in string2:
         integer_value=int(char,16)
         binary_string2+=bin(integer_value)[2:].zfill(4)
     
def fixedXor(binary_string1,binary_string2):
         if len(binary_string2) > len(binary_string1):
             binary_string1=binary_string1.zfill(len(binary_string2))
         else:
           binary_string2=binary_string2.zfill(len(binary_string1))
         xorrr=int(binary_string1,2) ^ int(binary_string2,2)
         xor_solution=hex(xorrr)[2:]
         return xor_solution
print(fixedXor(binary_string1,binary_string2)) 