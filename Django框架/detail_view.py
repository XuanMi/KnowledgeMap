# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
import thulac

import sys

sys.path.append("..")
from toolkit.pre_load import neo_con
from toolkit.pre_load import wv_model, tree, predict_labels
from toolkit.NER import get_explain, get_detail_explain


# 接收GET请求数据
def showdetail(request):
    ctx = {}
    if 'title' in request.GET:
        # 连接数据库
        db = neo_con
        title = request.GET['title']
        answer = db.matchHudongItembyTitle(title)
        if answer == None:
            return render(request, "404.html", ctx)

        # 内容介绍
        ctx['detail'] = answer['detail']
        # 标题
        ctx['title'] = answer['title']
        # 目录
        text = '<table class="table table-striped table-advance table-hover"> <tbody>'
        keyList = answer['InfoKeyList'].split('##')[1:]
        i = 0
        print("--------------", len(keyList))
        if len(keyList) > 6:
            while i < len(keyList):
                value = " "
                text += "<tr>"
                try:
                    text += '<td><strong>' + str(i + 1) + '.' + keyList[i] + '</strong></td>'
                    i += 1
                    text += '<td><strong>' + str(i + 1) + '.' + keyList[i] + '</strong></td>'
                    i += 1
                    text += '<td><strong>' + str(i + 1) + '.' + keyList[i] + '</strong></td>'
                    i += 1
                except:
                    pass

                text += "</tr>"
        else:
            while i < len(keyList):
                value = " "
                text += "<tr>"
                text += '<td><strong>' + str(i + 1) + '.' + keyList[i] + '</strong></td>'
                text += '<td>' + value + '</td>'
                i += 1

                text += "</tr>"

        text += " </tbody> </table>"
        if answer['InfoKeyList'].strip() == '':
            text = ''
        ctx['InfoKeyTable'] = text
        ctx['InfoValueList'] = answer['InfoValueList']
        # 页面图片
        image = answer['image']
        ctx['image'] = '<img src="' + str(image) + '" alt="该条目无图片" height="100%" width="100%" >'
        # 属性名列表（值）
        ctx['baseInfoKeyList'] = []
        try:
            List = answer['baseInfoKeyList'].split('##')
            for p in List:
                ctx['baseInfoKeyList'].append(p)
            # 列表所对应的属性
            ctx['baseInfoValueList'] = []
            List = answer['baseInfoValueList'].split('##')
            for p in List:
                ctx['baseInfoValueList'].append(p)
        except:
            pass
        # 关系列表
        text = ""
        try:
            List = answer['openTypeList'].split('##')
            for p in List:
                text += '<span class="badge bg-important">' + str(p) + '</span> '
            ctx['openTypeList'] = text
        except:
            pass
        # 详情
        text = '<table class="table table-striped table-advance table-hover"> <tbody>'
        try:
            keyList = answer['InfoKeyList'].split('##')[1:]
            valueList = answer['InfoValueList'].split('##')[1:]
            i = 0
            while i < len(valueList):
                value = " "
                if i < len(valueList):
                    value = valueList[i]
                text += "<tr>"
                text += '<td><strong>' + keyList[i] + '</strong></td>'
                text += '<td>' + value + '</td>'
                i += 1
                text += "</tr>"
            text += " </tbody> </table>"
            if answer['InfoKeyList'].strip() == '':
                text = ''
            ctx['baseInfoview'] = text
        except:
            pass

        # 列表
        try:
            text = '<table class="table table-striped table-advance table-hover"> <tbody>'
            keyList = answer['baseInfoKeyList'].split('##')
            valueList = answer['baseInfoValueList'].split('##')
            i = 0
            while i < len(keyList):
                value = " "
                if i < len(valueList):
                    value = valueList[i]
                text += "<tr>"
                text += '<td><strong>' + keyList[i] + '</strong></td>'
                text += '<td>' + value + '</td>'
                i += 1

                if i < len(valueList):
                    value = valueList[i]
                if i < len(keyList):
                    text += '<td><strong>' + keyList[i] + '</strong></td>'
                    text += '<td>' + value + '</td>'
                else:
                    text += '<td><strong>' + '</strong></td>'
                    text += '<td>' + '</td>'
                i += 1
                text += "</tr>"
            text += " </tbody> </table>"
            if answer['baseInfoKeyList'].strip() == '':
                text = ''
            ctx['baseInfoTable'] = text
        except:
            pass

        tagcloud = ""
        taglist = wv_model.get_simi_top(answer['title'], 10)
        for tag in taglist:
            tagcloud += '<a href= "./detail.html?title=' + str(tag) + '"> '
            tagcloud += str(tag) + "</a>"
        #			print(tag)
        ctx['tagcloud'] = tagcloud

        # 农业类型
        agri_type = ""
        ansList = tree.get_path(answer['title'], True)
        for List in ansList:
            agri_type += '<p >'
            flag = 1
            for p in List:
                if flag == 1:
                    flag = 0
                else:
                    agri_type += ' / '
                agri_type += str(p)

            agri_type += '</p>'
        if len(ansList) == 0:
            agri_type = '<p > 暂无农业类型</p>'
        ctx['agri_type'] = agri_type

        # 实体类型
        entity_type = ""
        explain = get_explain(predict_labels[answer['title']])
        detail_explain = get_detail_explain(predict_labels[answer['title']])
        entity_type += '<p > [' + explain + "]: "
        entity_type += detail_explain + "</p>"
        ctx['entity_type'] = entity_type
    else:
        return render(request, "404.html", ctx)

    return render(request, "detail.html", ctx)

#	
## -*- coding: utf-8 -*-
# from django.http import HttpResponse
# from django.shortcuts import render_to_response
# import thulac
# 
# import sys
# sys.path.append("..")
# from neo4jModel.models import Neo4j
#
# def search_detail(request):
#	return render_to_response('detail.html')
#
## 接收GET请求数据
# def showdetail(request):
#	request.encoding = 'utf-8'
#	if 'title' in request.GET:
#		# 连接数据库
#		db = Neo4j()
#		db.connectDB()
#		title = request.GET['title']
#		answer = db.matchItembyTitle(title)
#		message = answer['detail']
#				
#	return HttpResponse(message)