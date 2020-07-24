
from PIL import Image
import os

source = r"Icons\To Be Converted"
destination = r"Icons"
destination_format = ".png"


def main():

    img_converter = ImageConverter(source, destination, destination_format)
    img_converter.convert()


class ImageConverter:
    def __init__(self, src, dest, dest_format=".ico"):
        self.source = src
        self.destination = dest
        self.destination_format = dest_format

    def convert(self):
        img_list = os.listdir(self.source)

        for img_file in img_list:
            img_name = img_file.split('.')[0]

            img=Image.open(self.source+"\\" + img_file)
            img.save(self.destination+"\\" + img_name + self.destination_format)


if __name__ == "__main__":
    main()
