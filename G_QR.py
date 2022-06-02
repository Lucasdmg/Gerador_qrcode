import qrcode

a=0
continuar = "sim"
while continuar == "sim":
    dado = str(input("Nome: >> "))
    img=qrcode.make(dado)
    img.save(f"{dado}{a}.png")
    continuar = str(input("Continuar: >> "))
    a+=1
