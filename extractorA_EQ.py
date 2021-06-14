import json
import re

##  **** type8에 answer option에서 A)A) B)B) C)C) D)D) E)E) 같이 옵션이 중복 되는 경우 있음

def dumper(answer, equation, rationale):
    global idx
    global data
    global data_rationale
    print("called------")
    print(answer)
    print(equation)

    data.append({str(idx) : {"answer":answer, "equation":equation}})

    with open("./answersheet.json", "w", encoding="utf-8") as answer_file:
        json.dump(data, answer_file, indent=4)

    data_rationale.append({str(idx) : {"equation":rationale}})
    with open("./rationale.json", "w", encoding="utf-8") as equation_file:
        json.dump(data_rationale, equation_file, indent=2)

    


def jsonMaker():
    global idx

    with open('./type8.json') as json_file:
        
        for line in json_file:
            data = json.loads(line)

            ## answer
            answer_cha = data["correct"]
            answeer_opt = data["options"]
            
            # print(answer_cha)
            # print(answeer_opt)
            if answer_cha == "A":
                answer=answeer_opt[0]
                answer = answer[2:]
            elif answer_cha == "B":
                answer=answeer_opt[1]
                answer = answer[2:]
            elif answer_cha == "C":
                answer=answeer_opt[2]
                answer = answer[2:]
            elif answer_cha == "D":
                answer=answeer_opt[3]
                answer = answer[2:]
            else:
                answer=answeer_opt[4]
                answer = answer[2:]
            
            print(answer)

            #rationale
            equation_ = data["rationale"]

            dumper(answer, "12+6", equation_)
            idx+=1




if __name__ == "__main__":
    idx = 1
    data = []
    data_rationale = []
    jsonMaker()