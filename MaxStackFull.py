# This one solution runs for every test case in hacker rank
# but in this solution because python didn't demands for any
# stack implementation because just by performing a single or more
# operation its inbuilt List Datastructure is enough and works like 
# array,stack and even in some cases with other functionalities works
# like deque.
N = int(input())          #Taking total number of input
stack = []                #list named as stack
for i in range(N):        #for loop for tracking total number of command input 
    line = input()        #line=next command and the element input
    comm = line[0]       #command=first element at index 0 of line command
    if comm == '1':      #If it's the command for Push according to question
        val = int(line[2:])  #then it's just going to index 2 after the space and assigning it to val
        if len(stack) == 0:  #just checking the length of stack that it's currently have any element or not
            stack.append(val)  #if it's null then appending the value
        else:                   #else just setting the current max to the last element of stack 
            currMax = stack[-1]  #it's basically for the third command od getting maximum element out of the stack
            stack.append(val if val > currMax else currMax) #if the value that has to append in else case is greater then current max then appending it or in else case appending the current max
    elif comm == '2':    #for the second command of deleting the element
        stack.pop()
    else:                 #third command refrenced here
        print(stack[-1])