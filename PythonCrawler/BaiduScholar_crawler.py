#下载百度学术的论文
# 导入所需模块
import requests
import re
import os
from urllib.request import urlretrieve

# 获取URL信息
def get_url(key):
    url = 'https://xueshu.baidu.com/s?wd=' + key + '&rsv_bp=0&tn=SE_baiduxueshu_c1gjeupa&rsv_spt=3&ie=utf-8&f=8&rsv_sug2=0&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D'
    return url

# 设置请求头
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Referer': 'https://googleads.g.doubleclick.net/'
}

# 获取相关论文的DOI列表
def get_paper_link(headers, key):
    response = requests.get(url=get_url(key), headers=headers)
    res1_data = response.text
    #找论文链接
    paper_link = re.findall(r'<h3 class=\"t c_font\">\n +\n +<a href=\"(.*?)\"',
                            res1_data)

    doi_list = []  #用一个列表接收论文的DOI
    for link in paper_link:
        paper_link = link
        response2 = requests.get(url=paper_link, headers=headers)
        res2_data = response2.text
        #提取论文的DOI
        try:
            paper_doi = re.findall(r'\'doi\'}\">\n +(.*?)\n ', res2_data)
            if str(10) in paper_doi[0]:
                doi_list.append(paper_doi)

        except:
            pass
    return doi_list
#get_paper_link(headers,'packet classification')

#构建sci-hub下载链接
def doi_download(headers, key):
    doi_list = get_paper_link(headers, key)
    print(doi_list)
    for doi in doi_list:
        doi_link = 'https://sci-hub.tf/' + doi[0]
        print(doi_link)

        if 'https:' not in doi_link:
            doi_link = 'https:' + doi_link

        res = requests.get(url=doi_link, headers=headers)
        try:
            down_link = re.findall(r'<iframe.*?src="(.*?)" id=.*?<\/iframe>',
                               res.text)[0]
            print(down_link)
            r = requests.get(url=down_link, headers=headers)
            path = r'F:\Work and Learn\Projects\PycharmProjects\PythonCrawler\Lab1Mission2'
            path = path +'\\' +  doi_link.split('/')[-1] + '.pdf'
            with open(path, 'wb') as f:
                f.write(r.content)
                print('下载完毕: ' + doi_link.split('/')[-1])

        except:
            print('该文章为空')
            pass

# 检索及下载
key = input("请输入您想要下载论文的关键词（英文）：")
doi_download(headers, key)