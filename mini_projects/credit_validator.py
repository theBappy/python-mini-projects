
# 1234-5678-9012-3456

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# remove any '-' or ' '
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# add all digits of the odd places
for x in card_number[::2]:
    sum_odd_digits += int(x)

# double all every second digit
for x in card_number[1::2]:
    x = int(x * 2)
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# add both 
total = sum_odd_digits + sum_even_digits

# validation check
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")

# print(card_number)