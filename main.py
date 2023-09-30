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


print(star_print(8))
print(power(4, 4))
