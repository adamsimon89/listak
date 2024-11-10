print("Adjon meg olyan szavakat, amelyek kis 'a' vagy nagy 'A' betűvel kezdődnek!")
print("Ha nem 'a' vagy 'A' betűvel kezdődik egy szó, a program figyelmen kívül hagyja.")
print("Program megszakításához nyomjon enter-t.")


szavak = []

while True:
    szo = input("Adjon meg egy szót: ")

    if szo == "":
        break
    

    if szo[0] == "a" or szo[0] == "A":
        szavak = szavak + [szo]  

print("\nA bekért szavak, amelyek 'a' vagy 'A' betűvel kezdődnek:")
for szo in szavak:
    print(szo)