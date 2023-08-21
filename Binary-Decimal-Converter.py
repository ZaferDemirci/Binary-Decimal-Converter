
def decimal_to_binary(decimal_value):
    if decimal_value < 0 or decimal_value > 65535:
        raise ValueError("Invalid decimal value. It should be between 0 and 65535.")

    binary_answ = ""
    add_zero = True

    for i in range(15, -1, -1):
        bit_value = (decimal_value >> i) & 1

        if bit_value == 1:
            add_zero = False

        if not add_zero:
            binary_answ += str(bit_value)

            if (i % 8 == 0) and (i != 0):
                binary_answ += "."

    return binary_answ


def binary_to_decimal(binary_value):
    if not all(bit in ['0', '1'] for bit in binary_value):
        raise ValueError("Invalid binary value. It should consist of 0s and 1s.")

    if len(binary_value) > 16:
        raise ValueError("Invalid binary value. It should have at most 16 bits.")

    decimal_ans = 0
    power = len(binary_value) - 1

    for bit in binary_value:
        if bit == '1':
            decimal_ans += 2 ** power
        power -= 1

    return decimal_ans


def main():
    while True:
        user_input = input("Enter 'd' for decimal or 'b' for binary input, or enter 'q' to quit: ")

        if user_input.lower() == 'q':
            break

        if user_input.lower() == 'd':
            decimal_input = input("Enter a decimal integer (0-65535): ")

            try:
                decimal_value = int(decimal_input)
                binary_answ = decimal_to_binary(decimal_value)
                print("Decimal:", decimal_value)
                print("Binary:", binary_answ)
            except ValueError as e:
                print("Error:", str(e))

        elif user_input.lower() == 'b':
            binary_input = input("Enter a binary number: ")

            try:
                decimal_answ = binary_to_decimal(binary_input)
                print("Binary:", binary_input)
                print("Decimal:", decimal_answ)
            except ValueError as e:
                print("Error:", str(e))

        else:
            print("Invalid input. Please try again.")


if __name__ == '__main__':
    main()
