import numpy as np
import string

# esta funcion genera una matriz cuadrada con los posibles tamaños de las mesas (4, 5, 6 o 8)
def generarMesas(tamaño:int)-> tuple:
    # si se ingresa un numero fuera del rango valido, se lanza un error
    if tamaño not in (4, 5, 6, 8):
        raise ValueError(f"El tamaño de la matriz debe ser 4, 5, 6 o 8. Se recibió: {tamaño}")
    # letras desde A hasta el tamaño de la matriz, ej: si tamaño = 4, letras = ["A","B","C","D"]
    letras = list(string.ascii_uppercase)[:tamaño]
    matriz = np.array([[{"posicion":f"{letras[i]}{j}", "ocupado":False, "capacidad":0, "personasUsando":0} for j in range(tamaño)] for i in range(tamaño)])
    matrizVisual = matriz.copy()
    # se inicia la variable i en un numero dependiendo del tamaño de la matriz para cumplir con el patron de colores
    if tamaño == 4:
        i = 2
        ajuste = -2
    elif tamaño in (5, 8):
        i = 1
        ajuste = 0
    elif tamaño == 6:
        i = 3
        ajuste = -1

    # se recorre la matriz y se asigna el color y la capacidad a cada mesa
    for row in range(tamaño):
        if row > 0:
            # esta suma es para que el patron se mantenga
            i+=ajuste
        if i > 3:
            # y esta para que i no supere el rango de colores
            i = i-3
        for col in range(tamaño):
            if i > 3:
                # aca i se reinicia cuando llegue a 4
                i = 1
            capacidades = [2,4,8] 
            colores = ["🟩","🟪","🟦"] # ⚠️⚠️⚠️⚠️ - estos colores son para visualizar graficamente como se ve la matriz en la consola, remover en la versión final
            matriz[row][col]["capacidad"] = capacidades[i-1] # se asigna la capacidad a la mesa
            matrizVisual[row][col] = colores[i-1] # ⚠️⚠️⚠️⚠️ - se asigna el color a las mesas de la matriz visual, remover en la versión final
            i+=1
    
    return (matriz, matrizVisual) # ⚠️⚠️⚠️⚠️ - el primer valor retornado [0] es la matriz que se va a usar en el resto del programa, el segundo [1] es para no confundirse tanto, se puede eliminar en la version final O quizás se puede incluir en la interfaz de usuario


print(generarMesas(4)[0])
print(generarMesas(4)[1])


# el siguiente paso es crear una funcion para asignar una mesa aleatoria a una(s) personas con los criterios de la Historia de Usuario. Recomiendo hacer un for que genere una cantidad aleatoria de grupos de personas y que cada grupo tenga una cantidad aleatoria de personas para probar que si funciona.