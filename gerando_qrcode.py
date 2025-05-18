import qrcode
from PIL import Image, ImageDraw, ImageFont
from teste_api import repositorios

def get_reposit(nome_repositorio):
    url = f"https://github.com/hmarinhoo/{nome_repositorio}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=3
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Criando imagem do QR code e convertendo para RGB
    img = qr.make_image(fill_color="pink", back_color="white").convert("RGB")

    # Adicionando texto embaixo da imagem
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 30)  
    except IOError:
        font = ImageFont.load_default()
    
    width, height = img.size
    text = nome_repositorio

    # Usar textbbox para medir o texto
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Criar nova imagem com espaço para o texto
    new_height = height + text_height + 20  # margem
    new_img = Image.new("RGB", (width, new_height), "white")
    new_img.paste(img, (0, 0))  # funciona agora porque img está em RGB

    # Escrever o texto na nova imagem
    draw_new = ImageDraw.Draw(new_img)
    position = ((width - text_width) // 2, height + 10)
    draw_new.text(position, text, fill="pink", font=font)

    # Salvando imagem final com texto
    new_img.save(f"qrcode_hmarinhoo_{nome_repositorio}.png")
    print(f"QR Code salvo: qrcode_{nome_repositorio}.png")

for repositorio in repositorios:
    get_reposit(repositorio["nome"])
