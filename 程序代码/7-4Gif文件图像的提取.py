from PIL import Image
im = Image.open('pybit.gif')      # 读入一个GIF文件
print(im.format,im.size,im.mode)
try:
    im.save('picframe{:02d}.png'.format(im.tell()))#返回当前帧的序号Image.seek()Image.tell
    while True:
        im.seek(im.tell()+1)                       #跳转并返回图像中的指定帧Image.seek()
        im.save('picframe{:02d}.png'.format(im.tell()))
except:
    print("处理结束")
