from PIL import Image, ImageFont, ImageDraw

def main(img):
     im = Image.open(img)
     im.show()
     w, h = im.size
     #font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-R.ttf', 30)
     fillcolor = "#ff0000"
     draw = ImageDraw.Draw(im)
     draw.text((w - 20, 0), '1', fill=fillcolor)
     im.save('r.jpg', 'jpeg')


main('1.jpg')