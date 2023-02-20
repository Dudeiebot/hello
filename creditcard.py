def get_credit_card_number():
    while True:
        input_str = input("Enter the credit card number: ")
        if not input_str.isdigit():
            print("Invalid input. Please enter a positive integer.")                #come back here to add comments
            continue
        user_input = int(input_str)
        if user_input <= 0:
            print("Invalid input. Please enter a positive integer.")
            continue
        return user_input

def calculate_luhn_checksum(card_number):
    digit_count = 0
    luhn_sum = 0
    while card_number > 0:
        digit_count += 1
        digit = card_number % 10
        card_number //= 10

        if digit_count % 2 == 0:
            product = digit * 2
            luhn_sum += (product // 10) + (product % 10)
        else:
            luhn_sum += digit
       
    return luhn_sum

def get_card_issuer(card_number):
    first_digit = card_number
    while first_digit >= 10:
        first_digit //= 10

    first_two_digits = card_number
    while first_two_digits >= 100:
        first_two_digits //= 10
    
    second_digit = calculate_luhn_checksum(card_number)
    if len(str(second_digit)) > 1 and str(second_digit)[1] == "0":
        print("The card is valid", end = " ")
    else:
        print("The card is invalid", end = " ")
    

    if first_digit == 4:
        return "VISA"
    elif first_two_digits >= 51 and first_two_digits <= 55:
        return "MASTERCARD"
    elif first_two_digits in [34, 37]:
        return "AMEX"


credit_card_number = get_credit_card_number()
issuer = get_card_issuer(credit_card_number)
print(f"and issued by {issuer}", end="")
