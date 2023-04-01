class Stack:

    def init(list):
        list = [] 
          
    def push(list,a):
        list.append(a)

    def pop(list):
        list.pop()

    def empty(list):
        list.clear()

    def isEmpty(list):
        if len(list) == 0:
            return True
        else:
            return False 


def Match(open,close):               
    if open == '{' and close == '}':
        return True
    elif open == '[' and close == ']':
        return True
    elif open == '(' and close == ')':
        return True
    else:
        return False 


myStack = list() 
s = Stack

s.init(myStack) 
print("Stack after init() is:", myStack)


s.push(myStack,1)
s.push(myStack,2)
s.push(myStack,3) 
print("Stack after push() contains:", myStack) 


s.pop(myStack)
print("Stack after pop() contains:", myStack)

s.empty(myStack)
print("Stack after empty() is:", myStack) 


myStack1 = list()
s1 = Stack 
s1.init(myStack1) 
exp ='{([()])}' 
isBalanced = True
i = 0 
print("Testing if expression: ", exp , "is balanced.")
while i < len(exp) and isBalanced == True:               
    str1 = exp[i]                       #current element of expression gets saved in str1
    if str1 in "{[(":
        s1.push(myStack1, str1)         #pushing opening elements('{' , '[' , '(' )  on top of the stack
    elif str1 in "}])":
        if s1.isEmpty(myStack1) == True:    #if we get a closing element('}' , ']' , ')' ) and our stack is empty then there is an imbalance of opening and closing elements 
            isBalanced == False 
            print("More right than left parentheses/elements. Expression is unbalanced.")
        else:
            str2 = s1.pop(myStack1)         #if we get a closing element and our stack is not empty, then we pop the stack and check whether the two elements are of the same type
            isMatched = Match(str1,str2)  
            if isMatched == False:
                isBalanced == False  
    i+=1 

if s1.isEmpty(myStack1) == True and isBalanced == True:
    print("Expression is perfectly balanced.")
else:
    print("Expression is unbalanced.")          
        









 