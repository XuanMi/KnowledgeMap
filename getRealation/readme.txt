PlantDis：植物病害
PlantAll：植物详情

createDetail.py:    分别获取互动百科里，植物和病害详情
model.py:            1.通过病害title和detail拼接与植物的title进行比较，如果包含在内，则有关系（关系准确但并不全）illnessRealation.txt
	            2.通过病害title和detail拼接与植物的title（分词后）进行比较，如果包含在内，则有关系（关系全面但不准）plant_Disease_realation.txt
	               plant_Disease_realation_CN.txt为中文病害的关系