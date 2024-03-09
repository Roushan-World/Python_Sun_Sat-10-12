try: 
    x=int(input('Enter first number:'))
    y=int(input('Enter second number:'))
    z=x/y
    print(z)
except ZeroDivisionError:
    print('Denominator Could not be zero.')
except ValueError:
    print('Enter correct value integer form.')

print('hello world')

