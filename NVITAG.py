
# coding: utf-8

# In[2]:

import bs4 as bs
import requests
import urllib.request
import re
Z1 = ["https://www.nonviolenceinternational-ny.org/single-post/2018/06/04/How-a-Violent-Conflict-Came-to-Be","https://www.nonviolenceinternational-ny.org/single-post/2018/06/01/NYC-Youth-Over-Guns-March","https://www.nonviolenceinternational-ny.org/single-post/2018/04/26/How-do-we-Reform-Sustaining-Peace","https://www.nonviolenceinternational-ny.org/single-post/2018/05/03/Zambia%E2%80%99s-Hidden-Gems","https://www.nonviolenceinternational-ny.org/single-post/Trumping-the-Norm","https://www.nonviolenceinternational-ny.org/single-post/2018/04/19/Funding-for-Teachers-vs-Funding-for-Guns","https://www.nonviolenceinternational-ny.org/single-post/2018/03/30/A-Landmine-Model-for-Peace","https://www.nonviolenceinternational-ny.org/single-post/2018/04/05/Organ-Trafficking-Education-and-War-Women-and-Their-Plight-for-Sustainable-Lives","https://www.nonviolenceinternational-ny.org/single-post/2018/03/15/Trumps-Empty-Offices","https://www.nonviolenceinternational-ny.org/single-post/2018/03/18/The-2018-Preparatory-Committee"]
for a in range(0,len(Z1)): 
    A = urllib.request.urlopen(Z1[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        for j in soup.find_all(class_="font_5"):
            print(j.text)
            print(i.text)


# In[25]:

import bs4 as bs
import requests
import urllib.request
import re
Z1 = ["https://www.nonviolenceinternational-ny.org/single-post/2018/06/04/How-a-Violent-Conflict-Came-to-Be"]
for a in range(0,len(Z1)): 
    A = urllib.request.urlopen(Z1[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all("h1",class_="font_5"):
        print("Heading:",j.text)
    for k in soup.find_all(id = "comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_daterichTextContainer",class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
        print("Date:",k.text)
    for l in soup.find_all(class_="flex_display",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_def_13"):
        print("Author:",l.text)
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        print("Tags:",i.text)


# !In[26]:

import bs4 as bs
import requests
import urllib.request
import re
Z1 = ["https://www.nonviolenceinternational-ny.org/single-post/2018/06/04/How-a-Violent-Conflict-Came-to-Be","https://www.nonviolenceinternational-ny.org/single-post/2018/06/01/NYC-Youth-Over-Guns-March","https://www.nonviolenceinternational-ny.org/single-post/2018/04/26/How-do-we-Reform-Sustaining-Peace","https://www.nonviolenceinternational-ny.org/single-post/2018/05/03/Zambia%E2%80%99s-Hidden-Gems","https://www.nonviolenceinternational-ny.org/single-post/Trumping-the-Norm","https://www.nonviolenceinternational-ny.org/single-post/2018/04/19/Funding-for-Teachers-vs-Funding-for-Guns","https://www.nonviolenceinternational-ny.org/single-post/2018/03/30/A-Landmine-Model-for-Peace","https://www.nonviolenceinternational-ny.org/single-post/2018/04/05/Organ-Trafficking-Education-and-War-Women-and-Their-Plight-for-Sustainable-Lives","https://www.nonviolenceinternational-ny.org/single-post/2018/03/15/Trumps-Empty-Offices","https://www.nonviolenceinternational-ny.org/single-post/2018/03/18/The-2018-Preparatory-Committee"]
for a in range(0,len(Z1)): 
    A = urllib.request.urlopen(Z1[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all("h1",class_="font_5"):
        print("Heading:",j.text)
    for k in soup.find_all(id = "comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_daterichTextContainer",class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
        print("Date:",k.text)
    for l in soup.find_all(class_="flex_display",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_def_13"):
        print("Author:",l.text)
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        print("Tags:",i.text)


# In[31]:

import bs4 as bs
import requests
import urllib.request
import re
Z1 = ["https://www.nonviolenceinternational-ny.org/single-post/2018/06/04/How-a-Violent-Conflict-Came-to-Be","https://www.nonviolenceinternational-ny.org/single-post/2018/06/01/NYC-Youth-Over-Guns-March","https://www.nonviolenceinternational-ny.org/single-post/2018/04/26/How-do-we-Reform-Sustaining-Peace","https://www.nonviolenceinternational-ny.org/single-post/2018/05/03/Zambia%E2%80%99s-Hidden-Gems","https://www.nonviolenceinternational-ny.org/single-post/Trumping-the-Norm","https://www.nonviolenceinternational-ny.org/single-post/2018/04/19/Funding-for-Teachers-vs-Funding-for-Guns","https://www.nonviolenceinternational-ny.org/single-post/2018/03/30/A-Landmine-Model-for-Peace","https://www.nonviolenceinternational-ny.org/single-post/2018/04/05/Organ-Trafficking-Education-and-War-Women-and-Their-Plight-for-Sustainable-Lives","https://www.nonviolenceinternational-ny.org/single-post/2018/03/15/Trumps-Empty-Offices","https://www.nonviolenceinternational-ny.org/single-post/2018/03/18/The-2018-Preparatory-Committee"]
Z2 = ["https://www.nonviolenceinternational-ny.org/single-post/2018/03/08/Teenage-boy-shot-and-killed-after-a-car-accident-with-Conceal-and-Carry-holder","https://www.nonviolenceinternational-ny.org/single-post/2018/03/01/Uneven-Progress-The-Aging-of-the-Beijing-Declaration","https://www.nonviolenceinternational-ny.org/single-post/2018/02/15/Toxic-Trump","https://www.nonviolenceinternational-ny.org/single-post/2018/02/22/Disarming-West-Africa","https://www.nonviolenceinternational-ny.org/single-post/2018/01/25/New-Conservatism-Lincoln-and-Trump","https://www.nonviolenceinternational-ny.org/single-post/2018/02/13/North-Korea-and-Denuclearization","https://www.nonviolenceinternational-ny.org/single-post/2017/12/28/How-SDG-164-is-Making-You-Safer","https://www.nonviolenceinternational-ny.org/single-post/2018/01/05/NRA-vs-NRA","https://www.nonviolenceinternational-ny.org/single-post/2017/12/01/They-Are-the-LAWS-Killer-Robots-and-Trump","https://www.nonviolenceinternational-ny.org/single-post/2017/12/21/Why-is-the-West-Turning-a-Blind-Eye-Towards-Yemen"]
Z3 = ["https://www.nonviolenceinternational-ny.org/single-post/2017/11/16/The-Kashmir-Issue","https://www.nonviolenceinternational-ny.org/single-post/2017/11/15/The-Heinous-Humanitarian-Cost-of-Modern-Warfare","https://www.nonviolenceinternational-ny.org/single-post/2017/11/03/Examining-Synergies-Between-the-UN-POA-ATT-and-SDGs","https://www.nonviolenceinternational-ny.org/single-post/2017/11/09/PEACE-BOAT-GLOBAL-VOYAGES-FOR-PEACE","https://www.nonviolenceinternational-ny.org/single-post/2017/10/26/Sustainability-vs-Displacement","https://www.nonviolenceinternational-ny.org/single-post/2017/11/01/Re-Examining-the-PoA","https://www.nonviolenceinternational-ny.org/single-post/2017/10/25/Scrapping-the-Surplus-IANSA-Side-Event","https://www.nonviolenceinternational-ny.org/single-post/2017/10/25/The-Second-Amendment-Conservatives-and-Irony","https://www.nonviolenceinternational-ny.org/single-post/2017/10/16/A-President-Meets-With-Civil-Society","https://www.nonviolenceinternational-ny.org/single-post/2017/10/18/The-15th-Anniversary-of-the-Hague-Code-of-Conduct"]
Z4 = ["https://www.nonviolenceinternational-ny.org/single-post/2017/10/11/Rose-Welsch-Speaks-at-the-First-Committee","https://www.nonviolenceinternational-ny.org/single-post/2017/10/11/Spirituality-Psychology-and-the-Eight-Pillars-of-Peace","https://www.nonviolenceinternational-ny.org/single-post/2017/10/10/How-Guns-Shift-Conflict-Towards-Violence-Part-5","https://www.nonviolenceinternational-ny.org/single-post/2017/10/09/How-Guns-Shift-Conflict-Towards-Violence-Part-4","https://www.nonviolenceinternational-ny.org/single-post/2017/10/07/How-Guns-Shift-Conflict-Towards-Violence-Part-2","https://www.nonviolenceinternational-ny.org/single-post/2017/10/08/How-Guns-Shift-Conflict-Towards-Violence-Part-3","https://www.nonviolenceinternational-ny.org/single-post/2017/10/06/How-Guns-Shift-Conflict-Towards-Violence-Part-1","https://www.nonviolenceinternational-ny.org/single-post/Path-of-NonviolenceNY","https://www.nonviolenceinternational-ny.org/single-post/2017/09/28/A-Framework-For-Peace","https://www.nonviolenceinternational-ny.org/single-post/2017/09/21/The-Evolution-of-Violent-Conflict"]
Z5 = ["https://www.nonviolenceinternational-ny.org/single-post/2017/09/14/International-Day-of-Peace","https://www.nonviolenceinternational-ny.org/single-post/2017/08/11/An-HLPF-To-Remember","https://www.nonviolenceinternational-ny.org/single-post/2017/08/02/My-HLPF-2017-Reflections-and-Recognitions","https://www.nonviolenceinternational-ny.org/single-post/2017/07/28/Peaceful-Just-and-Inclusive-Societies-and-the-SDGs","https://www.nonviolenceinternational-ny.org/single-post/2017/07/26/An-Intern%25E2%2580%2599s-Perspective-on-the-HLPF","https://www.nonviolenceinternational-ny.org/single-post/2017/07/21/Women-Reproductive-Health-and-Sustainable-Development","https://www.nonviolenceinternational-ny.org/single-post/2017/07/17/Reproductive-Rights-and-the-2030-Agenda","https://www.nonviolenceinternational-ny.org/single-post/2017/07/14/Spreading-the-International-Day-of-Peace-A-Grassroots-Effort","https://www.nonviolenceinternational-ny.org/single-post/URGENT-ACTION-NEEDED","https://www.nonviolenceinternational-ny.org/single-post/2017/07/14/50-Years-of-Israeli-Occupation-Moving-Forward"]
Z6 = ["https://www.nonviolenceinternational-ny.org/single-post/2017/07/08/International-Gun-Destruction-Day-Scrap-the-Surplus","https://www.nonviolenceinternational-ny.org/single-post/2017/07/07/The-Importance-of-the-Intergenerational-Dialogues-on-Sustainable-Development-Goals","https://www.nonviolenceinternational-ny.org/single-post/2017/07/01/BeyondTheWageGapCEDAWandGenderEquality","https://www.nonviolenceinternational-ny.org/single-post/2017/07/07/The-Straw-Thing-Technology-Education-for-Sustainable-Oceans","https://www.nonviolenceinternational-ny.org/single-post/2017/06/26/PremonitionOfDangerMartialLawInThePhilippines","https://www.nonviolenceinternational-ny.org/single-post/2017/06/24/SmallIslandsBigChallengesRoadblocksInThePathToASustainableFuture","https://www.nonviolenceinternational-ny.org/single-post/WhyWeNeedALeaderLikeDag-HammarskjoldNowMoreThanEver","https://www.nonviolenceinternational-ny.org/single-post/FiveAwakeLightsAFire","https://www.nonviolenceinternational-ny.org/single-post/2017/04/21/Nadia-Murad-The-Fight-for-Justice","https://www.nonviolenceinternational-ny.org/single-post/InDisarmementNegotiationsWomenMatter"]
Z7 = ["https://www.nonviolenceinternational-ny.org/single-post/2017/04/14/Finding-Brightness-in-Darkness-The-Story-of-One-Syrian-Refugee","https://www.nonviolenceinternational-ny.org/single-post/2017/04/07/A-Step-in-Our-Mission-Towards-Peace","https://www.nonviolenceinternational-ny.org/single-post/2017/03/31/The-Solace-of-Music-Amid-Chaos","https://www.nonviolenceinternational-ny.org/single-post/CSWTheInternsPerspective","https://www.nonviolenceinternational-ny.org/single-post/InternationalWomesDay","https://www.nonviolenceinternational-ny.org/single-post/2017/03/03/The-Pandemic-of-Indifference","https://www.nonviolenceinternational-ny.org/single-post/2017/02/24/How-Does-Gender-Inequality-Affect-Sustainable-Peace-and-Development","https://www.nonviolenceinternational-ny.org/single-post/2017/02/16/The-55th-Commission-for-Social-Developments-Opening-Address-Presented-by-Daniel-Perell","https://www.nonviolenceinternational-ny.org/single-post/2017/02/10/The-ECOSOC-Youth-Forum","https://www.nonviolenceinternational-ny.org/single-post/2017/01/31/SOLVING-WORLD-PROBLEMS-THROUGH-SPIRITUALITY-WHAT-EACH-ONE-OF-US-CAN-DO"]
Z8 = ["https://www.nonviolenceinternational-ny.org/single-post/2016/12/16/Turkey%E2%80%99s-Systematic-Regression-from-the-Rule-of-Law","https://www.nonviolenceinternational-ny.org/single-post/2016/12/12/Tell-Me-About-That-Good-Thing-They-Call-Culture-of-Peace","https://www.nonviolenceinternational-ny.org/single-post/2016/12/09/Activism-against-Gender-Based-Violence-An-Orange-Campaign","https://www.nonviolenceinternational-ny.org/single-post/2016/12/07/Stand-Up-for-Dignity-Human-Rights-and-Spiritual-Rights","https://www.nonviolenceinternational-ny.org/single-post/2016/11/15/Youth-Boosting-the-Promotion-and-Implementation-of-the-SDGs","https://www.nonviolenceinternational-ny.org/single-post/2016/11/03/Presidential-Artillery","https://www.nonviolenceinternational-ny.org/single-post/2016/09/30/Harmonizing-Reporting-for-Global-Regional-Conventional-Arms-Instrument","https://www.nonviolenceinternational-ny.org/single-post/2016/07/29/Private-Sectors-engagement-in-Sustainable-Development-Goals-1","https://www.nonviolenceinternational-ny.org/single-post/2016/06/22/Speaking-Life-From-Victim-to-Victor"]
Z9 = ["https://www.nonviolenceinternational-ny.org/single-post/2016/06/15/Synergies-Through-Different-Lenses","https://www.nonviolenceinternational-ny.org/single-post/2016/09/30/Beyond-the-Orlando-Shooting","https://www.nonviolenceinternational-ny.org/single-post/2016/06/10/Peace-Brought-by-Angels-1","https://www.nonviolenceinternational-ny.org/single-post/2016/06/09/Civil-Society-as-the-Third-Pillar","https://www.nonviolenceinternational-ny.org/single-post/2016/04/05/Nonviolent-Peaceforce-is-nominated-for-the-2016-Noble-Peace-Prize","https://www.nonviolenceinternational-ny.org/single-post/2016/06/08/Promoting-Program-of-Action-PoA-and-International-Tracing-Instrument-ITI-in-the-Arab-World","https://www.nonviolenceinternational-ny.org/single-post/2016/02/17/WHAT-ISRAEL-IS-AN-APARTHEID-STATE-","https://www.nonviolenceinternational-ny.org/single-post/2016/03/25/Without-Weapons-and-With-Women-A-Civilian-Protection-and-Peacekeeping-Model-1","https://www.nonviolenceinternational-ny.org/single-post/2015/06/26/THE-VATICAN-AND-ONE-STEP-FORWARD","https://www.nonviolenceinternational-ny.org/single-post/2016/07/29/Private-Sectors-engagement-in-Sustainable-Development-Goals","https://www.nonviolenceinternational-ny.org/single-post/2015/05/03/MILITARY-STRIKES"]

for a in range(0,len(Z1)): 
    A = urllib.request.urlopen(Z1[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all("h1",class_="font_5"):
        print("Heading1:",j.text)
    for k in soup.find_all(id = "comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_daterichTextContainer",class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
        print("Date:",k.text)
    for l in soup.find_all(class_="flex_display",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_def_13"):
        print("Author:",l.text)
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        print("Tags:",i.text)
        
for a in range(0,len(Z2)): 
    A = urllib.request.urlopen(Z2[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all("h1",class_="font_5"):
        print("Heading2:",j.text)
    for k in soup.find_all(id = "comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_daterichTextContainer",class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
        print("Date:",k.text)
    for l in soup.find_all(class_="flex_display",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_def_13"):
        print("Author:",l.text)
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        print("Tags:",i.text)
        
for a in range(0,len(Z3)): 
    A = urllib.request.urlopen(Z3[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all("h1",class_="font_5"):
        print("Heading3:",j.text)
    for k in soup.find_all(id = "comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_daterichTextContainer",class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
        print("Date:",k.text)
    for l in soup.find_all(class_="flex_display",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_def_13"):
        print("Author:",l.text)
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        print("Tags:",i.text)
        
for a in range(0,len(Z4)): 
    A = urllib.request.urlopen(Z4[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all("h1",class_="font_5"):
        print("Heading4:",j.text)
    for k in soup.find_all(id = "comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_daterichTextContainer",class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
        print("Date:",k.text)
    for l in soup.find_all(class_="flex_display",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_def_13"):
        print("Author:",l.text)
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        print("Tags:",i.text)
        
for a in range(0,len(Z5)): 
    A = urllib.request.urlopen(Z5[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all("h1",class_="font_5"):
        print("Heading5:",j.text)
    for k in soup.find_all(id = "comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_daterichTextContainer",class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
        print("Date:",k.text)
    for l in soup.find_all(class_="flex_display",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_def_13"):
        print("Author:",l.text)
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        print("Tags:",i.text)
        
for a in range(0,len(Z6)): 
    A = urllib.request.urlopen(Z6[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all("h1",class_="font_5"):
        print("Heading6:",j.text)
    for k in soup.find_all(id = "comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_daterichTextContainer",class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
        print("Date:",k.text)
    for l in soup.find_all(class_="flex_display",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_def_13"):
        print("Author:",l.text)
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        print("Tags:",i.text)
        
for a in range(0,len(Z7)): 
    A = urllib.request.urlopen(Z7[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all("h1",class_="font_5"):
        print("Heading7:",j.text)
    for k in soup.find_all(id = "comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_daterichTextContainer",class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
        print("Date:",k.text)
    for l in soup.find_all(class_="flex_display",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_def_13"):
        print("Author:",l.text)
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        print("Tags:",i.text)
        
for a in range(0,len(Z8)): 
    A = urllib.request.urlopen(Z8[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all("h1",class_="font_5"):
        print("Heading8:",j.text)
    for k in soup.find_all(id = "comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_daterichTextContainer",class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
        print("Date:",k.text)
    for l in soup.find_all(class_="flex_display",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_def_13"):
        print("Author:",l.text)
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        print("Tags:",i.text)
        
for a in range(0,len(Z9)): 
    A = urllib.request.urlopen(Z9[a]).read()
    soup = bs.BeautifulSoup(A.decode('ascii', 'ignore'),'lxml') # parse the html 
    for j in soup.find_all("h1",class_="font_5"):
        print("Heading9:",j.text)
    for k in soup.find_all(id = "comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_daterichTextContainer",class_="s_usaAWRichTextClickableSkin_richTextContainer s_usaAWRichTextClickableSkinrichTextContainer"):
        print("Date:",k.text)
    for l in soup.find_all(class_="flex_display",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_def_13"):
        print("Author:",l.text)
    for i in soup.find_all(class_="s_pQyQInlineSkin",id ="comp-irns72fq_SinglePostMediaTop_MediaPost__0_0_tags"):
        print("Tags:",i.text)

