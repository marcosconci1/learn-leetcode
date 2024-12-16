strs = ["neet","code","love","you"]

def encode(strs):
    """Encodes a list of strings to a single string."""
    
    encoded = ""
    for i in range(len(strs)):
        encoded += f"{len(strs[i])}#{strs[i]}"
    
    return encoded

def decode(encoded):
    """Decodes a single string to a list of strings."""
    
    decoded = []  

    while encoded:
    
        delimiter_index = encoded.find('#')
        
        length = int(encoded[:delimiter_index])

        start_index = delimiter_index + 1
        substring = encoded[start_index:start_index + length]

        decoded.append(substring)

        encoded = encoded[start_index + length:]
        
    return decoded

print(decode(encode(strs)))