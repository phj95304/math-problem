import json


def dumper(question):
    global idx
    global data

    data.append({str(idx) : {"question":question}})

    with open("./test.json", "w") as testfile:
        json.dump(data, testfile)
    
    

def fileReader():
    global idx
    with open('./type8.json') as json_file:
        for line in json_file:
            data = json.loads(line)
            question = data["question"]

            dumper(question)
            idx+=1


if __name__ == "__main__":
    idx =1
    data = []
    fileReader()