def convert_binary_to_decimal(binary_str):
    # Split the binary string into integer and fractional parts
    integer_part, fractional_part = binary_str.split('.') if '.' in binary_str else (binary_str, '')

    # Convert integer part to decimal
    decimal_integer = 0
    for idx, digit in enumerate(integer_part[::-1]):
        decimal_integer += int(digit) * (2 ** idx)

    # Convert fractional part to decimal
    decimal_fraction = 0
    for idx, digit in enumerate(fractional_part):
        decimal_fraction += int(digit) * (2 ** -(idx + 1))

    decimal_value = decimal_integer + decimal_fraction

    return decimal_value


def bin_to_dec_signed():
    """
    Converts signed binary values to decimal. Works with floating point numbers. Only works for signed values.
    """
    binary_str = input("Enter a binary number (with optional floating point): ")

    # Check for invalid characters
    if not all(c in {'0', '1', '.'} for c in binary_str) or binary_str.count('.') > 1:
        print("Error: Invalid input. Please enter a valid binary number.")
        return None

    # Split the binary string into integer and fractional parts
    integer_part, fractional_part = binary_str.split('.') if '.' in binary_str else (binary_str, '')

    # Check if the number is negative 
    is_negative = int(integer_part[0]) == 1

    if is_negative:
        # Invert bits
        inverted_integer = ''.join(['1' if bit == '0' else '0' for bit in integer_part])
        inverted_fraction = ''.join(['1' if bit == '0' else '0' for bit in fractional_part])

        # Add 1
        inverted_bin = inverted_integer + '.' + inverted_fraction
        inverted_dec = convert_binary_to_decimal(inverted_bin)
        inverted_dec += 2 ** -(len(fractional_part))  # Add 1 to the inverted decimal value

        integer_part, fractional_part = str(inverted_dec).split('.')

    decimal_value = convert_binary_to_decimal(integer_part + '.' + fractional_part)

    if is_negative:
        decimal_value = -decimal_value

    print(f"The decimal value of the binary number {binary_str} is: {decimal_value}")
    return decimal_value
