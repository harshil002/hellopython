from bs4 import BeautifulSoup
import re
import time
import requests

def getTextLen(review):
    return len(review)
    
def getCritic(review):
    criticChunk=review.find('a',{'href':re.compile('/critic/')})
    if criticChunk:  return criticChunk.text
    else: return 'NA'
    
def getRating(review):
    ratingChunk = review.find('div',{'class':'review_icon icon small fresh'})
    if ratingChunk:
        return 'fresh'
    elif review.find('div',{'class':'review_icon icon small rotten'}):
        return 'rotten'
    return 'NA'

def getSource(review):
    sourceChunk = review.find('em',{'class':'subtle'})
    if sourceChunk: return sourceChunk.text
    else: return 'NA'
    
def getDate(review):
    myDate = review.find('div',{'class':'review_date subtle small'})
    if myDate: return myDate.text
    else: return 'NA'

def run(url):

    pageNum=1 # number of pages to collect

    fw=open('reviews.txt','w') # output file
	
    for q in range(1,pageNum+1): # for each page 

        print ('page',q)
        html=None

        if q==1: pageLink=url # url for page 1
        else: pageLink=url+'?page='+str(p)+'&sort=' # make the page url
		
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
#                time.sleep(2) # wait 2 secs
				
		
        if not html:continue # couldnt get the page, ignore
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 

        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) # get all the review divs

        for review in reviews:
            
#            text='NA' # initialize critic and text 
            
#            textChunk=review.find('div',{'class':'the_review'})
#            if textChunk: text=textChunk.text#.encode('ascii','ignore')	
            fw.write(getCritic(review)+'\t'+getRating(review)+'\t'+getSource(review)+'\t'+str(getDate(review))+'\t'+str(getTextLen(review))+'\n') # write to file
#		getCritic(review)+'\t'+getRating(review)+'\t'+getSource(review)+'\t'+getDate(review)+'\t'+getTextLen(review)+
#            time.sleep(2)	# wait 2 secs 

    fw.close()

if __name__=='__main__':
    url='https://www.rottentomatoes.com/m/space_jam/reviews/'
    run(url)

