# This solution code isn't optimized that much
# but in this case a stack is implemented manually
# it's a dynamic kind of stack but there's a problem
# it works fine but in hackerrank test case after 17 
# it's taking more time then the demanding one in 
# hackerrank
n= int(input())                     #total number of inputs
lis = []
for i in range(n):
    a=list(map(int,input().split()))
    lis.append(a)
        
class stack(object):
    def __init__(self,limit):
        self.item=[]
        self.limit=limit             #Implementation of stack
                                     #
    def push(self,item):
        self.item.append(item)
    def pop(self):
        self.item.pop()
    def max_ele(self):
        for ele in self.item:
            print(max(self.item))
            return max(self.item)
        
ss = stack(n*100)
for i in lis:
    if i[0] == 1:
        ss.push(i[1])               #getting those commands as the three case
                                    #mentioned-  1) Push 2) Delete/pop 3) getting max element
    if i[0] == 2:                   
        ss.pop()
    if i[0] == 3:
        ss.max_ele()