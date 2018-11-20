from   hm7 import LogReader

#Test1
for i in LogReader():
    print(i)

#Test2
with LogReader() as l:
    for i in l:
        print(i)


#Test3

logrdr =LogReader()

for i in logrdr.files:
    print(i)

