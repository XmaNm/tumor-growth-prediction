import os
from PIL import Image
from array import *
from random import shuffle

Names = [['./nodule/train', 'train'], ['./nodule/test', 'test']]

for name in Names:

    data_image = array('B')
    data_label = array('B')
    FileList = []
    for dirname in os.listdir(name[0])[1:]:
        path = os.path.join(name[0], dirname)
        for filename in os.listdir(path):
            if filename.endswith(".jpg"):
                FileList.append(os.path.join(name[0], dirname, filename))

    shuffle(FileList)
    for filename in FileList:
        if name == ['./nodule/train', 'train']:
            label = int(filename[15])
        else:
            label = int(filename[14])
        im = Image.open(filename)
        pixel = im.load()
        width, height = im.size
        for x in range(0, width):
            for y in range(0, height):
                data_image.append(pixel[y, x])
        data_label.append(label)

    hexval = "{0:#0{1}x}".format(len(FileList), 6)
    header = array('B')
    header.extend([0,0,8,1,0,0])
    header.append(int('0x'+hexval[2:][:2],16))
    header.append(int('0x'+hexval[2:][2:],16))
    data_label = header + data_label

    if max([width, height]) <= 256:
        header.extend([0,0,0,width,0,0,0,height])
    else:
        raise ValueError('Image exceeds maximun size: 256*256')
    header[3] = 3
    data_image = header + data_image
    outout_file = open(name[1]+'-images-idx3-ubyte','wb')
    data_image.tofile(outout_file)
    outout_file.close()

    outout_file = open(name[1]+'-labels-idx1-ubyte','wb')
    data_label.tofile(outout_file)
    outout_file.close()

for name in Names:
    os.system('gzip ' + name[1] + '-images-idx3-ubyte')
    os.system('gzip ' + name[1] + '-labels-idx1-ubyte')