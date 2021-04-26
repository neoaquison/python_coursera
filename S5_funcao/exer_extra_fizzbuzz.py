def fizzbuzz(x):
    tres = x % 3
    cinco = x % 5
    if tres == 0 and cinco != 0:
        fizzbuzz = "Fizz"
    elif cinco == 0 and tres != 0:
        fizzbuzz = "Buzz"
    elif cinco == 0 and tres == 0:
        fizzbuzz = "FizzBuzz"
    else:
        fizzbuzz = x
    return fizzbuzz

numero = int(input('Digite um número: '))

print(fizzbuzz(numero))
