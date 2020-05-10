import cv2
from matplotlib import pyplot as plt


def show_image(img):
    obj_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Faz a conversão de BGR para RGB
    plt.imshow(obj_img)
    plt.show()  # Exibe a janela gráfica


def set_color(obj_img, x, y, vermelho, verde, azul):
    obj_img.itemset((y, x, 0), azul)
    obj_img.itemset((y, x, 1), verde)
    obj_img.itemset((y, x, 2), vermelho)


def get_color(obj_img, x, y):
    return obj_img.item(y, x, 0), obj_img.item(y, x, 1), obj_img.item(y, x, 2)


def deixar_azulado(obj_img, altura, largura):
    for y in range(altura):
        for x in range(largura):
            azul, verde, vermelho = get_color(obj_img, x, y)
            set_color(obj_img, x, y, 0, 0, azul)


def main():
    obj_img = cv2.imread('../resources/my_imgs/pierre_vieira_13_anos.jpg')  # Vai ler a imagem
    altura, largura, canais_de_cor = obj_img.shape
    deixar_azulado(obj_img, altura, largura)
    show_image(obj_img)


if __name__ == '__main__':
    main()
