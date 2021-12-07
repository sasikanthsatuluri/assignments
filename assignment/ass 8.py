amount = float(input('enter the amount value'))
one = amount+(amount*(4/100))
two = one+(one*(4/100))
three = two+(two*(4/100))
print('the amount on first year{:.2f}, on second year{:.2f},on third year{:.2f}'.format(one,two,three))

def compound(amount):
    one = amount + (amount * (4 / 100))
    two = one + (one * (4 / 100))
    three = two + (two * (4 / 100))
    print('the amount on first year{:.2f}, on second year{:.2f},on third year{:.2f}'.format(one, two, three))
    amount = float(input('enter the amount value'))
    compound(amount)