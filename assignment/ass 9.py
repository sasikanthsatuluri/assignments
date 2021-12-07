# m = int(input('enter the number of widgets:'))
# n = int(input('enter the number of gizmos'))
# widgets = m*75
# gizmos = n*112
# print('the total weight is{}'.format(widgets+gizmos))


def total(m,n):
    widgets = m * 75
    gizmos = n * 112
    print('the total weight is{}'.format(widgets + gizmos))
    m = int(input('enter the number of widgets:'))
    n = int(input('enter the number of gizmos'))
    total(m, n)