from level03 import findMostRepeatedKey
f = open('4.txt', 'r')
content=f.readlines()
letters="etaoin srhldcmfu"
for line in content:
    bytess = bytes.fromhex(line)
    key=findMostRepeatedKey(bytess)
    if key is None:
     continue
    else:
     xored_result = bytes([byte ^ key for byte in bytess])
     ascii_result = xored_result.decode('ascii')
     print(line)
     print(ascii_result)
f.close()