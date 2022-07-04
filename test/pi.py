from PIL import Image,ImageFont,ImageDraw
import os
from PIL import Image,ImageFont,ImageDraw
import pandas as pd

# text=str(pd.read_csv(r'D:\output.csv',encoding='gbk'))
text = u"这是一段测试文本，test 123。"
im = Image.new("RGB", (300, 50), (255, 255, 255))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 14)
dr.text((10, 5), text, font=font, fill="#000000")
im.show()
im.save(r'D:\output.png')