def power(number,step):
    if step == 0:
        return 1
    else:
        return number * power(number,step - 1)

print(power(4,4))