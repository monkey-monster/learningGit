from PIL import Image
im = Image.open('birdnest.jpg')

im.save( "birdnest","png")    #将图像保存为文件名，图片格式 im.save( "birdnest.png")
im.thumbnail((300,500))    #创建图像的缩略图
r, g, b = im.split()        #获得RGB通道数据
om = Image.merge("RGB", (b, g, r))  #合并通道 （色彩，新的色彩通道）
om.save('birdnestBGR.jpg')
