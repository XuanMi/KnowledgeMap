

list = []
def hudong():
    with open('hudong_pedia2.csv','r',encoding='utf-8') as readfile:
        with open('disease.txt','r',encoding='utf-8') as disease:
            with open('diseaseDetail.csv','a',encoding='utf-8') as diseaseDetail:
                for dis in disease:
                    d = dis.strip().split(' ')[0]
                    list.append(d)
                for line in readfile:
                    str = line.strip().split(',')[0][1:-1]
                    if str in list:
                        diseaseDetail.write(line)

hudong()





