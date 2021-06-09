#Les variables n'ont pas besoin d'être typé 
#----------------------------------------------------------------------------------------------------------------------------------------------------
message = "Hello"                       
print(message)                        # Prints Hello
message = 1+2+3+4                     # Prints 10
print(message)
#----------------------------------------------------------------------------------------------------------------------------------------------------
if message ==10:
                print('ok')           # 4 indentations pour remplacer les {}
                message+=message+1
elif message ==9:                     #elif = else if                    
                print('nope')
#----------------------------------------------------------------------------------------------------------------------------------------------------                
print(message)              
number = 1 + 2 * 3 / 4.0              # multiplication et division ensuite addition et soustraction sauf si () = priorité  
print(number)
number = 2**3                         # ** = puissance de
print(number)
helloworld = "hello" + " " + "world"  # Concaténation String basique
print(helloworld) 

#----------------------------------------------------------------------------------------------------------------------------------------------------
tableau = []
tableau2 = [1,2,3]                    # Tableau
tableau.append(helloworld)            # Tableau append
tableau.append(13)
tableau.append(1153)
print(tableau[0]) # prints hellohellohello....
print(tableau[1]) # prints 13
tableaufusion = tableau + tableau2    # Fusion de tableaux
print(tableaufusion)

for element in tableau:               # print tous les éléments du tableau, element = variable au choix
    print(element)
for element in tableau2:              # print tous les éléments du tableau2, element = variable au choix
    print(element)
#----------------------------------------------------------------------------------------------------------------------------------------------------
helloworld = "hello" * 10             # String + * = hellohellohello... X10 
print(helloworld)                     # Prints hellohellohello... X 10

print(tableau * 3)                    # Print le contenu du tableau 3 fois dans un seul tableau                            
#----------------------------------------------------------------------------------------------------------------------------------------------------
                                      # Compter une valeur ou un objet dans un tableau
if tableau.count(13)==2:
                print("Le tableau contient deux fois le nombre 13")
elif tableau.count(13)==1:
                print("Le tableau contient une fois 13")
#----------------------------------------------------------------------------------------------------------------------------------------------------
nom ='Tom'
age = 23
print("%s a %s ans." % (nom, age))    # %s = variable temporaire, (nom,age) remplace les variable temporaire
# Prints Tom a 23 ans
#----------------------------------------------------------------------------------------------------------------------------------------------------
print("Mon tableau: %s" % tableau)

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)
#------------------------------------------------------------------------------------------------------------------------------------------------------
