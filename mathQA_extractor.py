# This code is contributed by avishekarora
import json


# Python Program to convert prefix to Infix
def prefixToInfix(prefix):
    stack = []
    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")" or c == "**":
        return True
    else:
        return False

def reader(file_path):
    json_file = open(file_path)
    data = json.load(json_file)

    for entity in data:
        formula = entity["annotated_formula"]
        formula = formula.replace("(", ",")
        formula = formula.replace(", ", ",")
        formula = formula.replace(")", "")
        formula = formula.replace("const_", "")
        #print(formula)
        formula = formula.split(",")
        #print(formula)

        # string oeprator => symbol operator
        idx=-1
        for i in formula:
            idx+=1
            if i == "add":
                formula[idx]="+"
                
            elif i == "subtract":
                formula[idx]="-"
                
            elif i == "multiply":
                formula[idx]="*"
                
            elif i =="divide":
                formula[idx]="/"
                
            elif i =="power":
                formula[idx]="**"
            else:#숫자
                pass
            
        print(formula)
        equation = prefixToInfix(formula)
        
        #write the equation to json file
        with oepn("mathQQ_equation.json", 'w') as file:
            file.write(equation)
        
 
# Driver code
if __name__=="__main__":

    file_path = "./mathQA.json"
    formula = reader(file_path)

     
