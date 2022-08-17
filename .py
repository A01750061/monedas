mon1=(int(input("Dame moneda 1:")))
mon2=(int(input("Dame moneda 2:")))
mon3=(int(input("Dame moneda 3:")))
if (mon1>mon2):
    mayor=mon1 
else: 
    mayor=mon2
if (mon3>mayor):
    mayor=mon3
else:
    mayor=mayor 
print ("La moneda con mayor valor es: "+(str(mayor)))



#print(mon1+1)