import cv2
from matplotlib import pyplot as plt


def show_image(img):
    obj_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Faz a inversão de vermelho e verde
    plt.imshow(obj_img)  # Constroi a janela gráfica
    plt.show()  # Exibe a janela gráfica


def get_color(obj_img, x, y):
    return obj_img.item(y, x, 0), obj_img.item(y, x, 1), obj_img.item(y, x, 2)


def set_color(obj_img, x, y, vermelho, verde, azul):
    obj_img.itemset((y, x, 0), azul)
    obj_img.itemset((y, x, 1), verde)
    obj_img.itemset((y, x, 2), vermelho)


def percorrer_imagem(obj_img, altura, largura):
    for y in range(altura):
        for x in range(largura):
            azul, verde, vermelho = get_color(obj_img, x, y)
            set_color(obj_img, x, y, azul, vermelho, verde)


def main():
    obj_img = cv2.imread('../imgs/pierre_vieira_13_anos.jpg')  # Vai ler a imagem, o valor opcional 0 deixa preto e branco
    try:
        altura, largura, canais_de_cor = obj_img.shape  # Carrega a largura, altura e canais de cor
    except ValueError:
        altura, largura = obj_img.shape
    else:
        print(f'Canais de cor: {canais_de_cor}')
    print(f'Dimensões da imagem {largura} x {altura}')
    percorrer_imagem(obj_img, altura, largura)
    show_image(obj_img)


if __name__ == '__main__':
    main()
