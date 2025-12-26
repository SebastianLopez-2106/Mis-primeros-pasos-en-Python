"""Calculadora"""
Numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
Comandos = ["+", "-", "*", "/", "=", ")" , "("]
Inferior = ["+","-", "="]
Medio = ["*", "/"]

# verifica que no se introducieron letras
Correct = "No"
while Correct == "No":
    print("\n> Multiplicacion: \"*\" \n> Division: \"/\" \n> Suma: \"+\" \n> Resta: \"-\"")
    G = str(input("Ingrese la operacion y finalize con \"=\": "))
    if G[len(G) - 1] == "=":
        Correct = "Si"
    else:
        print("\nTermine con un \"=\" por favor! \n") 

Num = "" 

for i in range(len(G)): #Num -- Guarda los valores que estan antes del primer operador
    if G[i] in Numeros:
        Num = Num + G[i]
    
    elif G[i] in Comandos:
        Num = int(Num)
        break

Terminar = "off"
c = i # "c" es un contador para que "j" inicie en donde termino el bloque (c va a ser igual a la posicion final de Num siempre)
Num2 = ""#Num2 -- es el segundo numero que sera operaodo con Num
Num3 = ""

while Terminar == "off":
    Num2 = str(Num2)
    Num3 = str(Num3)
    Num3 = ""

    for j in range(c + 1, len(G)):
        if G[j] in Numeros:
            Num2 = Num2 + G[j]
        
        elif G[j] in Comandos and G[c] == "*":
            Num2 = int(Num2)
            Num = Num * Num2
            Num2 = ""
            c = j
            break
        
        elif G[j] in Comandos and G[c] == "/":
            Num2 = int(Num2)
            Num = Num / Num2
            Num2 = ""
            c = j
            break
        
        elif G[j] in Inferior and G[c] == "+":
            Num2 = int(Num2)
            Num = Num + Num2
            Num2 = ""
            c = j
            break

        elif G[j] in Inferior and G[c] == "-":
            Num2 = int(Num2)
            Num = Num - Num2
            Num2 = ""
            c = j
            break

        elif G[j] in Medio and G[c] in Inferior:
            Num2 = int(Num2)
            
            
            #Num3 -- si el siguiente operador depues de Num2 es "/" o "*" se crea una nueva variable que sera operada con Num2 para posteriormente sino se encuentran mas operadores como "*" o "/" operarse con Num
            Repetir = "on"
            d = j #contador de posision final de Num2 (en d se encuentra el comando)
            while Repetir == "on":
                Num3 = ""
                
                
                for k in range(d + 1, len(G)):
                    Num3 = str(Num3)
                    if G[k] in Numeros:    
                        Num3 = Num3 + G[k]
                    
                    elif G[k] in Comandos and G[d] == "*":
                        Num3 = int(Num3)
                        Num2 = Num2 * Num3
                        Num3 = str(Num3)
                        d = k
                        

                        if G[k] in Inferior:
                            if G[c] == "+":
                                Num = Num + Num2
                                Num2 = ""
                                Repetir = "of"
                                c = k
                                break
                            
                            elif G[c] == "-":
                                Num = Num - Num2
                                Num2 = ""
                                Repetir = "of"
                                c = k
                                break
                        
                        else:
                            d = k
                            break

                    elif G[k] in Comandos and G[d] == "/":
                        Num3 = int(Num3)
                        Num2 = Num2 / Num3
                        Num3 = str(Num3)
                        d = k

                        if G[k] in Inferior:
                            if G[c] == "+":
                                Num = Num + Num2
                                Num2 = ""
                                c = k
                                Repetir = "of"

                            elif G[c] == "-":
                                Num = Num - Num2
                                Num2 = ""
                                c = k
                                Repetir = "of"
                        else:
                            d = k
                            break
            break
    if c + 1 == len(G):
        Terminar = "on"

print(f"\nEl resultado es: {Num} \n")