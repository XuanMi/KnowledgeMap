

import jieba

dis = {}
with open('PlantDis.csv','r',encoding='utf-8') as d:
    for dd in d:
        str = dd.strip().split(',')
        dis[str[0]] = str[0][1:-1]+str[4]

# for key in dis:
#     print(key,dis[key])

with open('plantAll.csv','r',encoding='utf-8') as p:
    with open('illnessRealation.txt','w',encoding='utf-8') as writefile:
            for pp in p:
                strp = pp.strip().split(',')[0]
                # print(strp)
                # entity = list(jieba.cut(strp))
                entity = []
                entity.append(strp)
                for e in entity:
                    if len(e) == 1:
                        entity.remove(e)
                for key in dis:
                    flag = 0
                    for i in entity:
                        if dis[key].find(i) >= 0:
                            if flag == 0:
                                print(strp+'  --->  '+key)
                                writefile.write(strp+','+'illness'+','+key+'\n')
                            flag = 1