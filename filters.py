from loguru import logger
from PIL import Image, ImageFilter


class my_filter:
    @staticmethod
    def get():
        size = (3, 3)
        kernel = (-1, -1, -1, -1, 11, -2, -2, -2, -2)
        scale = 1
        offset = 0
        return ImageFilter.Kernel(size, kernel, scale, offset)


if __name__ == "__main__":
    try:
        original = Image.open("pictures/nturaone.jpg")
    except FileNotFoundError:
        logger.error("Файл не найден")
        exit(0)
    im = original.filter(my_filter.get())
    im.show()
