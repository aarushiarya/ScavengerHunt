```python

# Python program to implement Reverse Alphabet Decoder 
  
''' 
VARIABLE 
'decoded_string' -> 'stores the decoded string' 
'message' -> 'stores the string to be encoded or decoded' 
'''
  
# Dictionary representing the reverse alphabet chart 
REVERSE_ALPHABET_CODE_DICT = { 'A':'Z', 'B':'Y', 
                    'C':'X', 'D':'W', 'E':'V', 
                    'F':'U', 'G':'T', 'H':'S', 
                    'I':'R', 'J':'Q', 'K':'P', 
                    'L':'O', 'M':'N', 'N':'M', 
                    'O':'L', 'P':'K', 'Q':'J', 
                    'R':'I', 'S':'H', 'T':'G', 
                    'U':'F', 'V':'E', 'W':'D', 
                    'X':'C', 'Y':'B', 'Z':'A'} 

# Decrypt the string from reverse alphabets

message = 'URIHGDLNZMGLDRMGSVZ.N.GFIRMTZDZIWULIXLNKFGRMT'

decoded_string = '' 

for letter in message:
   # print letter
   if letter in REVERSE_ALPHABET_CODE_DICT:
       decoded_string+= REVERSE_ALPHABET_CODE_DICT.get(letter)
  
print decoded_string
```
