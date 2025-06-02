from PIL import Image
#importing the nessecary packages


# defining functions
images = []

#The function for merging two images left-to-right
def merge(im1: Image.Image, im2: Image.Image) -> Image.Image:
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im

#the function for merging two images top-and-bottom
def topmerge(im1: Image.Image, im2: Image.Image) -> Image.Image:
    h = im1.size[1] + im2.size[1]
    w = max(im1.size[0], im2.size[0])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (0, im1.size[1]))

    return im

#the functions for the seven frieze patterns
def p1(img: Image.Image) -> Image.Image:
    add_img = img
    for i in range(8):
        img = merge(img, add_img)

    return img

def p1m1(img: Image.Image) -> Image.Image:
    flipimg = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    img = merge(img, flipimg)
    for i in range(2):
        img = merge(img, img)

    return img

def p11m(img: Image.Image) -> Image.Image:
    img = p1(img)
    img = topmerge(img, img.transpose(Image.Transpose.FLIP_TOP_BOTTOM))
    
    return img

def  p2mm(img: Image.Image) -> Image.Image:
    img = p1m1(img)
    img = topmerge(img, img.transpose(Image.Transpose.FLIP_TOP_BOTTOM))
    
    return img

def p2(img: Image.Image)-> Image.Image:
    strip = merge(img, img.transpose(Image.Transpose.ROTATE_180))
    strip = merge(strip, strip)
    strip = merge(strip, strip)

    return strip

def p11g(img: Image.Image)-> Image.Image:
    strip = merge(img, img.transpose(Image.Transpose.FLIP_TOP_BOTTOM))
    strip = merge(strip, strip)
    strip = merge(strip, strip)
    
    return strip

def p2mg(img: Image.Image) -> Image.Image:
    strip = merge(img, img.transpose(Image.Transpose.ROTATE_180))
    strip = merge(strip, strip.transpose(Image.Transpose.FLIP_LEFT_RIGHT))
    strip = merge(strip, strip)

    return strip

def game():
    filename = input('''please enter the name of your chosen image, and make sure that it is in
    the same folder as this code. Example: "Knight.png".''')
    for i in images:
        if filename == i:
            print("You have already used this image before")
    images.append(filename)

    filename = Image.open(filename)

    pattern = input('''which of the 7 frieze patterns would you like this code to output?
    The Seven Frieze patterns are:
        p1, p1m1, p11m, p2mm, p2, p11g,  and p2mg''')
    if pattern == "p1":
        filename = p1(filename)
        filename.show()
    if pattern == "p1m1":
        filename = p1m1(filename)
        filename.show()
    if pattern == "p11m":
        filename = p11m(filename)
        filename.show()
    if pattern == "p2mm":
        filename = p2mm(filename)
        filename.show()
    if pattern == "p2":
        filename = p2(filename)
        filename.show()
    if pattern == "p11g":
        filename = p11g(filename)
        filename.show()
    if pattern == "p2mg":
        filename = p2mg(filename)
        filename.show()
    
    #asking the player if they would like to play again
    playagain = input("Do you want to play again? If yes, type 'Y', if no type 'N'")
    if playagain == 'Y':
        game()


# calling the procedure to run the game
game()
