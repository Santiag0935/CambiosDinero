print("En este programa convertiremos el monto ingresado de pesos mexicanos a dolares americanos, dolares canadienses, yenes, rupias, colones, euros, pesetas españolas y marcos alemanes")
print()
mx= float(input("Ingrese un monto de pesos mexicanos: "))
while mx<0:
    print()
    print("Monto no valido. Debe ingresar un monto positivo.")
    print()
    mx= float(input("Ingrese un monto de pesos mexicanos: "))
print()
m1= "Dolar americano (USD) "
usd= 0.045
mxd= mx*usd
m2= "Dolar canadiense (CAD)"
cad= 0.061
mxc= mx*cad
m3= "Yenes (JPY)           "
jpy= 4.79
mxj= mx*jpy
m4= "Rupias (INR)          "
inr= 3.34
mxi= mx*inr
m5= "Colones (CRC)         "
crc= 27.06
mxco= mx*crc
m6= "Euros (EUR)           "
eur= 0.39
mxe= mx*eur
m7= "Peseta española (ESP) "
esp= 6.39
mxp= mx*esp
m8= "Marcos alemanes (DEM) "
dem= 0.08
mxde= mx*dem
print("{:^15} {:^38}".format("MONEDA","EQUIVALENCIA"))
print("{:^15} {:^25,.2f}".format(m1,mxd))
print("{:^15} {:^25,.2f}".format(m2,mxc))
print("{:^15} {:^25,.2f}".format(m3,mxj))
print("{:^15} {:^25,.2f}".format(m4,mxi))
print("{:^15} {:^25,.2f}".format(m5,mxco))
print("{:^15} {:^25,.2f}".format(m6,mxe))
print("{:^15} {:^25,.2f}".format(m7,mxp))
print("{:^15} {:^25,.2f}".format(m8,mxde))
