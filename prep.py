import main
from PIL import Image
import os

path = main.directory + r"\\"
dirs = os.listdir(path)

"""THIS RESIZES ALL IMAGES TO SATISY INSTAGRAM AND ORDERS THEM"""
def rename():
    count = 1
    for i, f in enumerate(dirs):
        src = os.path.join(path, f)
        dst = os.path.join(path, (f'{count:04}' + ".jpg"))
        os.rename(src, dst)
        count += 1


def resize():
    for item in dirs:
        print(item)
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((800, 1000))
            imResize.save(f + '.jpg', 'JPEG', quality=100)


resize()
rename()
