// ��hudong_pedia.csv ����
LOAD CSV WITH HEADERS  FROM "file:///hudong_pedia.csv" AS line  
CREATE (p:HudongItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList,InfoKeyList:line.InfoKeyList,InfoValueList:line.InfoValueList}) 

// ������hudong_pedia2.csv
LOAD CSV WITH HEADERS  FROM "file:///hudong_pedia2.csv" AS line  
CREATE (p:HudongItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList,InfoKeyList:line.InfoKeyList,InfoValueList:line.InfoValueList}) 

//ɾ���ظ��ڵ㣺
MATCH (e:HudongItem{title:'93'}) delete e	����ɾ����'93','2','65',20','23','63','3','25','7','4'	�ظ�10��

// ��������
CREATE CONSTRAINT ON (c:HudongItem)
ASSERT c.title IS UNIQUE

// �����µĽڵ�
LOAD CSV WITH HEADERS FROM "file:///new_node.csv" AS line
CREATE (:NewNode { title: line.title })

//�������
CREATE CONSTRAINT ON (c:NewNode)
ASSERT c.title IS UNIQUE

//����ֲ��ڵ�
LOAD CSV WITH HEADERS  FROM "file:///plantAll.csv" AS line  
CREATE (p:PlantItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList,InfoKeyList:line.InfoKeyList,InfoValueList:line.InfoValueList}) 

//���벡���ڵ�
LOAD CSV WITH HEADERS  FROM "file:///disAll.csv" AS line  
CREATE (p:DiseaseItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList,InfoKeyList:line.InfoKeyList,InfoValueList:line.InfoValueList}) 

//����hudongItem���¼���ڵ�֮��Ĺ�ϵ
LOAD CSV  WITH HEADERS FROM "file:///wikidata_relation2.csv" AS line
MATCH (entity1:HudongItem{title:line.HudongItem}) , (entity2:NewNode{title:line.NewNode})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)

LOAD CSV  WITH HEADERS FROM "file:///wikidata_relation.csv" AS line
MATCH (entity1:HudongItem{title:line.HudongItem1}) , (entity2:HudongItem{title:line.HudongItem2})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)

//����ֲ��Ͳ��������ģ���������ϵ����ϵȫ���ǲ�׼
LOAD CSV  WITH HEADERS FROM "file:///plant_Disease_realation.csv" AS line

MATCH (entity1:HudongItem{title:line.HudongItem1}) , (entity2:HudongItem{title:line.HudongItem2})

CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)

//����ֲ��Ͳ�����Ӣ�ģ�illness����ϵ����ϵ׼���ǲ�ȫ
LOAD CSV  WITH HEADERS FROM "file:///illnessRealation.csv" AS line

MATCH (entity1:HudongItem{title:line.HudongItem1}) , (entity2:HudongItem{title:line.HudongItem2})

CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)

//��attributes.csv�ŵ�neo4j��importĿ¼�£�Ȼ��ִ��
LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:HudongItem{title:line.Entity}), (entity2:HudongItem{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2);
                                                            
LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:HudongItem{title:line.Entity}), (entity2:NewNode{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2);
                                                            
LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:NewNode{title:line.Entity}), (entity2:NewNode{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2);
                                                            
LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:NewNode{title:line.Entity}), (entity2:HudongItem{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2)  

