#使用 Python 生成类似于下图中的字母+数字验证码图片
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import string

#随机获取四个字母
def get_random_char(length =4):
    chars = string.ascii_letters + string.digits
    return [random.choice(chars) for _ in range(length)]

#获取颜色
def get_random_color():
    return (random.randint(30,100),random.randint(30,100),random.randint(30,100))

#获取验证码图片
def get_codepic():
    width = 240
    height = 60
    #创建画布
    image = Image.new('RGB',(width,height),(180,180,180))#画布大小
    font = ImageFont.truetype('C:/windows/fonts/Arial.ttf',size=40) #字体样式，大小
    draw = ImageDraw.Draw(image)
    #创建验证码图片
    code = get_random_char()
    #把验证码放到画布上
    for t in range(4):
        draw.text((60 * t + 10,0),code[t],font=font,fill=get_random_color())
    #填充噪点
    # for _ in range(random.randint(1500,3000)):
    #     draw.point((random.randint(0,width),random.randint(0,height)),fill = get_random_color())
    #模糊处理
    # image = image.filter(ImageFilter.BLUR)
    #保存名字为验证码的图片
    image.save('F:\学习内容\python_learn\Python图片转字符画\code.jpg','jpeg')

if __name__=="__main__":
    get_codepic()