# Goal - Detect single-character XOR
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)

## Solution
```
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
```

### Description
In this solution, I imported the findMostRepeatedKey function from level03 and read the file line by line. For each line, I used the function to find the most repeated key, then decoded it into an ASCII string.