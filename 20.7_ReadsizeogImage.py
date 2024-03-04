# Python program to find the size (Resolution) of a Image.
# You will learn to find the resolution of a jpej image in this example without using external libraries.

# JPEG: Jay-Peg stand for Joint photographic Experts Group

def jpej_res(filename):
    # this function prints the resolution of the jpeg image file.
    with open(filename, 'rb') as img_file:
        # height of the image(in 2 bytes) is at 164th position:
        img_file.seek(163)

        # Read the 2 bytes
        L = img_file.read(2)

        # Calculate Height
        height = (L[0] << 8) + L[1]

        # Next 2 bytes is width
        E = img_file.read(2)

        # Calculate width
        width = (E[0] << 8) + E[1]
    print("The resolution of the image is", width, "x", height)

jpej_res("Saurabh.jpg")