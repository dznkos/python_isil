
def ejercicio3():

    #ejer 1:
    suma=0
    listNum = [1,3,4,5,7,11]
    for num in listNum:
        suma=suma+(num**2)
    print("la suma de los cuadrados es: ", suma)

    #ejer 2:
    cont=0
    mitext= "Avellaneda Talara"
    print(mitext)
    for busc in mitext:
        if(busc=='a' or busc=='A'):
         cont+=1
    print("total de a es:",cont)


if __name__=='__main__':
 ejercicio3()
