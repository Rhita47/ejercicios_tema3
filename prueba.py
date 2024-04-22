# 27. Valores de una sucesión geométrica hacia atrás
def sucesion_geometrica_atras(valor_final, a1, r):
    valores= [valor_final]
    while valor_final != a1:
        valor_final //= r  # División entera para asegurar que el resultado sea un entero
        valores.append(valor_final)
        return valores
valor_final=1376256
a1=5.25
r=4
valores=sucesion_geometrica_atras(valor_final, a1, r)
print(f"27. Valores de la sucesión geométrica hacia atrás: {valores}")
