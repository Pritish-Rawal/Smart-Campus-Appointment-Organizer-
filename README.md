# Smart-Campus-Director-lobby
#The project helps a person to organize his meeting in an easy and user friendly way. It helps him take decisions and allows him #freedom to choose the order in which he wants to meet based on his priority. 
name=[ ] #list for names
purpose=[ ] #list for the purpose
sort=[ ]		#list for order according to ID
tname='lol'	#temporary name
tpur='none'	#temporary purpose
i=0		#counter
temp=0	#temp variable

for i in range(5):	#for loop to accept the name and purpose 
    tname= input('Enter your name: ')
    name.append(tname)
    tpur=input('Give purpose:')
    purpose.append(tpur)
for i in range(5):	#for to print the names and purpose with their ID’s
               print('Unique number is ',(i+1))
               print('name is: ')
               print(name[i])
               print('purpose is:')
               print(purpose[i])
               print()
print('enter the way you want it to be sorted')
for i in range(5):	#user enters his preferred order
    print(i+1,':')
    temp=input()
    sort.append(temp)
# users order is printed
print('your order is :')
for i in range(5):
    print(sort[i], end=' ')

print()
for i in range(5):
    sort[i]=int(sort[i])-1
#printing the names in order
for i in range(5):
    temp=sort[i]
    temp=int(temp)
    print(name[temp])


# writing in html

import webbrowser
#opening index .php, it can be .html also
f = open('index.php','w')
#writing the html code
message = """<html>
<head></head>
<body>
<p>Order is:</p>
"""

f.write(message)
message="""<p>"""
f.write(message)
for i in range(5):	#for loop to write each name in html
    temp=sort[i]
    temp=int(temp)
    f.write(message)
    f.write(name[temp])
    f.write(message)
message = """
</body>
</html>"""	#closing html
f.write(message)
f.close()	#closing file
#opening  the file 
webbrowser.open_new_tab('index.html')
