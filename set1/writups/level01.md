# Goal- Convert Hex to Base64

## What is Hex?
-A system for representing numbers that uses 16 symbols: 0-9 and A-F. Here, A represents 10, B represents 11, and so on, up to F, which represents 15 in decimal.
-typically represented by the prefix 0x at the beginning of the code.

## Why Use Hex Instead of Decimal?

At the lowest level, the only code system that a computer truly understands is binary—sequences of 0s and 1s, where 0 represents a circuit that is "off" and 1 represents a circuit that is "on." However, representing larger numbers directly in binary can be cumbersome.

To understand why hex is useful, consider how we represent numbers in binary. Three bits can represent only 8 values (from 0 to 7), which isn't enough to cover a full set of decimal digits. By using 4 bits, we can represent 16 values (from 0 to 15), aligning perfectly with hexadecimal's 16 symbols. This makes hex ideal for compactly representing binary data.

Using hex also simplifies binary representation by allowing us to represent one byte (8 bits) as two hex digits. 
eg - 00001010 = 0x0A here we can easily convert 1 byte to hexcode,making it more compact version to represent numbers in human readable format.

-I'm sure there are lot more reasons behind this:)






## What is Base64?


-A number system that represents binary numbers into text that uses 6 bit to represent a character making 64 unique printable characters.The characters are(0-9,A-Z,a-z,+,/) and '=' is used for padding

Base64 encoding takes 24bit sequences making it 3byte input length or multiple of 3byte that produce 4 or multiple of 4 length base64 characters

If input is one byte then it adds 2 padding characters to make 4length output

Ex Ascii character A ->QQ== 

if input is 2 byte it adds 1 padding 

Ex Ap ->QXA=

And if it's 3 byte and no padding is added

ex App ->QXBw

for more that 3 bytes first it is grouped into sequences of 3 3 bytes and then padding added if necessary

ex App i ->QXBwIGK= (here QXBw is the Base64 for App and IGk= is the Base64 for i (with one padding character added))

## What is padding?
Adding extra bit in the sequence that has no impact in the input.It is done because 
the input bit is always not exactly the multiple of 6bits so to make it perfectly multiple of 6bits,it is padded.



## How to Convert to in python?
## Solutions
```
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

```
## Solutions Overview
Here main target is to encode hex string to base64.I used to base64 liabrary to encode the input.
string.base64.b64encode(),here the correct format for input is bytearray,so we need to convert hex string to byte array.For this I first convert the hex string to binary using zfill(4),it will convert each character exactly to 4 bits.And I made the input bit exactly multiple of 8 and used integer_value.to_bytes(length,byteorder='big') to convert it to the byteobject.

### We can also use bytes.fromhex(hex_string) directly to convert it to base64.
```
import base64
hex_string='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
hex_bytes=bytes.fromhex(hex_string)
basesixty4=base64.b64encode(hex_bytes)
print(basesixty4)

```
