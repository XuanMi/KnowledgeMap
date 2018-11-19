

list = []
with open('plant.txt','r',encoding='utf-8') as disease:
    for dis in disease:
        d = dis.strip().split(' ')[0]
        list.append(d)



with open('hudong_pedia2.csv','r',encoding='utf-8') as readfile:
        with open('plantAll.csv','a',encoding='utf-8') as diseaseDetail:
            for line in readfile:
                str = line.strip().split(',')[0]
                if str in list:
                    diseaseDetail.write(line)







