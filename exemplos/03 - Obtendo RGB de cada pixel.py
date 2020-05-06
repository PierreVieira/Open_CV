import cv2


def get_rgb(obj_img, x, y):
    return obj_img.item(y, x, 0), obj_img.item(y, x, 1), obj_img.item(y, x, 2)


def info_rgb_pixel(obj_img, altura, largura):
    for y in range(altura):  # Fixa a coluna
        for x in range(largura):  # Percorre a linha
            # azul, verde, vermelho = obj_img[y][x]  # Dá para fazer desse jeito, porém não é o mais recomendado
            azul, verde, vermelho = get_rgb(obj_img, x, y)
            print({'coordenada': (x, y), 'R': vermelho, 'G': verde, 'B': azul})


def main():
    obj_img = cv2.imread('../imgs/pierre_vieira_13_anos.jpg')
    altura, largura, canais_de_cor = obj_img.shape
    info_rgb_pixel(obj_img, altura, largura)


if __name__ == '__main__':
    main()
