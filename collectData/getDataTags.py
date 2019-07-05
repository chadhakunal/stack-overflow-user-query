import requests
from lxml.html import fromstring
import pandas as pd
from stackapi import StackAPI
import datetime
import csv
import pickle

SITE = StackAPI('stackoverflow')

def getQuestions(tags):
    questions = SITE.fetch('questions', fromdate=datetime.datetime(2005,1,1).date(), todate=datetime.date.today()
                           , tagged=tags, sort='votes',filter='withbody',pagesize=80,page=1)
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
    tags = pd.read_pickle("tags1.pickle")
    with open('data_tags_1.csv', 'a',newline='',encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        
        for cnt,i in enumerate(tags[1000:]):
            questions = getQuestions([str(i)])
            if cnt%20==0:
                print("Iteration: ",cnt)
            for i in questions["items"]:
                row = [text_prepare_questions(i["title"]),i["tags"]]
                writer.writerow(row)
        csvFile.close()

if __name__ == "__main__":
    main()
