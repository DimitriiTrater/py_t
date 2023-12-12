from PIL import Image, ImageDraw

START_POS = (0, 0)

if __name__ == "__main__":
    size_x, size_y = (int(i) for i in input("plz enter size of image(x, y): ")
                      .split())

    new_im = Image.new(mode="RGB", size=(size_x, size_y), color="snow")
    draw = ImageDraw.Draw(new_im)
    draw.line(START_POS + new_im.size, fill=128)
    draw.line((0, new_im.size[1], new_im.size[0], 0), fill=128)

    rect = [(size_x * 0.2, size_y * 0.2), (size_x * 0.5, size_y * 0.5)]
    draw.rectangle(rect, fill="red")

    rect = [(size_x * 0.5, size_y * 0.5), (size_x * 0.8, size_y * 0.8)]
    draw.rectangle(rect, fill="blue")

    new_im.show()
