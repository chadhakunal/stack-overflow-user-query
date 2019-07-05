import requests
from lxml.html import fromstring
from stackapi import StackAPI
import datetime
import csv
import pickle

SITE = StackAPI('stackoverflow')

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//*[@id="proxylisttable"]/tbody/tr')[5:100]:
        if i.xpath('.//td[1]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def getQuestions(tags,proxy):
    proxy_dict = {  
      "http": proxy,
    }
    questions = SITE.fetch('questions', fromdate=datetime.datetime(2005,1,1).date(), todate=datetime.date.today()
                           , tagged=tags, sort='votes',filter='withbody',pagesize=50,page=1,proxy=proxy_dict)
    return questions


# Preprocessing of Questions: Replace special characters with symbol
def text_prepare_questions(text):
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        text = text.replace(code[1], code[0])
    return text


def main():
    
    proxies = ["165.22.178.128:8118","68.183.135.4:8080","68.183.99.96:3128"]#list(get_proxies())
    print("All Proxies: ",proxies)
    proxy_cnt = 0
    allTags = pickle.load( open( "tags_to_extract_seperate.txt", "rb" ) )

    
    with open('X_Train.csv', 'a',newline='',encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        
        for cnt,i in enumerate(allTags):
            current_proxy = "http://" + str(proxies[int(proxy_cnt/30)])
            
            print("\n",cnt,") Tag: ",str(i),"  Proxy: ",current_proxy,"\n")
            
            questions = getQuestions([str(i)],current_proxy)
            
            for i in questions["items"]:
                row = [text_prepare_questions(i["title"]),i["tags"]]
                writer.writerow(row)
            proxy_cnt = (proxy_cnt+1)%(30*50)
        
        csvFile.close()

if __name__ == "__main__":
    main()


