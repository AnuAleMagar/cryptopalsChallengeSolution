## Understanding the Question 
original file --> repeating key XOR encrypted-->base64 encrypted--->present file(6.txt)
The original file has been repeatedly XORed and then base64 encoded.
# Goal
The goal is to find the original file

To achieve the goal we need to first find out the keySize
then find the key and at last decode base64 and do repeating XOR to decrypt the original file

## Understanding the hint:
1: keySize can be 2 to 40

2:def haming_distance(string1,string2) here we need to find out the hamming distance between two strings

3:for each keySize divide the 6.txt file into blocks of size keySize and compare each pair of blocks and find hamming distance,normalize it by dividing it by keySize,here take the average hamming distance

4:repeat step 3 for keySize range (2-40) and the keySize that generates the smallest hammingDistance is the actual keySize or length of the keysize

5:divide the 6.txt file into blocks of keySize length

6: Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.

7:Solve each block as if it was single-character XOR.

8:For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.

# Solution
```
import base64
with open('6.txt', 'r') as f:
    content = ''.join(f.read().split())

letters="etaoin srhldcmfu"
def findMostRepeatedKey(hexBytes):
    
    best_score = 0
    best_key = 0

    for i in range(256):  
        xored_bytes = bytes([byte ^ i for byte in hexBytes])
        try:
           
            ascii_result = xored_bytes.decode('ascii')
        except UnicodeDecodeError:
            continue  
        
        
        ascii_result2 = ascii_result.lower()
        count = 0
        
      
        for letter in letters:
            count += ascii_result2.count(letter)

        
        if len(ascii_result2) > 0: 
            countPer = (count / len(ascii_result2)) * 100

            
            if countPer > best_score:
                best_score = countPer
                best_key = i

    
    return best_key
# finding key
def fix_base64_padding(data):
    """Ensure Base64 string has proper padding."""
    while len(data) % 4 != 0:
        data += "="
    return data

content = base64.b64decode(fix_base64_padding(content))
def pad_blocks(block1, block2):
    len1, len2 = len(block1), len(block2)
    if len1 < len2:
        
        block1 += b'\x00' * (len2 - len1)
    elif len2 < len1:
       
        block2 += b'\x00' * (len1 - len2)
    return block1, block2

def hamming_distance(block1,block2):
    block1, block2 = pad_blocks(block1, block2)
    bin_str1 = ''.join(format(byte, '08b') for byte in block1)
    bin_str2 = ''.join(format(byte, '08b') for byte in block2)
    intger1=int(bin_str1,2)
    intger2=int(bin_str2,2)
    xor=intger1 ^ intger2
    binaryString=bin(xor)[2:]
    hamming_distance=0
    for char in binaryString:
        if char == "1":
            hamming_distance +=1
    
    return hamming_distance

def divides_into_blocks(content,keySize):
        blocks=[]
        for i in range(0,len(content),keySize):
            block=content[i:i+keySize]
            blocks.append(block)
        return blocks
totalHaming=[]
for keySize in range(2,41):
   blocks=divides_into_blocks(content,keySize)
   distance=0
   num_comp=0
   for i in range(len(blocks)-1):
        block1=blocks[i]
        block2=blocks[i+1]
        distance += hamming_distance(block1,block2)/keySize
        num_comp+=1
  
   hamming = distance / num_comp
   totalHaming.append(hamming)

smallest=min(totalHaming)

index=totalHaming.index(smallest)+2
keySize=index
ciphertext=divides_into_blocks(content,29)
# print(len(ciphertext[-1]))
ciphertext = [block + b'\x00' * (keySize - len(block)) for block in ciphertext] # here it makes all blocks of ciphertext to equal length
# print(len(ciphertext[-1])) 

newCipherText = []
# print("Hello")
for i in range(29):
    block = []
    for k in range(len(ciphertext)):
        block.append(ciphertext[k][i])
    newCipherText.append(bytes(block))

keys=''
for i  in range(len(newCipherText)):
   
    key=findMostRepeatedKey(newCipherText[i])
    keyy=chr(key)
    keys+=keyy
    
print("keys: ", keys)  
#  here now we get the keys  

# Now we will use that key and we will do repeating xor to get the originalFile


total_hex_result=''
lengthOfKeys=len(keys)
for i in range(len(content)):
    key=keys[i % lengthOfKeys]
    keyByte=(key.encode("ascii"))
    actualKey=int.from_bytes(keyByte,byteorder='big')
    resultInt=actualKey ^ content[i]
    hex_result=hex(resultInt)[2:].zfill(2)
    total_hex_result +=hex_result
solution=total_hex_result
originalFile = bytes.fromhex(total_hex_result).decode('ascii')
print("The original File:")
print(originalFile)


```
## Solution Description
Here, I loop through the range 2 to 40, and for each key size, I divide the content into blocks using divides_into_blocks and calculate the Hamming distance. I then return the minimum Hamming distance and its corresponding key size.

After identifying the key size, I divide the content of 6.txt into blocks of the identified key size. Next, I transpose these blocks and analyze each transposed block using single-byte XOR analysis over the range 0 to 255. I return the key that produces the best score based on English alphabet frequencies, as explained in Level 3.

I combine the keys from each block to create the actual key string. Finally, I use repeating XOR with this key string to decrypt the content, as described in Level 5.