def is_unique(string):
    chars = set()
    for char in string:
        if char in chars:
            return False
        chars.add(char)
    return True

def is_unique2(string):
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True

def is_permutation(string1, string2):
    chars1 = {}
    for char in string1:
        if char in chars1:
            chars1[char] += 1
        else:
            chars1[char] = 1

    chars2 = {}
    for char in string2:
        if char in chars2:
            chars2[char] += 1
        else:
            chars2[char] = 1

    for char in chars1:
        if chars1[char] != chars2.get(char):
            return False
    return True

#tacocat
#TactCoca
def is_palindrome_permutation(string):
    chars = {}

    for char in string:
        if char == ' ':
            continue

        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    has_odd_count = False
    for char in chars:
        if chars[char] % 2 != 0:
            if has_odd_count:
                return False
            has_odd_count = True

    return True

    #pale
    #pales
def one_away(string1, string2):
    if abs(len(string1) - len(string2)) > 1: 
        return False

    i, j = 0, 0
    is_edit_used = False
    while i < len(string1) and j < len(string2):
        print(string1[i], string2[j])
        if string1[i] != string2[j]:
            if is_edit_used:
                return False
            
            is_edit_used = True
            if len(string1) < len(string2):
                j += 1
                continue
            elif len(string1) > len(string2):
                i += 1
                continue
            
        i += 1
        j += 1
    
    return not (len(string1) != len(string2) and is_edit_used)

def string_compression(string):
    compressed = ''
    prev_char = string[0]
    count = 1
    for char in string[1:]:
        if char != prev_char:
            compressed += prev_char + str(count)
            count = 1
            prev_char = char
        else:
            count += 1

    compressed += prev_char + str(count)

    return compressed




if __name__ == "__main__":
    print(one_away('hall', 'helle'))
    


        
