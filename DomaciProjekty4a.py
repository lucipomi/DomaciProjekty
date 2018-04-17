#Domaci ukol c.5
for a in range(4):
    print("a")

#Domaci ukol c.6
cisla_radku = [0 ,1 ,2 ,3 ,4]
for cislo in cisla_radku:
    print("Radek"+str(cislo))

#Domaci ukol c.8
x = [0, 1, 2, 3, 4]
for x in x:
    print(str(x)+" na duhou je "+str(x**2))

#Domaci ukol c.9
#Jiny zpusob bez END, jelikoz se mi END nelibi :-)
#    for x in range(5):
#        print(5*"x")

for x in range(5):
    print(5*"x ", end="\n")


#Domaci ukol c.10
for i in range(0,5):
    for j in range (0,5):
        tmp=str(i*j)
        print(tmp, end=" ")
    print("\n")
