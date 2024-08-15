from dotenv import load_dotenv
import os

load_dotenv()

S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

S2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

def expension(toExpense):
    return toExpense[7] + toExpense[0] + toExpense[1] + toExpense[2] + toExpense[3] + toExpense[4] + toExpense[3] + toExpense[4] + toExpense[5] + toExpense[6] + toExpense[7] + toExpense[0]

def permutation (toPermute):
    return toPermute[1] + toPermute[7] + toPermute[3] + toPermute[6] + toPermute[6] + toPermute[4] + toPermute[2] + toPermute[0]

def permutationKey(toPermute):
    return toPermute[7] + toPermute[6] + toPermute[0] + toPermute[3] + toPermute[9] + toPermute[4] + toPermute[3] + toPermute[8] + toPermute[1] + toPermute[11] + toPermute[5] + toPermute[10]

SECRET = (os.getenv('SECRET_DES')) # 12 bits

MESSAGE = "1100100111001101" # 16 bits

left_part= MESSAGE[:len(MESSAGE)//2]
right_part= MESSAGE[len(MESSAGE)//2:]

for i in range(16):
    print("\n### Iteration " + str(i) + " ###\n")
    key_left_part= SECRET[:len(SECRET)//2]
    key_right_part= SECRET[len(SECRET)//2:]

    # find E
    E = expension(right_part)
    print("E value : " + E)

    # find K
    if(i+1 in [1, 2, 9, 16]):
        key_left_part = key_left_part[1:] + key_left_part[:1]
        key_right_part = key_right_part[1:] + key_right_part[:1]
    else:
        key_left_part = key_left_part[2:] + key_left_part[:2]
        key_right_part = key_right_part[2:] + key_right_part[:2]

    SECRET = key_left_part + key_right_part
    K =  permutationKey(key_left_part + key_right_part)
    print("K value : " + K)

    # find XOR result between E and K
    xor_result = ""
    for j in range(len(E)):
        if E[j] == K[j]:
            xor_result += "0"
        else:
            xor_result += "1"

    print("E XOR K value : " + str(xor_result))

    # find S
    X_1_part = xor_result[:len(xor_result)//2]
    X_2_part = xor_result[len(xor_result)//2:]

    ## first vector S-box value
    X_1_row_index = int(X_1_part[0] + X_1_part[-1], 2)
    X_1_col_index = int(X_2_part[1 : -1], 2)
    S_1_value = S1[X_1_row_index][X_1_col_index]

    ## second vector S-box value
    X_2_row_index = int(X_2_part[0] + X_2_part[-1], 2)
    X_2_col_index = int(X_2_part[1 : -1], 2)
    S_2_value = S2[X_2_row_index][X_2_col_index]
    
    # find P
    P = permutation(bin(S_1_value).zfill(4) + bin(S_2_value).zfill(4))
    print("P value : " + P)

    # find XOR result between P and Left_part
    xor_result = ""
    for j in range(len(left_part)):
        if left_part[j] == P[j]:
            xor_result += "0"
        else:
            xor_result += "1"

    right_part = xor_result
    left_part = right_part # permute left/right value for next iteration

    print ("n°" + str(i) + " : " + str(left_part) + " " + str(right_part))

print ("\nCrypted message : " + str(left_part) + str(right_part))