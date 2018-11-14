



with open('predict_labels_full.txt','r',encoding='utf-8') as readfile:
    with open('plant.txt','w',encoding='utf-8') as plant:
        with open('disease.txt','w',encoding='utf-8') as disease:
            for line in readfile:
                key,value = line.strip().split(' ')
                if int(value) == 6:
                    plant.write(key+'\n')
                if int(value) == 10:
                    disease.write(key+'\n')