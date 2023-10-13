from PIL import Image,ImageFilter
class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.edited = []

    def open(self):
        try:
            self.original = Image.open(self.filename)
            self.original.show()
        except:
            print("Такого нема")

    def do_left(self):
        left = self.original.transpose(Image.ROTATE_90)
        self.edited.append(left)
        left.show()
        left.save("left_" + self.filename)

    def bw(self):
        bw = self.original.convert("L")
        self.edited.append(bw)

        bw.save("bw_" + self.filename)
img = ImageEditor("2824384.jpg")

img.open()
img.do_left()
img.bw()