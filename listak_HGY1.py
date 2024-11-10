print("Adj meg gyümölcs neveket! Ha befejezted, írd be, hogy 'vége'.")

gyumolcsok = []

while True:

    gyumolcs = input("Adj meg egy gyümölcs nevet: ")

    if gyumolcs == "vége":
        break  

    if gyumolcs in gyumolcsok:
        print("Ez a gyümölcs már szerepel a listában!")
    else:
        gyumolcsok.append(gyumolcs)

print("\nA megadott gyümölcsök fordított sorrendben:")
for gyumolcs in gyumolcsok[::-1]: 
    print(gyumolcs, end=" ")