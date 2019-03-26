from PIL  import Image,ImageFont,ImageDraw
import numpy as np
from pylab import *
import cv2
def makecarnum(str):
    fontchinese = ImageFont.truetype('simhei.ttf',250)#使用自定义的字体，第二个参数表示字符大小
    font = ImageFont.truetype('font.ttf', 310)
    im = Image.open('t.bmp')
    draw = ImageDraw.Draw(im)#绘图句柄

    xc,yc=(15,75) #初始左上角的坐标
    x, y = (35, 45)
    draw.text((xc,yc), str[0], font=fontchinese)#绘图M
    offsetx, offsety = fontchinese.getoffset(str[0])  # 获得文字的offset位置
    width, height = fontchinese.getsize(str[0])  # 获得文件的大小
    draw.text((offsetx+x+width, y), str[1:], font=font)
    im = np.array(im)

    pos=[]
    for i in range(len(str)):
        if i==0:
            offsetx, offsety = fontchinese.getoffset(str[i])  # 获得文字的offset位置
            width, height = fontchinese.getsize(str[i])  # 获得文件的大小
            rect=[offsetx+x,offsety+y,offsetx+x+width,offsety+y+height]
        else:
            offsetx, offsety = font.getoffset(str[i])  # 获得文字的offset位置
            width, height = font.getsize(str[i])  # 获得文件的大小
            rect=[pos[i-1][2],pos[i-1][1],pos[i-1][2]+width,pos[i-1][3]]
        # cv2.rectangle(im, (rect[0], rect[1]), (rect[2], rect[3]), (255, 255, 255), 1)
        pos.append(rect)
    imshow(im)
    show()
    imsave("img/"+str+'.png',im)
    # np.savetxt(str+'.txt',pos)#保存左上和右下


chars = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"A",
             u"B", u"C", u"D", u"E", u"F", u"G", u"H", u"J", u"K", u"L", u"M", u"N", u"P", u"Q", u"R", u"S", u"T", u"U", u"V", u"W", u"X",
             u"Y", u"Z"]
chinachars=[u"京", u"沪", u"津", u"渝", u"冀", u"晋", u"蒙", u"辽", u"吉", u"黑", u"苏", u"浙", u"皖", u"闽", u"赣", u"鲁", u"豫", u"鄂", u"湘", u"粤", u"桂",
             u"琼", u"川", u"贵", u"云", u"藏", u"陕", u"甘", u"青", u"宁", u"新",u"港",u"学",u"使",u"警",u"澳",u"挂",u"军",u"北",u"南",u"广",u"沈",u"兰",u"成",u"济",u"海",u"民",u"航",u"空"]
print(np.random.randint(0, 2))
str=''
print(len(chars),len(chinachars))
for i in range(7):
    if i==0:
        str=str+chinachars[np.random.randint(0, 50)]
    else:
        str = str +chars[np.random.randint(0, 35)]
makecarnum(str)