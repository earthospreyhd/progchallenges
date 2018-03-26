key = "lemonz";

input = "zachismyname";


def vig (status, key, input):

    output = [None] * len(input);

    for x in range(0,len(input)):
    
        index = x % len(key);
    
        offset = ord(key[index]) - 97;
    
        output[x] = chr((((ord(input[x]) + offset*status) - 97) % 26) + 97);
    
    return (output);

#call function with 1 to encrypt and -1 to decrypt

encrypt = vig(1, key, input);

decrypt = vig(-1, key, encrypt);

print (encrypt);

print (decrypt);
