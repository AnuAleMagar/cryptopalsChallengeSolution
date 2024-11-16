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
if __name__ == "__main__":
 key=findMostRepeatedKey(hexBytes)
 if key is None:
    print("Key not found")
 else:
    xored_result = bytes([byte ^ key for byte in hexBytes])
    ascii_result = xored_result.decode('ascii')
    print(ascii_result)
