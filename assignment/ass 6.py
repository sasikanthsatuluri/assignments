price = int(input('enter the amount:'))
tax =price*30/100
tip = price*18/100
total =price+tip+tax
print('the total is {},with tip{},tax{}'.format(total,tip,tax))

def price (n):
    tax = price * 30 / 100
    tip = price * 18 / 100
    total = price + tip + tax
    print('the total is {},with tip{},tax{}'.format(total, tip, tax))
    n = int(input('enter the amount:'))
    price(n)
