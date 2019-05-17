fo = open("price2016.csv", "r")
ls = []
for line in fo:
    line = line.replace("\n","")  #内置的字符串处理函数
    ls.append(line.split(","))
print(ls)
fo.close()
