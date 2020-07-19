# https://github.com/Yixiaohan/show-me-the-code
# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

import matplotlib.pyplot as plt
from PIL import Image

from PIL import Image, ImageDraw,ImageFont

import random


print(random.randint(0,9))


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