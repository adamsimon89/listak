print("Adj meg olyan szavakat amelyek kis 'a' betűvel kezdődik")
print("Ha nem 'a' betűvel kezdődik a szó akkor a program figyelmen kívül hagyja.")
print("A program befejezéséhez nyomjon enter-t")

szavak = []

while True:

    szo = input("Adjon meg egy szót: ")
    
    if szo == "":
        break
    

    if szo[0] == "a":
        szavak = szavak + [szo]  


print("\nA bekért szavak, amelyek kis 'a' betűvel kezdődnek:")
for szo in szavak:
    print(szo)