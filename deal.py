# -*- coding=utf-8 -*-
import csv    #加载csv包便于读取csv文件
def loaddata(file):
    csv_file = open(file, encoding='utf8')  # 打开csv文件
    csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
    data = []  # 创建列表准备接收csv各行数据
    for one_line in csv_reader_lines:
        judge=True
        for i in one_line:
            if i=='-':
                judge=False
        if judge:
            data.append(one_line)  # 将读取的csv分行数据按行存入列表‘date’中
    return data
def procsv(file,c,index):
    data=loaddata(file)
    # 1. 创建文件对象
    f = open(data[0][index]+'.csv', 'w', encoding='utf-8', newline='')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头
    csv_writer.writerow([data[0][index], "value", "label"])
    # 4. 写入csv文件内容
    for i in range(1,len(data)):
        csv_writer.writerow([c+str(i),data[i][index] ,data[0][index]])
    # 5. 关闭文件
    f.close()
def pro10csv(file,c):
    data=loaddata(file)
    data10=[]
    for i in data:
        if not i[10] in data10:
            data10.append(i[10])
    data10.sort()
    # 1. 创建文件对象
    f = open(data10[0]+'.csv', 'w', encoding='utf-8', newline='')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头
    csv_writer.writerow([data10[0], "name", "label"])
    # 4. 写入csv文件内容
    for i in range(1,len(data10)):
        csv_writer.writerow([c+str(i),data10[i] ,data10[0]])
    # 5. 关闭文件
    f.close()
def prostokecsv(file):
    data=loaddata(file)
    # 1. 创建文件对象
    f = open('stock.csv', 'w', encoding='utf-8', newline='')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头
    csv_writer.writerow([data[0][0], data[0][1], "label"])
    # 4. 写入csv文件内容
    for i in range(1,len(data)):
        csv_writer.writerow([data[i][0], data[i][1],"stock"])
    # 5. 关闭文件
    f.close()
def prorelationcsv(file):
    data=loaddata(file)
    data10 = []
    for i in data:
        if not i[10] in data10:
            data10.append(i[10])
    data10.sort()
    # 1. 创建文件对象
    f = open('relatiom.csv', 'w', encoding='utf-8')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头
    csv_writer.writerow(["start", "end", "type"])
    # 4. 写入csv文件内容
    lineLabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(1,len(data)):
        for j in range(2,10):
            csv_writer.writerow([data[i][1],lineLabe[j-2]+str(i) ,"owner to"])
        csv_writer.writerow([data[i][1], 'L'+str(data10.index(data[i][10])), "belong to"])
    # 5. 关闭文件
    f.close()

if __name__ == '__main__':
    lineLabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(2, 10):
        procsv("eastmoney_simple.csv", lineLabe[i - 2], i)
    pro10csv("eastmoney_simple.csv",'L')
    prostokecsv("eastmoney_simple.csv")
    prorelationcsv("eastmoney_simple.csv")
    files = ['stock.csv', 'relatiom.csv', 'quote_change.csv', 'price_cash_rate.csv', 'PEG.csv', 'PE_TTM.csv', 'PE_static.csv'
             , 'PB_ratio.csv', 'market_sales_rate.csv', 'latest_price.csv', 'industry.csv']
    for file in files:
        with open(file, 'r', encoding='utf8') as f:
            lines = f.readlines()
        with open(file, 'w', encoding='utf8') as f:
            for line in lines:
                if len(line) > 1:
                    f.write(line)
    files = ['a.csv', 'b.csv', 'c.csv', 'd.csv', 'e.csv', 'f.csv', 'g.csv', 'h.csv', 'L.csv']
    files = [csv.writer(open(file, mode='w', encoding='utf8', newline='')) for file in files]
    for file in files:
        file.writerow(['from', 'to', 'type'])
    char2files = {'a': files[0], 'b': files[1], 'c': files[2], 'd': files[3], 'e': files[4], 'f': files[5],
                  'g': files[6], 'h': files[7], 'L': files[8]}
    relation = open('relatiom.csv', mode='r', encoding='utf8')
    relations = list(csv.reader(relation))[1:]
    for relation in relations:
        char2files[relation[1][0]].writerow(relation)