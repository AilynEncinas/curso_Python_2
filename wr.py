import qrcode
img = qrcode.make('Hola niño')
type(img)  # qrcode.image.pil.PilImage
img.save("sjsksjk.png")
