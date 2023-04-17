def dec_to_bin(num_decimal_digits=8):
    decimal = input("\nEnter a valid decimal value: ")
    num = False
    if "." in decimal:
        dec_index = decimal.index(".")
        if decimal[0:dec_index].isdigit() and decimal[dec_index+1:].isdigit():
            num = True
    else:
        if decimal.isdigit():
            num = True
    if num:
        integer_part = int(decimal[0:dec_index]) if "." in decimal else int(decimal)
        fractional_part = float("0." + decimal[dec_index+1:]) if "." in decimal else 0
        
        # Convert integer part to binary
        binary_integer = bin(integer_part)[2:]
        
        # Convert fractional part to binary
        binary_fractional = ""
        for _ in range(num_decimal_digits):
            fractional_part *= 2
            if fractional_part >= 1:
                binary_fractional += "1"
                fractional_part -= 1
            else:
                binary_fractional += "0"
        
        # Combine integer and fractional binary parts
        if binary_fractional:
            binary = binary_integer + "." + binary_fractional
        else:
            binary = binary_integer
        
        print(f"The binary representation of {decimal} is {binary}")
    else:
        print("Invalid input. Please enter a valid decimal value.")



dec_to_bin()