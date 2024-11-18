# Goal -Implement repeating-key XOR
Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

## Solution
```
ascii_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal" 
bytes_result = ascii_string.encode("ascii") 
length=len(bytes_result)
keys="ICE"
total_hex_result=''
lengthOfKeys=len(keys)
for i in range(len(bytes_result)):
    key=keys[i % lengthOfKeys]
    keyByte=(key.encode("ascii"))
    actualKey=int.from_bytes(keyByte,byteorder='big')
    resultInt=actualKey ^ bytes_result[i]
    hex_result=hex(resultInt)[2:].zfill(2)
    total_hex_result +=hex_result
solution=total_hex_result
print(solution)
```
## Solution Description

First, I convert the ascii_string into a bytes object. The key provided is "ICE". I initialize total_hex_result as an empty string and measure the length of the key.

Next, I run a loop that iterates from 0 to the length of the input string. In each iteration, the key is selected using the expression key = keys[i % lengthOfKeys]. This ensures that the key repeats in the sequence: first 'I', then 'C', then 'E', and then back to 'I', continuing in this cycle.

For each character in the input string, I convert both the key and the current byte of the string into integers. Then, I apply the XOR operation between the key and the byte. Since the result of the XOR is an integer, I convert it back to its hexadecimal form. Finally, I concatenate the hexadecimal result to total_hex_result.
   