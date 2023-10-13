from PIL import Image,ImageFilter
with Image.open("2824384.jpg") as original:
    print(original.size)
    print(original.format)
    print(original.mode)

    ab_original = original.convert("L")
    #ab_original.show()

    blur_origignal = original.filter(ImageFilter.BLUR)
    #blur_origignal.show()

    #lef_orig = original.transpose(Image.ROTATE_90)
    #lef_orig.show()

