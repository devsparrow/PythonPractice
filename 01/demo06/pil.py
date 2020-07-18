

import matplotlib.pyplot as plt
from PIL import Image

from PIL import Image, ImageDraw,ImageFont


img = Image.open('001.jpg')
plt.imshow(img)

# dst = img.rotate(45)
# plt.imshow(dst)


txt=Image.new('RGBA', img.size, (0,0,0,0))

fnt=ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 20)
d=ImageDraw.Draw(img)
d.text( (txt.size[0]-30,15), "20", font=fnt, fill=(255, 0, 0, 255))

img.show()


# plt.show()