def insertion(n, m, i, j):
    for k in range(i, j+1):
        mask = ~(1 << k)
        n &= mask
    m <<= i
    return n | m

def longest_sequence_ones(n):
    curr = 0
    prev = 0
    max_len = 0
    for i in range(32):
        if n & (1 << i) != 0:
            curr += 1
        else:
            prev = curr
            curr = 0

        max_len = max(curr + prev + 1, max_len)
    
    return max_len

def conversion(a, b):
    c = a ^ b
    count = 0
    while c != 0:
        if c & 1 == 1:
            count += 1
        c >>= 1
    return count

def pairwise_swap(n):
    odd = 1
    even = 0
    mask = 0b11
    while odd < 32:
        odd_bit = (n & (1 << odd))
        even_bit = (n & (1 << even))
        n &= ~mask
        n |= (odd_bit >> 1)
        n |= (even_bit << 1)
        odd += 2
        even += 2
        mask <<= 2
    return n

if __name__ == '__main__':   
    print(bin(pairwise_swap(0b11101001)))
