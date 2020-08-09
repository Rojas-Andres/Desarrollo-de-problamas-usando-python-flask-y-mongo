#Comence por A:1 porque en el documento enviado lo desarrollaron asi para el ejemplo, tambien se tomo la letra Ñ porque 
#Somos latinos 
dic={
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":10,
    "K":11,
    "L":12,
    "M":13,
    "N":14,
    "Ñ":15,
    "O":16,
    "P":17,
    "Q":18,
    "R":19,
    "S":20,
    "T":21,
    "U":22,
    "V":23,
    "W":24,
    "X":25,
    "Y":26,
    "Z":27
}

#Desplazamiento cesar
while True:
    try:
        des=int(input("Digite el desplazamiento cesar\n\t:"))
        break 
    except:
        print("Has digitado mal el desplazamiento , recuerda que deben de ser numeros ")
while True:
    valor = input("Digite S para el cifrado cesar y N para descifrar\n\t:").upper()
    if valor in ('S','N'):
        if valor=='S':
            cifrado="cifrado cesar"
        else:
            cifrado= "descifrado cesar"
        break 
while True:
    try:        
        cadena=str(input("Digite la cadena para aplicar el {} \n\t:".format(cifrado))).upper()
        break 
    except:
        print("Recuerda que es una cadena , no deben de ser numeros ")
#Declaramos la cadena cesar para luego llenarla 
cesar = ""
#Esta funcion busca la llave en el diccionario la letra
def busca_llave(dic,letra):
    for llave,valor in dic.items():
        if llave==letra:
            return llave,valor
#Esta funcion busca el numero al que esta enlazada la letra del diccionario
def busca_valor(dic,indice):
    for llave,valor in dic.items():
        if valor==indice:
            return llave,valor
#Mostramos valores especiales para que el algoritmo no se caiga
valores_especiales=["1","2","3","4","5","6","7","8","9","0"," ",",",".","!","?","¡","¿","-","<",">","*","'",'"',"(",")"]
if valor=='S':
#Recorremos la cadena
    for i in range(len(cadena)):
        #Si el desplazamiento es positivo
        if des > 0:  
            letra=cadena[i]
            if letra in valores_especiales:
                cesar+=letra
                pass
            else:
                letra,indice = busca_llave(dic,cadena[i])
                indice += des 
                if indice > 27:
                    #Encontramos la diferencia para volver a empezar
                    dif = indice - 27
                    letra,valor = busca_valor(dic,dif)
                    cesar+=letra
                else:
                    #Buscamos la letra por el indice
                    letra,valor = busca_valor(dic,indice)
                    cesar+=letra
        #Si el desplazamiento es negativo
        elif des < 0:
            letra = cadena[i]
            if letra in valores_especiales:
                cesar+=letra
                pass
            else:
                letra,indice = busca_llave(dic,cadena[i])    
                indice +=des 
                if indice <= 0:
                    #Encontramos la diferencia para empezar desde la letra Z
                    #dif = 27 - indice
                    dif = 27 + indice
                    #print(dif,i)
                    
                    letra,valor = busca_valor(dic,dif)
                    cesar+=letra
                else:
                    #Buscamos la letra por el indice
                    letra,valor = busca_valor(dic,indice)
                    cesar+=letra
        else:
            cesar=cadena
#Significa que vamos a decifrar el mensaje
else:
    for i in range(len(cadena)):
        #Si el desplazamiento es positivo
        if des > 0:
            letra=cadena[i]
            if letra in valores_especiales:
                cesar+=letra
                pass
            else:
                letra,indice = busca_llave(dic,cadena[i])
                indice = indice - des 
                #print(letra,indice)
                if indice > 27:
                    #Encontramos la diferencia para volver a empezar
                    dif = 27 - indice
                    #print(dif) 
                    letra,valor = busca_valor(dic,dif)
                    cesar+=letra
                elif indice <=0:
                    dif = 27 + indice 
                    letra,valor = busca_valor(dic,dif)
                    cesar+=letra
                else:
                    #Buscamos la letra por el indice
                    letra,valor = busca_valor(dic,indice)
                    cesar+=letra    
        #Si el desplazamiento es negativo
        elif des < 0:
            letra=cadena[i]
            if letra in valores_especiales:
                cesar+=letra
                pass
            else:
                letra,indice = busca_llave(dic,cadena[i])
                indice -= des 
                if indice > 27:
                    #Encontramos la diferencia para volver a empezar
                    dif = indice - 27
                    letra,valor = busca_valor(dic,dif)
                    cesar+=letra
                else:
                    #Buscamos la letra por el indice
                    letra,valor = busca_valor(dic,indice)
                    cesar+=letra
        else:
            cesar = cadena
print("Cadena original : {}".format(cadena))
print("{}   : {}".format(cifrado,cesar)) 