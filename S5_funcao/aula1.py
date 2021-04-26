"""def troca(x, y):
    aux = x
    x = y
    y = aux

x = 10
y = 20
troca (x,y)
print("x =", x,"e y =",y)"""

"""def total_Caracteres (x, y, z):
    return sum(len(x,y,z))
"""

"""def total_Caracteres (x, y, z):
    return len(x)+len(y)+len(z)

x = input()
y = input()
z = input()

print(total_Caracteres(x, y, z))"""

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
