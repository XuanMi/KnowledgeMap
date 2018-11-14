# -*- coding: utf-8 -*-
import scrapy
from newSpider.items import NewspiderItem
import urllib
import re
import json
split_sign = '##'
class HudongSpider(scrapy.Spider):
    name = 'hudong'
    allowed_domains = ['http://www.baike.com']
    # count = 0
    crops_file_object = open('crops.txt', 'r', encoding='utf-8').read()
    disease_file_object = open('disease.txt', 'r', encoding='utf-8').read()
    crops_wordList = crops_file_object.split()  # 获取词表
    disease_wordList = disease_file_object.split()

    wordList = crops_wordList + disease_wordList
    start_urls = []
    # pp = 0
    for i in wordList:  ##生成url列表
        cur = "http://www.baike.com/wiki/"
        cur = cur + str(i)
        start_urls.append(cur)
        # pp += 1
        # print(cur)
        # if pp > 100:
        #     break
    def parse(self, response):
        #filename = "encyclopedia.html"
        #open(filename, 'wb').write(response.body)
        # div限定范围
        main_div = response.xpath('//div[@class="w-990"]')
# ——————————————————————————————————————————新————————————————————————————————————————————
        title = response.url.split('/')[-1]  # ---------通过截取url获取title-------------
        # urllib.request 请求模块
        # urllib.error 异常处理模块
        # urllib.parse url解析模块
        # urllib.robotparser robots.txt解析模块
        title = urllib.parse.unquote(title)
        # find到了返回下标，没找到返回-1
        if title.find('isFrom=intoDoc') != -1:
            title = 'error'

        url = response.url  # ---------------------url直接得到-------------------
        url = urllib.parse.unquote(url)

        # nodename	选取此节点的所有子节点。
        # /	从根节点选取。
        # //	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
        # .	选取当前节点。
        # ..	选取当前节点的父节点。
        # @	选取属性。
        img = ""  # -----------------------爬取图片url-----------------------------
        for p in main_div.xpath('.//div[@class="r w-300"]/div[@class="doc-img"]/a/img/@src'):
            img = p.extract().strip()

        openTypeList = ""  # -----------------爬取开放域标签-------------------
        flag = 0  # flag用于分隔符处理（第一个词前面不插入分隔符）
        for p in main_div.xpath('.//div[@class="l w-640"]/div[@class="place"]/p[@id="openCatp"]/a/@title'):
            if flag == 1:
                openTypeList += split_sign
                openTypeList += " "
            openTypeList += p.extract().strip()
            flag = 1

        detail = ""  # ---------详细信息---------------
        detail_xpath = main_div.xpath('.//div[@class="l w-640"]/div[@class="information"]/div[@class="summary"]/p')
        if len(detail_xpath) > 0:
            detailb = detail_xpath.xpath('string(.)').extract()[0].strip()
            detailc = re.sub("\t|\n|\r", "", detailb)
            detail += detailc.replace('"', '')
        if detail == "":  # 可能没有
            detail_xpath = main_div.xpath('.//div[@class="l w-640"]/div[@id="content"]')
            if len(detail_xpath) > 0:
                detaila = detail_xpath.xpath('string(.)').extract()[0].strip()
                detaild = re.sub("\t|\n|\r", "", detaila)
                detail += detaild.replace('"', '')

        flag = 0
        baseInfoKeyList = ""  # 基本信息的key值
        for p in main_div.xpath(
                './/div[@class="l w-640"]/div[@name="datamodule"]/div[@class="module zoom"]/table//strong/text()'):
            if flag == 1:
                baseInfoKeyList += split_sign
                baseInfoKeyList += " "
            baseInfoKeyList += p.extract().strip()
            flag = 1

        ## 继续调xpath！！！！！！！！！！！！！
        flag = 0
        baseInfoValueList = ""  # 基本信息的value值
        base_xpath = main_div.xpath('.//div[@class="l w-640"]/div[@name="datamodule"]/div[@class="module zoom"]/table')
        for p in base_xpath.xpath('.//span'):
            if flag == 1:
                baseInfoValueList += split_sign
                baseInfoValueList += " "
            all_text = p.xpath('string(.)').extract()[0].strip()
            baseInfoValueList += all_text
            flag = 1
# ————————————————————————————————————++————结束————————————————————————————————————————
# ---------通过截取url获取name-------------
#         name = response.url.split('/')[-1]
#         # urllib.request 请求模块
#         # urllib.error 异常处理模块
#         # urllib.parse url解析模块
#         # urllib.robotparser robots.txt解析模块
#         name = urllib.parse.unquote(name)
#         if name.find('isFrom=intoDoc') != -1:
#             name = 'error'
# -----------获取补全信息键---------------
        count = 0
        InfoKeyList = ""
        for p in main_div.xpath('.//div[@class="l w-640"]/fieldset[@id="catalog"]/div[@id="full-all"]/ul/li/a/@title'):
            if count >= 0:
                InfoKeyList += split_sign
                InfoKeyList += p.extract().strip()
            count += 1
# -----------获取补全信息值---------------
        counta = 0
        InfoValueList = ""
        info_xpath = main_div.xpath('.//div[@id="content"]')
        for p in info_xpath.xpath('.//p'):
            if counta >= 0:
                InfoValueList += split_sign
                InfoValueList += " "
            if (re.sub('\t|\n|\r',"",p.xpath('string(.)').extract()[0].strip())) != "":
                infoa = p.xpath('string(.)').extract()[0].strip()
                infob = re.sub('\t|\n|\r',"",infoa)
                InfoValueList += infob.replace('"','')
                counta += 1
            if counta == len(info_xpath.xpath('.//p')) and counta < count:
                for i in range(count-len(info_xpath.xpath('.//p'))):
                    InfoValueList += "##"
                    InfoValueList += " "
            if count == counta:
                break

        item = NewspiderItem()
        item['title'] = title.replace(u'\xa0', u' ')
        item['url'] = url.replace(u'\xa0', u' ')
        item['image'] = img.replace(u'\xa0', u' ')
        item['openTypeList'] = openTypeList.replace(u'\xa0', u' ')
        item['detail'] = detail.replace(u'\xa0', u' ')
        item['baseInfoKeyList'] = baseInfoKeyList.replace(u'\xa0', u' ')
        item['baseInfoValueList'] = baseInfoValueList.replace(u'\xa0', u' ')
        item['baseInfoKeyList'] = baseInfoKeyList.replace(u'\xa0', u' ')
        item['baseInfoValueList'] = baseInfoValueList.replace(u'\xa0', u' ')
        item['InfoKeyList'] = InfoKeyList.replace(u'\xa0', u' ')
        item['InfoValueList'] = InfoValueList.replace(u'\xa0', u' ')

        # file = open('newSpider/data/hudong_pedia.json', 'wb')
        # line = ""
        # line += json.dumps(dict(item), ensure_ascii=False) + '\n'
        # file.write(line)
        yield item