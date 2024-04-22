def main():
    # 1. Fibonacci
    def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

    n = 10
    resultado_fibonacci = fibonacci(n)
    print(f"1. Fibonacci: {resultado_fibonacci}")

    # 2. Suma de números enteros
    def suma_enteros(n):
        return 0 if n == 0 else n + suma_enteros(n-1)

    n = 5
    resultado_suma_enteros = suma_enteros(n)
    print(f"2. Suma de números enteros hasta {n}: {resultado_suma_enteros}")

    # 3. Producto de dos números enteros
    def producto(a, b):
        return 0 if b == 0 else a + producto(a, b-1)

    a, b = 3, 4
    resultado_producto = producto(a, b)
    print(f"3. Producto de {a} y {b}: {resultado_producto}")

    # 4. Potencia de un número entero
    def potencia(base, exponente):
        return 1 if exponente == 0 else base * potencia(base, exponente-1)

    base, exponente = 2, 3
    resultado_potencia = potencia(base, exponente)
    print(f"4. Potencia de {base}^{exponente}: {resultado_potencia}")

    # 5. Conversión de número romano a decimal
    def valor_romano(letra):
        if letra == 'I':
            return 1
        elif letra == 'V':
            return 5
        elif letra == 'X':
            return 10
        # Agregar el resto de las letras romanas con sus valores
        else:
            return 0

    def romano_a_decimal(romano):
        if len(romano) == 0:
            return 0
        elif len(romano) == 1:
            return valor_romano(romano)
        else:
            if valor_romano(romano[0]) < valor_romano(romano[1]):
                return valor_romano(romano[1]) - valor_romano(romano[0]) + romano_a_decimal(romano[2:])
            else:
                return valor_romano(romano[0]) + romano_a_decimal(romano[1:])

    romano = "XIV"
    resultado_romano_decimal = romano_a_decimal(romano)
    print(f"5. Conversión de {romano} a decimal: {resultado_romano_decimal}")

    # 6. Invertir una secuencia de caracteres
    def invertir_secuencia(secuencia):
        if len(secuencia) == 0:
            return secuencia
        else:
            return invertir_secuencia(secuencia[1:]) + secuencia[0]

    secuencia = "hello"
    resultado_invertir_secuencia = invertir_secuencia(secuencia)
    print(f"6. Invertir la secuencia '{secuencia}': {resultado_invertir_secuencia}")

    # 7. Calcular serie
    def calcular_serie(n):
        return 0 if n == 0 else n + calcular_serie(n-1)

    n = 5
    resultado_serie = calcular_serie(n)
    print(f"7. Calcular serie hasta {n}: {resultado_serie}")

    # 8. Decimal a binario
    def decimal_a_binario(decimal):
        if decimal == 0:
            return '0'
        elif decimal == 1:
            return '1'
        else:
            return decimal_a_binario(decimal // 2) + str(decimal % 2)

    decimal = 13
    resultado_decimal_a_binario = decimal_a_binario(decimal)
    print(f"8. Decimal {decimal} en binario: {resultado_decimal_a_binario}")

    # 9. Logaritmo entero en una base dada
    def logaritmo_entero(n, b):
        if n < b:
            return 0
        else:
            return 1 + logaritmo_entero(n // b, b)

    n, b = 16, 2
    resultado_logaritmo_entero = logaritmo_entero(n, b)
    print(f"9. Logaritmo entero de {n} en base {b}: {resultado_logaritmo_entero}")

    # 10. Cantidad de dígitos de un número entero
    def contar_digitos(numero):
        if numero < 10:
            return 1
        else:
            return 1 + contar_digitos(numero // 10)

    numero = 123456
    resultado_contar_digitos = contar_digitos(numero)
    print(f"10. Cantidad de dígitos de {numero}: {resultado_contar_digitos}")

    # 11. Invertir un número entero sin convertirlo a cadena
    def invertir_entero(numero):
        def invertir_aux(numero, resultado):
            if numero == 0:
                return resultado
            else:
                return invertir_aux(numero // 10, resultado * 10 + numero % 10)
        return invertir_aux(numero, 0)

    numero = 123456
    resultado_invertir_entero = invertir_entero(numero)
    print(f"11. Invertir el número entero {numero}: {resultado_invertir_entero}")

    # 12. Algoritmo de Euclides para el Máximo Común Divisor (MCD)
    def mcd(a, b):
        if b == 0:
            return a
        else:
            return mcd(b, a % b)

    a, b = 48, 18
    resultado_mcd = mcd(a, b)
    print(f"12. MCD de {a} y {b}: {resultado_mcd}")

    # 13. Algoritmo de Euclides para el Mínimo Común Múltiplo (MCM)
    def mcm(a, b):
        return a * b // mcd(a, b)

    resultado_mcm = mcm(a, b)
    print(f"13. MCM de {a} y {b}: {resultado_mcm}")

    # 14. Suma de los dígitos de un número entero
    def suma_digitos(numero):
        if numero < 10:
            return numero
        else:
            return numero % 10 + suma_digitos(numero // 10)

    numero = 12345
    resultado_suma_digitos = suma_digitos(numero)
    print(f"14. Suma de dígitos de {numero}: {resultado_suma_digitos}")

    # 15. Raíz cuadrada entera de un número entero
    def raiz_cuadrada_entera(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            x = n // 2
            prev = 0
            while x != prev:
                prev = x
                x = (x + n // x) // 2
            return x

    n = 16
    resultado_raiz_cuadrada_entera = raiz_cuadrada_entera(n)
    print(f"15. Raíz cuadrada entera de {n}: {resultado_raiz_cuadrada_entera}")

    # 16. Sucesión geométrica con a1=2 y razón r=-3
    def sucesion_geometrica(n):
        if n == 1:
            return 2
        else:
            return -3 * sucesion_geometrica(n-1)

    def valores_sucesion(n):
        return [sucesion_geometrica(i) for i in range(1, n+1)]

    n = 5
    resultado_sucesion_geometrica = valores_sucesion(n)
    print(f"16. Valores de la sucesión geométrica hasta {n}: {resultado_sucesion_geometrica}")

    # 17. Mostrar vector de atrás hacia adelante
    def mostrar_vector_atras(vec, i):
        if i < 0:
            return
        else:
            print(vec[i])
            mostrar_vector_atras(vec, i-1)

    vec = [1, 2, 3, 4, 5]
    mostrar_vector_atras(vec, len(vec)-1)

    # 18. Recorrer una matriz y mostrar sus valores
    def mostrar_matriz(mat, i, j):
        if i == len(mat):
            return
        elif j == len(mat[i]):
            mostrar_matriz(mat, i+1, 0)
        else:
            print(mat[i][j])
            mostrar_matriz(mat, i, j+1)

    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mostrar_matriz(matriz, 0, 0)

    # 19. Cálculo de sucesión recursiva dada
    def sucesion_recursiva(n):
        if n == 0:
            return 1
        elif n == 1:
            return 2
        else:
            return 2 * sucesion_recursiva(n-1) - 3 * sucesion_recursiva(n-2)

    n = 5
    resultado_sucesion_recursiva = sucesion_recursiva(n)
    print(f"19. Valor de la sucesión recursiva en {n}: {resultado_sucesion_recursiva}")

    # 20. Búsqueda secuencial recursiva con centinela
    def busqueda_secuencial(lista, valor, indice=0):
        if indice == len(lista):
            return False
        elif lista[indice] == valor:
            return True
        else:
            return busqueda_secuencial(lista, valor, indice + 1)

    lista = [1, 2, 3, 4, 5]
    valor = 3
    resultado_busqueda_secuencial = busqueda_secuencial(lista, valor)
    print(f"20. Búsqueda secuencial de {valor} en lista: {resultado_busqueda_secuencial}")

    # 21. Búsqueda binaria recursiva en lista ordenada
    def busqueda_binaria_recursiva(lista, valor, inicio=0, fin=None):
        if fin is None:
            fin = len(lista) - 1
        if inicio > fin:
            return False
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            return True
        elif lista[medio] < valor:
            return busqueda_binaria_recursiva(lista, valor, medio + 1, fin)
        else:
            return busqueda_binaria_recursiva(lista, valor, inicio, medio - 1)

    lista_ordenada = [1, 2, 3, 4, 5]
    valor = 3
    resultado_busqueda_binaria_recursiva = busqueda_binaria_recursiva(lista_ordenada, valor)
    print(f"21. Búsqueda binaria de {valor} en lista ordenada: {resultado_busqueda_binaria_recursiva}")

    # 22. Uso de la fuerza en la mochila Jedi
    def usar_la_fuerza(mochila, indice=0):
        if indice == len(mochila):
            return False, 0
        elif mochila[indice] == "sable de luz":
            return True, indice + 1
        else:
            encontrado, pasos = usar_la_fuerza(mochila, indice + 1)
            return encontrado, pasos + 1

    mochila = ["libro", "comida", "sable de luz", "mapa"]
    encontrado, pasos = usar_la_fuerza(mochila)
    print(f"22. ¿Se encontró un sable de luz en la mochila? {encontrado}. Pasos necesarios: {pasos}")

    # 23. Salida del laberinto
    def salir_del_laberinto(laberinto, x=0, y=0, solucion=None):
        if solucion is None:
            solucion = []
        n = len(laberinto)
        if x == n - 1 and y == n - 1:
            solucion.append((x, y))
            return True, solucion
        elif 0 <= x < n and 0 <= y < n and laberinto[x][y] == 0 and (x, y) not in solucion:
            solucion.append((x, y))
            if (salir_del_laberinto(laberinto, x+1, y, solucion)[0] or
                salir_del_laberinto(laberinto, x, y+1, solucion)[0] or
                salir_del_laberinto(laberinto, x-1, y, solucion)[0] or
                salir_del_laberinto(laberinto, x, y-1, solucion)[0]):
                return True, solucion
            solucion.pop()
        return False, solucion

    laberinto = [[0, 1, 0, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
    resultado_salida_laberinto, solucion = salir_del_laberinto(laberinto)
    if resultado_salida_laberinto:
        print("23. Se encontró un camino para salir del laberinto:")
        for fila, columna in solucion:
            print(f"({fila}, {columna}) -> ", end="")
        print("Salida")
    else:
        print("23. No se encontró un camino para salir del laberinto")

    # 24. Torre de Hanói
    def torre_de_hanoi(n, origen, destino, auxiliar):
        if n == 1:
            print(f"Mover disco de {origen} a {destino}")
        else:
            torre_de_hanoi(n-1, origen, auxiliar, destino)
            print(f"Mover disco de {origen} a {destino}")
            torre_de_hanoi(n-1, auxiliar, destino, origen)

    n_discos = 3
    print(f"24. Solución de la Torre de Hanói con {n_discos} discos:")
    torre_de_hanoi(n_discos, 'A', 'C', 'B')

    # 25. Triángulo de Pascal
    def triangulo_de_pascal(n):
        if n == 0:
            return [[1]]
        else:
            triangulo = triangulo_de_pascal(n-1)
            nueva_fila = [1]
            for i in range(1, n):
                nueva_fila.append(triangulo[n-1][i-1] + triangulo[n-1][i])
            nueva_fila.append(1)
            triangulo.append(nueva_fila)
            return triangulo

    filas = 5
    triangulo = triangulo_de_pascal(filas)
    print(f"25. Triángulo de Pascal con {filas} filas:")
    for fila in triangulo:
        print(fila)

    # 26. Colocación de las 8 reinas
    def es_valido(tablero, fila, columna):
        return not any(
            tablero[i] == columna or
            tablero[i] - i == columna - fila or
            tablero[i] + i == columna + fila
            for i in range(fila)
        )

    def colocar_reinas(tablero, fila=0):
        n = len(tablero)  # Asegurar que esta línea esté correctamente indentada
        if fila == n:
            return [tablero[:]]  # Crear una copia del tablero actual
        soluciones = []
        for columna in range(n):
            if es_valido(tablero, fila, columna):
                tablero[fila] = columna
                soluciones.extend(colocar_reinas(tablero, fila+1))
                tablero[fila] = -1  # Restaurar el valor original del tablero
        return soluciones

    tablero = [-1] * 8  # Inicializar el tablero con valores -1
    soluciones = colocar_reinas(tablero)
    print(f"26. Cantidad de soluciones encontradas para las 8 reinas: {len(soluciones)}")


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


    # 28. Cálculo de la bisección de una función
    def biseccion(f, a, b, tol=1e-6):
        if abs(b - a) < tol:
            return (a + b) / 2
        else:
            c = (a + b) / 2
            if f(a) * f(c) < 0:
                return biseccion(f, a, c)
            else:
                return biseccion(f, c, b)

    resultado_biseccion = biseccion(lambda x: x**2 - 2, 0, 2)
    print(f"28. Raíz cuadrada de 2 calculada con bisección: {resultado_biseccion}")

    # 29. Cálculo del método de la secante de una función
    def secante(f, x0, x1, tol=1e-6):
        while abs(x1 - x0) >= tol:
            x0, x1 = x1, x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        return x1

    resultado_secante = secante(lambda x: x**2 - 2, 1, 2)
    print(f"29. Raíz cuadrada de 2 calculada con secante: {resultado_secante}")

    # 30. Cálculo del método de Newton-Raphson de una función
    def newton_raphson(f, df, x0, tol=1e-6):
        while abs(f(x0)) >= tol:
            x0 -= f(x0) / df(x0)
        return x0

    resultado_newton_raphson = newton_raphson(lambda x: x**2 - 2, lambda x: 2*x, 2)
    print(f"30. Raíz cuadrada de 2 calculada con Newton-Raphson: {resultado_newton_raphson}")


if __name__ == "__main__":
    main()