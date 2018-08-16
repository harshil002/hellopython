
# coding: utf-8

# In[1]:d

import bs4 as bs
import urllib.request

F = urllib.request.urlopen('https://www.nonviolenceinternational-ny.org/blogs').read()
A = bs.BeautifulSoup(F,'lxml')
print(A.text)


# In[2]:

import bs4 as bs
import requests
import urllib.request
import re

F = urllib.request.urlopen('https://www.nonviolenceinternational-ny.org/blogs').read()
soup = bs.BeautifulSoup(F.decode('ascii', 'ignore'),'lxml') # parse the html 
for i in soup.find_all('p'):
    print(i.text)


# In[7]:

import bs4 as bs
import requests
import urllib.request
import re

F = urllib.request.urlopen('https://www.nonviolenceinternational-ny.org/single-post/2018/06/04/How-a-Violent-Conflict-Came-to-Be').read()
soup = bs.BeautifulSoup(F.decode('ascii', 'ignore'),'lxml') # parse the html 
for i in soup.find_all('p'):
    print(i.text)


# In[5]:

import bs4 as bs
import requests
import urllib.request
import re

F = urllib.request.urlopen('https://www.nonviolenceinternational-ny.org/single-post/2018/06/04/How-a-Violent-Conflict-Came-to-Be').read()
soup = bs.BeautifulSoup(F.decode('ascii', 'ignore'),'lxml') # parse the html 
for i in soup.find_all('p', class_="font_8"):
    print(i.text)


# In[7]:

import bs4 as bs
import requests
import urllib.request
import re

F = urllib.request.urlopen('https://www.nonviolenceinternational-ny.org/single-post/2018/06/01/NYC-Youth-Over-Guns-March').read()
soup = bs.BeautifulSoup(F.decode('ascii', 'ignore'),'lxml') # parse the html 
for i in soup.find_all('p', class_="font_8"):
    print(i.text)


# In[2]:

import bs4 as bs
import requests

list_links = []
A = requests.get("https://www.nonviolenceinternational-ny.org/blogs")
A.text
soup = bs.BeautifulSoup(A.text, 'lxml')
for link in soup.find_all('a', href=True):
    #print(link['href'])
    list_links.append(link['href'])

print(list_links)


# In[5]:

import bs4 as bs
import requests

A = requests.get("https://www.nonviolenceinternational-ny.org/single-post/2018/06/04/How-a-Violent-Conflict-Came-to-Be")
A.text
soup = bs.BeautifulSoup(A.text, 'lxml')
nav = soup.nav
body = soup.body
for para in body.find_all('div', class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
    print(para.text)
   


# In[4]:

import bs4 as bs
import requests

#for  i in range(0,len(list_links)):
 #   Content = requests.get(list_links[i])
  #  Content.text
   # soup = bs.BeautifulSoup(Content.text, 'lxml')
    #nav = soup.nav
    #body = soup.body
    #for para in body.find_all('div'):
     #   print(para.get_text())

    
import bs4 as bs
import requests
import urllib.request
import re
for  i in range(0,len(list_links)):
    Content = urllib.request.urlopen(list_links[i]).read()
    soup = bs.BeautifulSoup(Content.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all('p'):
        print(j.text)


# In[17]:

import bs4 as bs
import requests

list_links = []
A = requests.get("https://www.nonviolenceinternational-ny.org/blogs")
A.text
soup = bs.BeautifulSoup(A.text, 'lxml')
for link in soup.find_all(href=True):
    #print(link['href'])
    temp =  link['href']
    print(temp)
    list_links.append(temp)

print(list_links)
#results = []
#for a in reviews(href=True):
 #   temp = "http://www.porcys.com" + a['href']
  #  print(temp)
   # results.append(temp)

#print results


# In[23]:

import bs4 as bs
import requests
import urllib.request
import re
Z1 = ["https://www.nonviolenceinternational-ny.org/single-post/2018/06/04/How-a-Violent-Conflict-Came-to-Be","https://www.nonviolenceinternational-ny.org/single-post/2018/06/01/NYC-Youth-Over-Guns-March","https://www.nonviolenceinternational-ny.org/single-post/2018/04/26/How-do-we-Reform-Sustaining-Peace","https://www.nonviolenceinternational-ny.org/single-post/2018/05/03/Zambia%E2%80%99s-Hidden-Gems","https://www.nonviolenceinternational-ny.org/single-post/Trumping-the-Norm","https://www.nonviolenceinternational-ny.org/single-post/2018/04/19/Funding-for-Teachers-vs-Funding-for-Guns","https://www.nonviolenceinternational-ny.org/single-post/2018/03/30/A-Landmine-Model-for-Peace","https://www.nonviolenceinternational-ny.org/single-post/2018/04/05/Organ-Trafficking-Education-and-War-Women-and-Their-Plight-for-Sustainable-Lives","https://www.nonviolenceinternational-ny.org/single-post/2018/03/15/Trumps-Empty-Offices","https://www.nonviolenceinternational-ny.org/single-post/2018/03/18/The-2018-Preparatory-Committee"]
for a in range(0,len(Z1)): 
    A = urllib.request.urlopen(Z1[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for i in soup.find_all('p'):
        copy1=i.text
        print(copy1)


# In[21]:

import bs4 as bs
import requests
import urllib.request
import re
Z2 = ["https://www.nonviolenceinternational-ny.org/single-post/2018/03/08/Teenage-boy-shot-and-killed-after-a-car-accident-with-Conceal-and-Carry-holder","https://www.nonviolenceinternational-ny.org/single-post/2018/03/01/Uneven-Progress-The-Aging-of-the-Beijing-Declaration","https://www.nonviolenceinternational-ny.org/single-post/2018/02/15/Toxic-Trump","https://www.nonviolenceinternational-ny.org/single-post/2018/02/22/Disarming-West-Africa","https://www.nonviolenceinternational-ny.org/single-post/2018/01/25/New-Conservatism-Lincoln-and-Trump","https://www.nonviolenceinternational-ny.org/single-post/2018/02/13/North-Korea-and-Denuclearization","https://www.nonviolenceinternational-ny.org/single-post/2017/12/28/How-SDG-164-is-Making-You-Safer","https://www.nonviolenceinternational-ny.org/single-post/2018/01/05/NRA-vs-NRA","https://www.nonviolenceinternational-ny.org/single-post/2017/12/01/They-Are-the-LAWS-Killer-Robots-and-Trump","https://www.nonviolenceinternational-ny.org/single-post/2017/12/21/Why-is-the-West-Turning-a-Blind-Eye-Towards-Yemen"]
for a in range(0,len(Z2)): 
    B = urllib.request.urlopen(Z2[a]).read()
    soup = bs.BeautifulSoup(B.decode('ascii', 'ignore'),'lxml') # parse the html 
    for i in soup.find_all('p'):
        copy2=i.text
        print(copy2)


# In[22]:

import bs4 as bs
import requests
import urllib.request
import re
Z3 = ["https://www.nonviolenceinternational-ny.org/single-post/2017/11/16/The-Kashmir-Issue","https://www.nonviolenceinternational-ny.org/single-post/2017/11/15/The-Heinous-Humanitarian-Cost-of-Modern-Warfare","https://www.nonviolenceinternational-ny.org/single-post/2017/11/03/Examining-Synergies-Between-the-UN-POA-ATT-and-SDGs","https://www.nonviolenceinternational-ny.org/single-post/2017/11/09/PEACE-BOAT-GLOBAL-VOYAGES-FOR-PEACE","https://www.nonviolenceinternational-ny.org/single-post/2017/10/26/Sustainability-vs-Displacement","https://www.nonviolenceinternational-ny.org/single-post/2017/11/01/Re-Examining-the-PoA","https://www.nonviolenceinternational-ny.org/single-post/2017/10/25/Scrapping-the-Surplus-IANSA-Side-Event","https://www.nonviolenceinternational-ny.org/single-post/2017/10/25/The-Second-Amendment-Conservatives-and-Irony","https://www.nonviolenceinternational-ny.org/single-post/2017/10/16/A-President-Meets-With-Civil-Society","https://www.nonviolenceinternational-ny.org/single-post/2017/10/18/The-15th-Anniversary-of-the-Hague-Code-of-Conduct"]
for a in range(0,len(Z3)): 
    C = urllib.request.urlopen(Z3[a]).read()
    soup = bs.BeautifulSoup(C.decode('ascii', 'ignore'),'lxml') # parse the html 
    for i in soup.find_all('p'):
        copy3=i.text
        print(copy3)


# In[24]:

import bs4 as bs
import requests
import urllib.request
import re
Z4 = ["https://www.nonviolenceinternational-ny.org/single-post/2017/10/11/Rose-Welsch-Speaks-at-the-First-Committee","https://www.nonviolenceinternational-ny.org/single-post/2017/10/11/Spirituality-Psychology-and-the-Eight-Pillars-of-Peace","https://www.nonviolenceinternational-ny.org/single-post/2017/10/10/How-Guns-Shift-Conflict-Towards-Violence-Part-5","https://www.nonviolenceinternational-ny.org/single-post/2017/10/09/How-Guns-Shift-Conflict-Towards-Violence-Part-4","https://www.nonviolenceinternational-ny.org/single-post/2017/10/07/How-Guns-Shift-Conflict-Towards-Violence-Part-2","https://www.nonviolenceinternational-ny.org/single-post/2017/10/08/How-Guns-Shift-Conflict-Towards-Violence-Part-3","https://www.nonviolenceinternational-ny.org/single-post/2017/10/06/How-Guns-Shift-Conflict-Towards-Violence-Part-1","https://www.nonviolenceinternational-ny.org/single-post/Path-of-NonviolenceNY","https://www.nonviolenceinternational-ny.org/single-post/2017/09/28/A-Framework-For-Peace","https://www.nonviolenceinternational-ny.org/single-post/2017/09/21/The-Evolution-of-Violent-Conflict"]
for a in range(0,len(Z4)): 
    D = urllib.request.urlopen(Z4[a]).read()
    soup = bs.BeautifulSoup(D.decode('ascii', 'ignore'),'lxml') # parse the html 
    for i in soup.find_all('p'):
        copy4=i.text
        print(copy4)


# In[25]:

import bs4 as bs
import requests
import urllib.request
import re
Z5 = ["https://www.nonviolenceinternational-ny.org/single-post/2017/09/14/International-Day-of-Peace","https://www.nonviolenceinternational-ny.org/single-post/2017/08/11/An-HLPF-To-Remember","https://www.nonviolenceinternational-ny.org/single-post/2017/08/02/My-HLPF-2017-Reflections-and-Recognitions","https://www.nonviolenceinternational-ny.org/single-post/2017/07/28/Peaceful-Just-and-Inclusive-Societies-and-the-SDGs","https://www.nonviolenceinternational-ny.org/single-post/2017/07/26/An-Intern%25E2%2580%2599s-Perspective-on-the-HLPF","https://www.nonviolenceinternational-ny.org/single-post/2017/07/21/Women-Reproductive-Health-and-Sustainable-Development","https://www.nonviolenceinternational-ny.org/single-post/2017/07/17/Reproductive-Rights-and-the-2030-Agenda","https://www.nonviolenceinternational-ny.org/single-post/2017/07/14/Spreading-the-International-Day-of-Peace-A-Grassroots-Effort","https://www.nonviolenceinternational-ny.org/single-post/URGENT-ACTION-NEEDED","https://www.nonviolenceinternational-ny.org/single-post/2017/07/14/50-Years-of-Israeli-Occupation-Moving-Forward"]
for a in range(0,len(Z5)): 
    E = urllib.request.urlopen(Z5[a]).read()
    soup = bs.BeautifulSoup(E.decode('ascii', 'ignore'),'lxml') # parse the html 
    for i in soup.find_all('p'):
        copy5=i.text
        print(copy5)


# In[26]:

import bs4 as bs
import requests
import urllib.request
import re
Z6 = ["https://www.nonviolenceinternational-ny.org/single-post/2017/07/08/International-Gun-Destruction-Day-Scrap-the-Surplus","https://www.nonviolenceinternational-ny.org/single-post/2017/07/07/The-Importance-of-the-Intergenerational-Dialogues-on-Sustainable-Development-Goals","https://www.nonviolenceinternational-ny.org/single-post/2017/07/01/BeyondTheWageGapCEDAWandGenderEquality","https://www.nonviolenceinternational-ny.org/single-post/2017/07/07/The-Straw-Thing-Technology-Education-for-Sustainable-Oceans","https://www.nonviolenceinternational-ny.org/single-post/2017/06/26/PremonitionOfDangerMartialLawInThePhilippines","https://www.nonviolenceinternational-ny.org/single-post/2017/06/24/SmallIslandsBigChallengesRoadblocksInThePathToASustainableFuture","https://www.nonviolenceinternational-ny.org/single-post/WhyWeNeedALeaderLikeDag-HammarskjoldNowMoreThanEver","https://www.nonviolenceinternational-ny.org/single-post/FiveAwakeLightsAFire","https://www.nonviolenceinternational-ny.org/single-post/2017/04/21/Nadia-Murad-The-Fight-for-Justice","https://www.nonviolenceinternational-ny.org/single-post/InDisarmementNegotiationsWomenMatter"]
for a in range(0,len(Z6)): 
    F = urllib.request.urlopen(Z6[a]).read()
    soup = bs.BeautifulSoup(F.decode('ascii', 'ignore'),'lxml') # parse the html 
    for i in soup.find_all('p'):
        copy6=i.text
        print(copy6)


# In[27]:

import bs4 as bs
import requests
import urllib.request
import re
Z7 = ["https://www.nonviolenceinternational-ny.org/single-post/2017/04/14/Finding-Brightness-in-Darkness-The-Story-of-One-Syrian-Refugee","https://www.nonviolenceinternational-ny.org/single-post/2017/04/07/A-Step-in-Our-Mission-Towards-Peace","https://www.nonviolenceinternational-ny.org/single-post/2017/03/31/The-Solace-of-Music-Amid-Chaos","https://www.nonviolenceinternational-ny.org/single-post/CSWTheInternsPerspective","https://www.nonviolenceinternational-ny.org/single-post/InternationalWomesDay","https://www.nonviolenceinternational-ny.org/single-post/2017/03/03/The-Pandemic-of-Indifference","https://www.nonviolenceinternational-ny.org/single-post/2017/02/24/How-Does-Gender-Inequality-Affect-Sustainable-Peace-and-Development","https://www.nonviolenceinternational-ny.org/single-post/2017/02/16/The-55th-Commission-for-Social-Developments-Opening-Address-Presented-by-Daniel-Perell","https://www.nonviolenceinternational-ny.org/single-post/2017/02/10/The-ECOSOC-Youth-Forum","https://www.nonviolenceinternational-ny.org/single-post/2017/01/31/SOLVING-WORLD-PROBLEMS-THROUGH-SPIRITUALITY-WHAT-EACH-ONE-OF-US-CAN-DO"]
for a in range(0,len(Z7)): 
    G = urllib.request.urlopen(Z7[a]).read()
    soup = bs.BeautifulSoup(G.decode('ascii', 'ignore'),'lxml') # parse the html 
    for i in soup.find_all('p'):
        copy7=i.text
        print(copy7)


# In[28]:

import bs4 as bs
import requests
import urllib.request
import re
Z8 = ["https://www.nonviolenceinternational-ny.org/single-post/2016/12/16/Turkey%E2%80%99s-Systematic-Regression-from-the-Rule-of-Law","https://www.nonviolenceinternational-ny.org/single-post/2016/12/12/Tell-Me-About-That-Good-Thing-They-Call-Culture-of-Peace","https://www.nonviolenceinternational-ny.org/single-post/2016/12/09/Activism-against-Gender-Based-Violence-An-Orange-Campaign","https://www.nonviolenceinternational-ny.org/single-post/2016/12/07/Stand-Up-for-Dignity-Human-Rights-and-Spiritual-Rights","https://www.nonviolenceinternational-ny.org/single-post/2016/11/15/Youth-Boosting-the-Promotion-and-Implementation-of-the-SDGs","https://www.nonviolenceinternational-ny.org/single-post/2016/11/03/Presidential-Artillery","https://www.nonviolenceinternational-ny.org/single-post/2016/09/30/Harmonizing-Reporting-for-Global-Regional-Conventional-Arms-Instrument","https://www.nonviolenceinternational-ny.org/single-post/2016/07/29/Private-Sectors-engagement-in-Sustainable-Development-Goals-1","https://www.nonviolenceinternational-ny.org/single-post/2016/06/22/Speaking-Life-From-Victim-to-Victor"]
for a in range(0,len(Z8)): 
    H = urllib.request.urlopen(Z8[a]).read()
    soup = bs.BeautifulSoup(H.decode('ascii', 'ignore'),'lxml') # parse the html 
    for i in soup.find_all('p'):
        copy8=i.text
        print(copy8)


# In[39]:

import bs4 as bs
import requests
import urllib.request
import re
Z9 = ["https://www.nonviolenceinternational-ny.org/single-post/2016/06/15/Synergies-Through-Different-Lenses","https://www.nonviolenceinternational-ny.org/single-post/2016/09/30/Beyond-the-Orlando-Shooting","https://www.nonviolenceinternational-ny.org/single-post/2016/06/10/Peace-Brought-by-Angels-1","https://www.nonviolenceinternational-ny.org/single-post/2016/06/09/Civil-Society-as-the-Third-Pillar","https://www.nonviolenceinternational-ny.org/single-post/2016/04/05/Nonviolent-Peaceforce-is-nominated-for-the-2016-Noble-Peace-Prize","https://www.nonviolenceinternational-ny.org/single-post/2016/06/08/Promoting-Program-of-Action-PoA-and-International-Tracing-Instrument-ITI-in-the-Arab-World","https://www.nonviolenceinternational-ny.org/single-post/2016/02/17/WHAT-ISRAEL-IS-AN-APARTHEID-STATE-","https://www.nonviolenceinternational-ny.org/single-post/2016/03/25/Without-Weapons-and-With-Women-A-Civilian-Protection-and-Peacekeeping-Model-1","https://www.nonviolenceinternational-ny.org/single-post/2015/06/26/THE-VATICAN-AND-ONE-STEP-FORWARD","https://www.nonviolenceinternational-ny.org/single-post/2016/07/29/Private-Sectors-engagement-in-Sustainable-Development-Goals","https://www.nonviolenceinternational-ny.org/single-post/2015/05/03/MILITARY-STRIKES"]
for a in range(0,len(Z9)): 
    I = urllib.request.urlopen(Z9[a]).read()
    soup = bs.BeautifulSoup(I.decode('ascii', 'ignore'),'lxml') # parse the html 
    for i in soup.find_all('p'):
        copy9=i.text
        print(copy9)


# In[77]:

import bs4 as bs
import requests
import urllib.request
import re
import pandas as pd

Z9 = ["https://www.nonviolenceinternational-ny.org/single-post/2016/06/15/Synergies-Through-Different-Lenses","https://www.nonviolenceinternational-ny.org/single-post/2016/09/30/Beyond-the-Orlando-Shooting","https://www.nonviolenceinternational-ny.org/single-post/2016/06/10/Peace-Brought-by-Angels-1","https://www.nonviolenceinternational-ny.org/single-post/2016/06/09/Civil-Society-as-the-Third-Pillar","https://www.nonviolenceinternational-ny.org/single-post/2016/04/05/Nonviolent-Peaceforce-is-nominated-for-the-2016-Noble-Peace-Prize","https://www.nonviolenceinternational-ny.org/single-post/2016/06/08/Promoting-Program-of-Action-PoA-and-International-Tracing-Instrument-ITI-in-the-Arab-World","https://www.nonviolenceinternational-ny.org/single-post/2016/02/17/WHAT-ISRAEL-IS-AN-APARTHEID-STATE-","https://www.nonviolenceinternational-ny.org/single-post/2016/03/25/Without-Weapons-and-With-Women-A-Civilian-Protection-and-Peacekeeping-Model-1","https://www.nonviolenceinternational-ny.org/single-post/2015/06/26/THE-VATICAN-AND-ONE-STEP-FORWARD","https://www.nonviolenceinternational-ny.org/single-post/2016/07/29/Private-Sectors-engagement-in-Sustainable-Development-Goals","https://www.nonviolenceinternational-ny.org/single-post/2015/05/03/MILITARY-STRIKES"]
f= open("some.txt","w")
for a in range(0,len(Z9)): 
    I = urllib.request.urlopen(Z9[a]).read()
    soup = bs.BeautifulSoup(I.decode('ascii', 'ignore'),'lxml') # parse the html 
    for i in soup.find_all('p'):
        copy9=i.text
        print(copy9)
        f.write(copy9)
        


# In[ ]:



