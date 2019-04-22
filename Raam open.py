temperatuur = input ("Voer de temperatuur in:")
raam_open = 0

print ("De temperatuur is volgens jou " + (temperatuur) + " graden")

if int(temperatuur) > 25:
    raam_open = 1
else:
    raam_open = 0
    
    
if int(raam_open) == 1:
    print ("Het raam staat open.")
else:
    print ("Het raam staat dicht.")   
    
# print (raam_open)
# print (temperatuur)
