ascii_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal" 
bytes_result = ascii_string.encode("ascii") 
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


