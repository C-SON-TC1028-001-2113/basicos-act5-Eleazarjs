import math
def main():
    #escribe tu código abajo de esta línea
    área = float(input("Area a pintar en metros: "))
    rendimiento = float (input("Rendimiento (m2/l): " ))
    litros = int(math.ceil(área/rendimiento)) 
    print ("Litros a comprar: "+str(litros))
    

if __name__ == '__main__':
    main()
