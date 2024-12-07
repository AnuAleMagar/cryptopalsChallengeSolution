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


    