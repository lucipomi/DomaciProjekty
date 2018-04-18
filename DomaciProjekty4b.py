#Domaci ukol c. 11

for X in range(1):
    for j in range(1,5):
        print("X "*j)
    printend=("\n")


#Domaci ukol c.12
for radek in range(1,5):
    if radek in range(1,2):
        print("Prvni radek")
    if radek in range(2,5):
        print("Neni prvni")

#Domaci ukol c.13
for radek in range(1,7):
    if radek in range(1,2):
        print(6*"X ")
    if radek in range(2,6):
        print("X         X")
    if radek in range(6,7):
        print(6*"X ")

#Domaci ukol c.14
x=int(input("Zadej velikost ctverce: "))

for i in range(0,x):
    for j in range(0,x):
        if (j==0 or j==x-1 or i==x-1 or i==0):
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print("\n", end="")
