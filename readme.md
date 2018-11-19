// 将hudong_pedia.csv 导入
LOAD CSV WITH HEADERS  FROM "file:///hudong_pedia.csv" AS line  
CREATE (p:HudongItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList,InfoKeyList:line.InfoKeyList,InfoValueList:line.InfoValueList}) 


// 新增了hudong_pedia2.csv
LOAD CSV WITH HEADERS  FROM "file:///hudong_pedia2.csv" AS line  
CREATE (p:HudongItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList,InfoKeyList:line.InfoKeyList,InfoValueList:line.InfoValueList}) 


//删除重复节点：

MATCH (e:HudongItem{title:'93'}) delete e	依次删除：'93','2','65',20','23','63','3','25','7','4'	重复10次


// 创建索引

CREATE CONSTRAINT ON (c:HudongItem)
ASSERT c.title IS UNIQUE


// 导入新的节点

LOAD CSV WITH HEADERS FROM "file:///new_node.csv" AS line
CREATE (:NewNode { title: line.title })


//添加索引

CREATE CONSTRAINT ON (c:NewNode)
ASSERT c.title IS UNIQUE


//导入植物节点
LOAD CSV WITH HEADERS  FROM "file:///plantAll.csv" AS line  
CREATE (p:PlantItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList,InfoKeyList:line.InfoKeyList,InfoValueList:line.InfoValueList}) 


//导入病害节点
LOAD CSV WITH HEADERS  FROM "file:///disAll.csv" AS line  
CREATE (p:DiseaseItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList,InfoKeyList:line.InfoKeyList,InfoValueList:line.InfoValueList}) 


//导入hudongItem和新加入节点之间的关系
LOAD CSV  WITH HEADERS FROM "file:///wikidata_relation2.csv" AS line
MATCH (entity1:HudongItem{title:line.HudongItem}) , (entity2:NewNode{title:line.NewNode})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)


LOAD CSV  WITH HEADERS FROM "file:///wikidata_relation.csv" AS line
MATCH (entity1:HudongItem{title:line.HudongItem1}) , (entity2:HudongItem{title:line.HudongItem2})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)


//导入植物和病害的中文（病害）关系：关系全但是不准
LOAD CSV  WITH HEADERS FROM "file:///plant_Disease_realation.csv" AS line
MATCH (entity1:HudongItem{title:line.HudongItem1}) , (entity2:HudongItem{title:line.HudongItem2})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)


//导入植物和病害的英文（illness）关系：关系准但是不全
LOAD CSV  WITH HEADERS FROM "file:///illnessRealation.csv" AS line
MATCH (entity1:HudongItem{title:line.HudongItem1}) , (entity2:HudongItem{title:line.HudongItem2})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)


//将attributes.csv放到neo4j的import目录下，然后执行
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

