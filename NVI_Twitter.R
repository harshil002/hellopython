install.packages(c("devtools", "rjson", "bit64", "httr"))
library(devtools)
install_github("geoffjentry/twitteR", force = TRUE)
library(twitteR)
library(re2r)
library(stringr)
library(igraph)

#install.packages('re2r')
ckey="gub8TbUR00omStsBU5bdUORBT"
csecret="OFoaGlIHRXQ8OkSVEUZCG2h5fZl58tjpMAShaqOjMGW9Dhb6Iv"
atoken="912740766291824640-aQoKnPBvqC2XH2QvgeWC3rS0oBrcJCy"
asecret="7QkVFLYKbu5kcpA6a8e811UxMXChxRdmTatkPYwiVkTXq"

setup_twitter_oauth(ckey,csecret,atoken,asecret)
tweets <- searchTwitter('UN',n=10000, lang = 'en') #n=20000
tweetsdf <- twListToDF(tweets)
write.csv(tweetsdf, file = 'C:/Users/Harshil/Desktop/NVI-UN/NVI_Market Analysis/vio_tweet.csv', row.names = FALSE)

MyData <- sapply(str_extract_all(tweetsdf$text, "#\\S+"), paste, collapse=", ")

write.csv(MyData, file = 'C:/Users/Harshil/Desktop/NVI-UN/NVI_Market Analysis/hashtag_UN.csv', row.names = FALSE)

#MyData <- sapply(str_extract_all(tweetsdf$created, "#\\S+"), paste, collapse=", ")
#MyData <- sapply(str_extract_all(tweetsdf$created_time, "#\\S+"), paste, collapse=", ")
#Dataframe <- read.csv("C:/Users/Harshil/Desktop/NVI-UN/NVI_Market Analysis/hashtag1.csv", header = TRUE)

#Dataframe_Graph = graph(edges = c("Dataframe$text","Dataframe$created"), directed = FALSE)
#is.directed(Dataframe_Graph)
#plot(Dataframe_Graph)
#Dataframe <- graph.data.frame(Dataframe, directed=T)




#1Trend locations
trend <- availableTrendLocations()
trend

#Get Trends
world <- getTrends(1)
head(world) 
tail(world)

Israel <- getTrends(1967449)
head(Israel)
tail(Israel)

Bhopal <- getTrends(2295407)
Bhopal

#User Timeline
t <- userTimeline('#violenceagainstwomen')
