fo = open("price2016bj.csv", "w")
ls = ['北京', '101.5', '120.7', '121.4']
fo.write(",".join(ls)+ "\n")
#生成一个新的字符串，他由字符串","分隔列表ls中的元素形成，再通过文件的write()方法存储到CSV文件中
fo.close()
#一维数据写入CSV文件