import csv
from fuzzywuzzy import process
#function to simplify the querry
def simplify(a):
    st =""
    vow = ['A','E','I','O','U']
    for i in range(len(a)):
        if i==0:
            st=st+a[i]
        elif a[i] not in vow:
            st=st+a[i]
        else:
            pass
    if len(st)<3:
        return a
    else:
        return st

filename = "demo.csv"
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

d = dict(rows)
li=list(d.values())
li.sort()
search = input("enter your search")
search = search.split(" ")
search = [i.upper() for i in search if i!=""]
result =[]

for i in li:
    items=i.split(" ")
    items=[i for i in items if i!=""]
    rat=0
    k=0
    for count in range(len(search)):
        for word in items:
           if search[count]==word:
               k+=1
           if k ==len(search):
               if i in result:
                   pass
               else:
                    result.append(i)

leangth = len(search)
for  i in search:
    if len(search)==1:
        for name in li:
            s=name.split(" ")
            for part in s:
                if part==i:
                    result.append(name)
                elif simplify(part)==simplify(i):
                    result.append(name)
    elif len(search)==2:
        try:
            for name in li:
                s=name.split(" ")
                if s[0]==search[0] and s[1]==search[1]:
                    result.append(name)
                elif simplify(s[0])==simplify(search[0]) and simplify(s[1])==simplify(search[1]):
                    result.append(name)
        except:
            pass
    elif len(search) == 3:
        for name in li:
            s=name.split(" ")
            if s[0]==search[0]and s[1]==search[1] and s[2]==search[2]:
                result.append(name)
                continue
            elif simplify(s[0])==simplify(search[0])and simplify(s[1])==simplify(search[1]) and simplify(s[2])==simplify(search[2]):
                result.append(name)
print(len(result))
least=()
try:
    if len(result)<20:
        for t in search:
            least =process.extract(t,li)
except:
    pass
for i in range(len(least)):
    result.append(least[i])

print("search results are", result[:21])

