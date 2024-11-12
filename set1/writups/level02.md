# Goal- Write a function that takes two equal-length buffers and produces their XOR combination.


If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179

## What is xor? 
 XOR also exclusive or is the logical operator,compares two input bits,and output is true when exactly one of the input bit is true.it is false when both input bits are true or both false.

 A XOR 0 = A 
 
 A XOR A = 0
 
 A XOR B XOR B = A [cuz B XOR B = 0] and [A XOR 0 = A]
 here we can treat B as a key and message A so when encoding message A we XOR against B and when we XOR again the result will be A.

 In cryptography, XOR is simple symmetric encryption method
 ## Solution
  ```
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
  ```
## Explaination
 Here first i convert both hex strings to equal length binary strings.And define a function which equalize the length if they are not equal and then they are XORED.The resultant value is interger so they are again converted to hex.
