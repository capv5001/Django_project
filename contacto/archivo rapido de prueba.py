def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        while letra == '0':
            cadena_invertida = letra + cadena_invertida
            print(cadena_invertida)
            break
        print(len(cadena_invertida))

""" invertir_cadena_manual('30103100000') """


def ejemplo(texto):
    num_u_cero = 0
    for i in texto:
        if i=='0':
            num_u_cero+=1
        else:
            num_u_cero=0   
    print(num_u_cero)