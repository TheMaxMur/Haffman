def int_to_hex(n: int=0):
    alpha = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "D", 15: "F"}
    result = ""
    while (n != 0):
        result = alpha[n%16] + result
        n = n // 16
    return (result)


def hex_to_int(n: str=""):
    alpha = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 14, 'F': 15}
    result = 0
    rank = 1
    for el in n[::-1]:
        result += alpha[el] * rank
        rank *= 16
    return (result)

num = int(input("Enter number: "))
print(int_to_hex(num))
print(hex_to_int(int_to_hex(num)))
