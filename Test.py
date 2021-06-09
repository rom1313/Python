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
