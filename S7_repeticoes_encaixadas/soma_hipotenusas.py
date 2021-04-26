def e_hipotenusa(n):
    i = 1
    j = 2
    cateto_ad = 0
    catteto_oposto = 0
    soma = 0
    while  soma <= n:
        cateto_ad = i ** 2
        while soma <= n:
            catteto_oposto = j ** 2
            j = j+1
            soma = cateto_ad + catteto_oposto
        i = 