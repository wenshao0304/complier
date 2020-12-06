import re
import sys
s=sys.argv[1]

str1=''
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
    str1=''
if str1=='':
    print("success")
else:
    
    print("fail {}".format(str1))
