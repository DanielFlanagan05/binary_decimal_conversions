def unsigned_bin_to_dec():
    """
    Converts unsigned binary numbers to decimal. Works for floating point values. 
    """
    binary_str = input("Enter an unsigned binary number: ")

    # Check for invalid characters
    if not all(c in {'0', '1', '.'} for c in binary_str) or binary_str.count('.') > 1:
        print("Error: Invalid input. Please enter a valid binary number.")
        return None

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

    print(f"The decimal value of the unsigned binary number {binary_str} is: {decimal_value}")
    return decimal_value
