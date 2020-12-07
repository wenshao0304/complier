import re
import sys
s=sys.argv[1]

str1=''
def coma(s,b):
    num=0
    if (57>=ord(s)>=48) and (57>=ord(b)>=48) and (ord(s)==ord(b)):
        
            num=1
    return num
def comn(s,b):
    num=0
    if (90>=ord(s)>=65) and (90>=ord(b)>=65) and (ord(s)==ord(b)):  
       
             num=1
    elif (122>=ord(s)>=97) and (122>=ord(b)>=97) and (ord(s)==ord(b)):  
       
             num=1	
    return num
if re.search('[A-Za-z]',s)==None:
    str1+='至少輸入一個英文 '
if re.search('[0-9]',s)==None:
    str1+='至少輸入一個數字 '
if re.search('[\W]',s)==None:
    str1+='至少輸入一個符號 '
if len(s)<8:
    str1+='長度小於8 '
if len(s)>16:
    str1+='長度大於16 '
if re.search('[A-Z]',s)==None:
    str1+='至少輸入一個大寫字母 '
else:
    str1==''  
for i in range(len(s)-1):
        if coma(s[i],s[i+1])==1:
            str1+='數字不可連續 '
            break;
for i in range(len(s)-1):
        if comn(s[i],s[i+1])==1:
            str1+='字母不可連續 '
            break;
if str1=='':
    print("success")
else:
    
    print("fail {}".format(str1))
