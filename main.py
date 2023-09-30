def power(number,step):
    if step == 0:
        return 1
    else:
        return number * power(number,step - 1)


def star_print(number):
    if number == 1:
        return "*"
    else:
        return "*" + str(star_print(number-1))


def sum_numbers(a, b):
    if a == b:
        return a
    else:
        return a + sum_numbers(a+1, b)

print(sum_numbers(1,5))
print(star_print(8))
print(power(4, 4))
