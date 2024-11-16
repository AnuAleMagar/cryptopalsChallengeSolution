# Goal Single-byte XOR cipher
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

## Solution
```
hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
hexBytes = bytes.fromhex(hex_string)

letters="etaoin srhldcmfu"
def findMostRepeatedKey(hexBytes):
    for i in range(256):
      xored_bytes = bytes([byte ^ i for byte in hexBytes])
      try:
            ascii_result = xored_bytes.decode('ascii')  
      except UnicodeDecodeError:
            continue 
      ascii_result2=ascii_result.lower()
      count=0
      for letter in letters:
         count+=ascii_result2.count(letter)
      if count !=0:
        countPer=(count/len(ascii_result2))*100
        if countPer >62 and countPer<85:
         return i
    return None
key=findMostRepeatedKey(hexBytes)
if key is None:
   print("Key not found")
else:
   xored_result = bytes([byte ^ key for byte in hexBytes])
   ascii_result = xored_result.decode('ascii')
   print(ascii_result)

```
### Description
Here, I define a function that takes the hex_string. I also set a string called letters that includes the most common letters in sentences, including the space character. First, I convert the hex string to bytes and then iterate through a loop up to 255. For each i, I XOR the bytes with i. If i results in a non-printable character, it will throw an error, so I have used a try-except block and then convert the result into ASCII characters. After that, I convert it to lowercase. I then use the count() function to find the frequency of each of the most common letters and sum the frequencies. If the repetition percentage is between 62% and 84%, I return the key.