import numpy as np
import cv2

class ImageModule():
    """Classe que contém as funções de processamento de imagem.
    Essa classe pode ser usada para processar imagens de qualquer fonte, como uma webcam ou um arquivo de vídeo.
    Recomenda-se que você crie uma classe que herde dessa classe e implemente os métodos que faltam para o seu projeto.
    """
    def __init__(self):
        self.kernel = None
    
    def color_filter(self, img: np.ndarray, lower: tuple, upper: tuple) -> np.ndarray:
        """Filtra a imagem de acordo com os valores de lower e upper

        Args:
            img (np.ndarray): Imagem a ser filtrada
            lower (tuple): Limite inferior
            upper (tuple): Limite superior

        Returns:
            mask (np.ndarray): Mascara binaria
        """
        pass # Pode remover essa linha
        # Desenvolva aqui
        return None
    
    def configure_kernel(self, kernel_size: int, type: str) -> None:
        """Configura o kernel para ser usado nas operações morfológicas

        Args:
            kernel_size (int): Tamanho do kernel
            type (str): rect (retangular), ellipse (elipse)
        """

        pass # Pode remover essa linha
        # Desenvolva aqui

    def morphological_transform(self, mask: np.ndarray, types: str) -> np.ndarray:
        """Realiza a operação morfológica selecionada na variável "types" na máscara "mask"

        Args:
            mask (np.ndarray): Máscara binária
            types (str): open (abertura), close (fechamento), erode (erosão), dilate (dilatação). Qualquer outra string não faz nada.

        Returns:
            mask (np.ndarray): Máscara binária transformada
        """

        if self.kernel is None:
            print("Kernel is not configured, call configure_kernel() first")
            return mask
        # Desenvolva aqui

        return mask

    def find_contours(self, mask: np.ndarray) -> list:
        """Baseado na máscara binária, encontra os contornos

        Args:
            mask (np.ndarray): Máscara binária

        Returns:
            contours (list): Lista de contornos
        """
        # Desenvolva aqui
        return None
    
    def order_contours(self, contours: list) -> list:
        """Ordena os contornos por área. O maior contorno deve ser o primeiro da lista.

        Args:
            contours (list): Lista de contornos

        Returns:
            contours (list): Lista de contornos ordenados
        """

        # Desenvolva aqui
        return None
    
    def contour_center(self, contour: list) -> tuple:
        """Retorna o centro de massa do contorno. Apenas de um contorno por vez.

        Args:
            contour (list): Contorno

        Returns:
            (cx, cy) (tuple(int, int)): Coordenadas do centro de massa
        """
        # Desenvolva aqui
        return None
    
    def contour_area(self, contour: list) -> float:
        """Retorna a área do contorno. Apenas de um contorno por vez.

        Args:
            contour (list): Contorno

        Returns:
            area (float): Area do contorno
        """
        # Desenvolva aqui
        return None
    
    def bounding_box(self, contour: list) -> tuple:
        """Retorna as coordenadas do retângulo que envolve o contorno. Apenas de um contorno por vez.

        Args:
            contour (list): Contorno

        Returns:
            (x, y, w, h) (tuple(int, int, int, int)): Coordenadas relevantes do retângulo. x e y são as coordenadas do canto superior esquerdo. w e h são a largura e altura do retângulo.
        """
        # Desenvolva aqui
        return None

    @staticmethod
    def draw_contours(img: np.ndarray, contours: list, color: tuple, thickness: int) -> np.ndarray:
        """Desenha os contornos na imagem

        Args:
            img (np.ndarray): Imagem a ser desenhada
            contours (list): Lista de contornos
            color (tuple): Cor do contorno
            thickness (int): Espessura do linha. -1 preenche o contorno

        Returns:
            img (np.ndarray): Imagem com os contornos desenhados
        """

        # Desenvolva aqui
        return None
    @staticmethod
    def draw_bounding_box(img: np.ndarray, x: int, y: int, w: int, h: int, color: tuple, thickness: int) -> np.ndarray:
        """Desenha um retângulo na imagem

        Args:
            img (np.ndarray): Imagem a ser desenhada
            x (int): Coordenada x do canto superior esquerdo
            y (int): Coordenada y do canto superior esquerdo
            w (int): Largura do retângulo
            h (int): Altura do retângulo
            color (tuple): Cor do retângulo
            thickness (int): Espessura do linha. -1 preenche o retângulo

        Returns:
            img (np.ndarray): Imagem com o retângulo desenhado
        """

        # Desenvolva aqui
        return None
    @staticmethod
    def cross_hair(img: np.ndarray, center: tuple, color: tuple, thickness: int) -> np.ndarray:
        """Desenha uma cruz na posição "center"

        Args:
            img (np.ndarray): Imagem a ser desenhada
            center (tuple): Posição da cruz
            color (tuple): Cor da cruz
            thickness (int): Espessura da linha

        Returns:
            img (np.ndarray): Imagem com a cruz desenhada
        """

        # Desenvolva aqui
        return None

def main():
    Module = ImageModule()
    
    # ABRA A IMAGEM
    
    # CONVERTA PARA HSV

    # USE A FUNÇÃO Module.color_filter(...) PARA FILTRAR A IMAGEM

    # MOSTRE A IMAGEM E A MÁSCARA FILTRADA EM JANELAS SEPARADAS


if __name__ == "__main__":
    # Esta função so é executada quando o arquivo é executado diretamente - ou seja, não é importado.
    main()