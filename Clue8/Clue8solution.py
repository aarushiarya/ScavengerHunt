# Python program to implement morse code Decoder

# Dictionary representing the morse code to english chart 
MORSE_CODE_DICT = { '.-':'A', '-...':'B', 
                    '-.-.':'C', '-..':'D', '.':'E', 
                    '..-.':'F', '--.':'G', '....':'H', 
                    '..':'I', '.---':'J', '-.-':'K', 
                    '.-..':'L', '--':'M', '-.':'N', 
                    '---':'O', '.--.':'P', '--.-':'Q', 
                    '.-.':'R', '...':'S', '-':'T', 
                    '..-':'U', '...-':'V', '.--':'W', 
                    '-..-':'X', '-.--':'Y', '--..':'Z'} 

# Decrypt the string from reverse alphabets

message = '.-- --- -- .- -. .-- .... --- .--. ..- - -- .- -. --- -. -- --- --- -. '

citext = ''
decoded_string = '' 

for letter in message:
    # check for space
    if (letter != ' '):
        # counter to keep track of space
        i=0
        # store morse code of a single character
        citext = citext + letter
    else:
    # if it is a space
        # if i=1 indicate new character
        i+=1
        # if i=2 indicate new word
        if i == 2:
            # add space to separate words
            decoded_string = decoded_string +' '
        else:
            # decode using dictionary
            if citext in MORSE_CODE_DICT:
                decoded_string = decoded_string+ MORSE_CODE_DICT.get(citext)
                citext=''
           
# print decoded string 
print decoded_string
