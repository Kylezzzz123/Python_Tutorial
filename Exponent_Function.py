print(2**3)  #2^3

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):  # determine how many pow_num, 
        result *= base_num   # base_num * base_num, go back to for loop, and do it again until end of number of pow_nunm
    return result


print(raise_to_power(3,2))