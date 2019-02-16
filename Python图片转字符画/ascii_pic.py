# 1.首先使用 PIL 的 Image.open 打开图片文件，获得对象 im
# 2.使用 PIL 库的 im.resize() 调整图片大小对应到输出的字符画的宽度和高度，注意这个函数第二个参数使用 Image.NEAREST，表示输出低质量的图片。
# 3.遍历提取图片中每行的像素的 RGB 值，调用 getchar 转成对应的字符
# 4.将所有的像素对应的字符拼接在一起成为一个字符串 txt
# 5.打印输出字符串 txt
# 6.如果执行时配置了输出文件，将打开文件将 txt 输出到文件，如果没有，则默认输出到 output.txt 文件


#思考思路
#1.先测试获取图片的属性，高度、宽度，以及每一个像素点的RGB和alpha值


from PIL import Image

def getchar(r,g,b,alpha):
    if alpha==0:
        return ''

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    length=len(ascii_char)
    unit=(256+1)/length
    return ascii_char[gray//unit]

if __name__=="__main__":
    im = Image.open("ascii_dora.png")
    pic_width ,pic_height=im.size
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

    for x in range(pic_height):
        for y in range(pic_width):
            rgb_alpha=im.getpixel((x, y))
            pic_str=getchar(*rgb_alpha)
            print(pic_str)





