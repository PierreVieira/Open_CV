import cv2
from matplotlib import pyplot as plt


def show_image(obj_img):
    obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)  # Convertendo BGR para RGB
    plt.imshow(obj_img)  # Carrega a imagem
    plt.show()  # Exibe a imagem


def main():
    obj_img = cv2.imread('../Resources/my_imgs/pierre_vieira.png')  # Lê a imagem
    show_image(obj_img)


if __name__ == '__main__':
    main()
