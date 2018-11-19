

list = ['医学','医学名词','疾病','妇科','中医','内科学','治疗','皮肤病','医院','血液病','卫生保健','病症','病理学','中医名词',
        '外科学','血液','人体解剖学名词','人体','骨科','怀孕','乳腺','人体','饮食','兽医','动物','禽病','口腔','男性','人畜共患病',
        '期刊','菜肴','国学','妇产科','中药','奶粉','红酒','粮食']


with open('disAll.csv','r',encoding='utf-8') as readfile:
    with open('PlantDis.csv','w',encoding='utf-8') as writefile:
        for line in readfile:
            flag = 1
            str = line.strip().split(',')[3].split('## ')
            print(str)
            for i in list:
                if i in str:
                    flag = 0
            if flag == 1:
                writefile.write(line)

# with open('PlantDis.csv','r',encoding='utf-8') as readfile:
#     for line in readfile:
#         flag = 1
#         str = line.strip().split(',')[3].split('## ')
#         print(str)
