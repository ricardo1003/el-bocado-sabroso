#La mala pa ricardo, no sabes sacar porcentaje
class sala:
    def __init__(self, nombre:str, sala:int):
        self.sala = sala-1
        self.nombre = nombre
        self.filas = (7,11,13)
        self.asientos_fila = (7,11,13)
        self.costos_asientos = (5000,15000,20000)
        self.asientos = [[False for _ in range(self.asientos_fila[self.sala])] for _ in range(self.filas[self.sala])]
        self.letras_filas = "ABCDEFGHIJKLM"
        
        print(self.letras_filas)
        print(self.letras_filas[0:3])
    def venderPuesto(self, letra:str, numero:str):
        if letra.upper() not in self.letras_filas:
            raise ValueError("La letra no esta dentro de las filas.")
        try:
            columna = int(numero)
        except ValueError:
            raise ValueError("El valor ingresado debe ser un numero")
        if columna <= 0:
            raise ValueError("El numero debe ser mayor a 0.")
        
        
        fila = self.letras_filas.index(letra.upper())
        print(fila)
        columna = columna-1
        print(columna)
        precio = 5000
        for row in range(self.asientos_fila[self.sala]):
            if fila >= round(self.filas[self.sala]/2,0)-1:
                i = 2
                for col in range(self.filas[self.sala]):
                    if columna == fila or columna == i:
                        precio = 15000
                    elif i >= 0:
                        i -= 1
            
            if fila >= round(self.filas[self.sala]/2,0):
                i = -1
                for col in range(self.filas[self.sala]):
                    i+=1
                    if columna in self.asientos[fila][print(round(self.filas[self.sala]/2,0)-1-i) : print(round(self.filas[self.sala]/2,0)-1-i)+i]: # sin terminar
                        precio = 20000
                        i = -1
                        

        
        
        if self.asientos[fila][columna] == False:
            return precio
            self.asientos[fila][columna] = False
        else:
            return "El asiento ya esta vendido"
        

    def calcular_asientos_vendidos(self)->int:
        vendidos = 0
        for columna in self.asientos:
            for fila in columna:
                if fila == True:
                    vendidos += 1
        return vendidos
    
    def calcular_asientos_disponibles(self) -> int:
        return (self.filas[self.sala]*self.asientos_fila[self.sala]) - self.calcular_asientos_vendidos()
    
    def calcular_dinero_recaudado(self):
        return self.calcular_asientos_vendidos() * self.costos_asientos
    
    def calcular_tasa_de_ocupacion_total(self)->float:
        return round(self.calcular_asientos_vendidos()/(self.filas[self.sala] * self.asientos_fila[self.sala])*100, 2)
    
    def calcular_tasa_de_ocupacion_fila(self, letra)->float:
        if letra.upper() not in self.letras_filas:
            raise ValueError("La letra no esta dentro de las filas.")
        fila = self.letras_filas.index(letra.upper())
        vendidos = 0
        for asiento in self.asientos[fila]:
            if asiento == True:
                vendidos += 1
        return (vendidos/self.asientos_fila[self.sala])*100
    
    def calcular_total_asientos(self):
        return self.filas[self.sala]*self.asientos_fila[self.sala]
    
    

            
    
    
    
una_sala = sala("cinecosta",1)


print(una_sala.venderPuesto("D",4))
print(una_sala.venderPuesto("E",4))

for fila in una_sala.asientos:
    print(fila)
print (f"la cantidad de puestos vendidos es de: {una_sala.calcular_asientos_vendidos()}, quedan {una_sala.calcular_asientos_disponibles()} disponibles de {una_sala.calcular_total_asientos()}")
print(f"total recaudado: ${una_sala.calcular_dinero_recaudado()} pesos")
print(f"En total, hay un {una_sala.calcular_tasa_de_ocupacion_total()}% de ocupacion")
print(f"En la fila C, hay un {round(una_sala.calcular_tasa_de_ocupacion_fila("C"), 2)}% de ocupación")
