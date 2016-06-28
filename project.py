name=[]
purpose=[]
sort=[]
tname='lol'
tpur='none'
i=0
temp=0

for i in range(5):
    tname= input('Enter your name: ')
    name.append(tname)
    tpur=input('Give purpose:')
    purpose.append(tpur)
for i in range(5):
               print('Unique number is ',(i+1))
               print('name is: ')
               print(name[i])
               print('purpose is:')
               print(purpose[i])
               print()
print('enter the way you want it to be sorted')
for i in range(5):
    print(i+1,':')
    temp=input()
    sort.append(temp)
    
    
            #show remaining
    #if mistake show that too while sorting
            #accept from site
        

print('your order is :')
for i in range(5):
    print(sort[i], end=' ')

print()
for i in range(5):
    sort[i]=int(sort[i])-1

for i in range(5):
    temp=sort[i]
    temp=int(temp)
    print(name[temp])


# write-html-2.py

import webbrowser

f = open('index.php','w')

message = """<html>
<head></head>
<body>
<p>Order is:</p>
"""

f.write(message)
message="""<p>"""
f.write(message)
for i in range(5):
    temp=sort[i]
    temp=int(temp)
    f.write(message)
    f.write(name[temp])
    f.write(message)
message = """
</body>
</html>"""
f.write(message)
f.close()

webbrowser.open_new_tab('index.html')
    

