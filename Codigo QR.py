import qrcode 

def generar_qr (texto):
    qr = qrcode.make(texto)
    qr.save("codigo_qr.png")
    print("Codigo QR generado con exito")
    
texto = input("Texto: ")
generar_qr(texto)