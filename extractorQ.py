import json
import re

import googletrans
from googletrans import Translator


def extractor(json_file_path, flag, math_file_path):
    pattern = re.compile(flag)
    math_file = open(math_file_path, 'w')
    with open(json_file_path) as json_file:
        for line in json_file:
            data = json.loads(line)
            
            #print(data["question"])
            question = data["question"]
            #does the question have a flag phrase?
            sent=pattern.search(question)
            if sent != None:
                math_file.write(line)

            #print(data["rationale"])

    math_file.close()     
    json_file.close()


def dumper(question):
    global idx
    global data
    print(question)
    data.append({str(idx) : {"question":question}})

    with open("./type8_KOR.json", "w", encoding="utf-8") as testfile:
        json.dump(data, testfile)

       

def jsonMaker():
    global idx

    with open('./type8.json') as json_file:
        
        for line in json_file:
            data = json.loads(line)
            question = data["question"]

            translator = Translator()
            trans = translator.translate(question, src='en', dest='ko')
            
            dumper(trans.text)
            idx+=1

            
if __name__ == "__main__":
    json_file_path = "./train.json"
    flag = "(([0-9]+)th)"
    math_file_path = "./type8.json"

    idx = 1
    data = []
    extractor(json_file_path, flag, math_file_path)
    jsonMaker()