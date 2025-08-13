from PIL import Image
# caminhos das imagens
foto_path = "img/memphis.jpg"
overlay_path = "img/img_rosa.png"

def gerar_foto(foto_path, overlay_path):
    foto = Image.open(foto_path).convert("RGBA")
    overlay = Image.open(overlay_path).convert("RGBA")

    # tamanho do círculo aproximado (baseado no seu PNG)
    circulo_diametro = 900  # ajuste conforme necessário
    circulo_pos = (overlay.size[0]//2+150, overlay.size[1]//2-50)  # centro do círculo

    # redimensiona a foto para caber no círculo
    foto_redimensionada = foto.resize((circulo_diametro, circulo_diametro))

    # cria uma imagem vazia para colocar a foto na posição correta
    resultado_base = Image.new("RGBA", overlay.size, (0, 0, 0, 0))

    # deslocamento (offset)
    offset_x = circulo_pos[0] - (circulo_diametro // 2)
    offset_y = circulo_pos[1] - (circulo_diametro // 2) - 50  # -50 joga a imagem pra cima

    # cola a foto posicionada
    resultado_base.paste(foto_redimensionada, (offset_x, offset_y))

    # aplica o overlay por cima
    resultado = Image.alpha_composite(resultado_base, overlay)

    # salvar resultado final
    resultado.save("pronta.png")
