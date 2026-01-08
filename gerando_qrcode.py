import qrcode
from PIL import Image, ImageDraw, ImageFont
from teste_api import repositorios
import os

# Pasta onde os QR Codes serão salvos
OUTPUT_DIR = "qrcodes"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def gerar_qrcode_repositorio(nome_repositorio, usuario="hmarinhoo"):
    # Monta a URL do repositório
    url = f"https://github.com/{usuario}/{nome_repositorio}"
    nome_arquivo = os.path.join(
        OUTPUT_DIR,
        f"qrcode_{usuario}_{nome_repositorio.replace(' ', '_')}.png"
    )

    # Cria o QR Code com personalização de cores
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=3
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#ff91b2", back_color="white").convert("RGB")

    # Tenta carregar uma fonte, senão usa a padrão
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()

    # Medidas da imagem e do texto
    width, height = qr_img.size
    draw_temp = ImageDraw.Draw(qr_img)
    bbox = draw_temp.textbbox((0, 0), nome_repositorio, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Cria uma nova imagem maior para incluir o texto
    new_height = height + text_height + 20
    image_final = Image.new("RGB", (width, new_height), "white")
    image_final.paste(qr_img, (0, 0))

    # Escreve o nome do repositório centralizado abaixo do QR
    draw_final = ImageDraw.Draw(image_final)
    position = ((width - text_width) // 2, height + 10)
    draw_final.text(position, nome_repositorio, fill="#ff91b2", font=font)

    # Salva a imagem
    image_final.save(nome_arquivo)
    print(f"QR Code salvo como: {nome_arquivo}")


# Vai percorrer a lista repositórios e criar um qrcpode para cada item da lista.
def main():
    for repositorio in repositorios:
        gerar_qrcode_repositorio(repositorio["nome"])

if __name__ == "__main__":
    main()
