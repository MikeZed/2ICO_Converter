
from PIL import Image
import os

source = r"Icons\To Be Converted"
destination = r"Icons"


def main():

    img_converter = ImageConverter(source, destination)
    img_converter.convert()


class ImageConverter:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def convert(self):
        img_list = os.listdir(self.source)

        for img_file in img_list:
            img_name = img_file.split('.')[0]

            img=Image.open(self.source+"\\"+img_file)
            img.save(self.destination+"\\"+img_name+".ico")


if __name__ == "__main__":
    main()