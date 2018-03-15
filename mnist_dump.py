import os
from PIL import Image
import chainer

def save(data, index, num):
    img = Image.new("L", (28, 28))
    pix = img.load()
    for i in range(28):
        for j in range(28):
            pix[i, j] = int(data[i+j*28]*256)
    img2 = img.resize((280, 280))
    filename = str(num) + "/test" + "{0:04d}".format(index) + ".png"
    img2.save(filename)
    print filename

def main():
    _, test = chainer.datasets.get_mnist()
    for i in range(10):
        dirname = str(i)
        if os.path.isdir(dirname) is False:
            os.mkdir(dirname)
    for i in range(100):
        save(test[i][0], i, test[i][1])

if __name__ == '__main__':
    main()
