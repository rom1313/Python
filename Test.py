#Les variables n'ont pas besoin d'être typé 
message = "Hello"
print(message)
message = 1+2+3+4
print(message)
if message ==10:
                print('ok')           # 4 indentations pour remplacer les {}
                message+=message+1
elif message ==9:                     #elif = else if                    
                print('nope')
print(message)              
number = 1 + 2 * 3 / 4.0              # multiplication et division ensuite addition et soustraction sauf si () = priorité  
print(number)
number = 2**3                         # ** = puissance de
print(number)
helloworld = "hello" + " " + "world"  # Concaténation String basique
print(helloworld) 
helloworld = "hello" * 10             # String + * = hellohellohello... X10 
print(helloworld)
tableau = []
tableau2 = [1,2,3]                          # Tableau
tableau.append(helloworld)            # Tableau append
tableau.append(13)
tableau.append(1153)
print(tableau[0]) # prints hellohellohello....
print(tableau[1]) # prints 13


for element in tableau:               # print tous les éléments du tableau, element = variable au choix
    print(element)
for element in tableau2:               # print tous les éléments du tableau2, element = variable au choix
    print(element)
