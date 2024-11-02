import base64
inputString="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
binary_result=''
for char in inputString:
    integer_value=int(char,16)
    binary_result+=bin(integer_value)[2:].zfill(4)

def binary_to_base64(binary_result):
    if len(binary_result)%8 !=0:
        binary_result=binary_result.zfill(len(binary_result)+(8-len(binary_result)%8))
    integer_value=int(binary_result,2)
    length=len(binary_result)//8
    bytearray=integer_value.to_bytes(length,byteorder='big')
    bas=base64.b64encode(bytearray)
    return bas

print(binary_to_base64(binary_result))
