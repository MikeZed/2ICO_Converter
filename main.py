
from PIL import Image

folder_to_convert = r'E:\My Stuff\Images\Icons\g.png'
destination = r'E:\My Stuff\Images\Icons\g.ico'


def main():

    # if destination doesnt exist create folder

    # check files in folder, open, convert, save

    # add converting class


    img = Image.open(folder_to_convert)
    img.show()
    print(img)
    img.save(destination)



class Image_Converter:
    pass





if __name__== "__main__":

    main()