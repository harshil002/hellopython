install.packages("dplyr")
install.packages("plyr")
install.packages("lubridate")
install.packages("tidyverse")
install.packages("tm")
install.packages("NLP")
install.packages("syuzhet")
install.packages("Rcpp")
install.packages("reshape2")
install.packages("wordcloud")
install.packages("NLP")
install.packages("RColorBrewer")
install.packages("SnowballC")
install.packages("installr")
install.packages("igraph")
install.packages("widyr")
install.packages("ggraph")
library(dplyr)
library(plyr)
library(lubridate)
library(tidyverse)
library(tm)
library(NLP)
library (syuzhet)
library(Rcpp)
library(reshape2)
library(ggplot2)
library(wordcloud)
library(NLP)
library(RColorBrewer)
library(SnowballC)
library(igraph)
library(widyr)
library(NLP)
library(tidytext)
library(ggraph)

#Read CSV File
tweetdata = read.csv("file:///C:/Users/Harshil/Desktop/658/ProjectX/trumptweets_131117_v2.1.csv", header= TRUE)
tweetdata$timeline<- ydm(paste(tweetdata$created_at..year.,tweetdata$created_at..day., tweetdata$created_at..month.,sep="/"))


# Breaking dataset into two group before and after presidency j

tweetdata_bp<-subset(tweetdata,tweetdata$timeline <= ydm("2016/08/11"))
tweetdata_ap<-subset(tweetdata,tweetdata$timeline > ydm("2016/08/11"))

#Text mining from the dataset

dataclean_tweetdata <- function(data){
  # remove retweet entities
  data = gsub("(RT|via)((?:\\b\\W*@\\w+)+)", "", data)
  # remove at people
  data = gsub("@\\w+", "", data)
  # remove punctuation
  data = gsub("[[:punct:]]", "", data)
  # remove numbers
  data = gsub("[[:digit:]]", "", data)
  # remove html links
  data = gsub("http\\w+", "", data)
  # remove unnecessary spaces
  data = gsub("[ \t]{2,}", "", data)
  data = gsub("^\\s+|\\s+$", "", data)
  data = tolower(data)
}

tweetdata$text = dataclean_tweetdata(tweetdata$text)
tweetdata_bp$text = dataclean_tweetdata(tweetdata_bp$text)
tweetdata_ap$text = dataclean_tweetdata(tweetdata_ap$text)

A = data.frame(tweetdata$text)
A$timeline = tweetdata$timeline
colnames(A)<- c("text")
A$syuzhet = get_sentiment(as.character(A$text), method="syuzhet")
B = get_nrc_sentiment(as.character(A$text))
n = names(B)
for (i in n) 
  A[,i]=B[i]

A_bp = data.frame(tweetdata_bp$text)
A_bp$timeline = tweetdata_bp$timeline
colnames(A_bp)<- c("text")
A_bp$syuzhet = get_sentiment(as.character(A_bp$text), method="syuzhet")
C = get_nrc_sentiment(as.character(A_bp$text))
K = names(C)
for (i in K) 
  A_bp[,i]=C[i]


A_ap = data.frame(tweetdata_ap$text)
colnames(A_ap)<- c("text")
A_ap$syuzhet = get_sentiment(as.character(A_ap$text), method="syuzhet")
C = get_nrc_sentiment(as.character(A_ap$text))
K = names(C)
for (i in K) 
  A_ap[,i]=C[i]

monthly_sentiment <- ddply(A, ~timeline, summarize, 
                           anger = mean(anger), 
                           anticipation = mean(anticipation), 
                           disgust = mean(disgust), 
                           fear = mean(fear), 
                           joy = mean(joy), 
                           sadness = mean(sadness), 
                           surprise = mean(surprise), 
                           trust = mean(trust))
monthly_sentiment <- melt(group_by(monthly_sentiment,timeline),id.vars="timeline")
names(monthly_sentiment) <- c("month", "sentiment", "meanvalue")
ggplot(data = monthly_sentiment, aes(x = month, y = meanvalue, group = sentiment)) +
  geom_line(size = 2.5, alpha = 0.7, aes(color = sentiment)) +
  geom_point(size = 0.5)


#timeline = data.frame(month(A_ap$timeline))
#n = names(timeline)
#for (i in n) 
#  A_ap[,i]=timeline[i]
#remove(timeline)
A_ap$timeline = tweetdata_ap$timeline
A_ap$month<-ymd(paste(year(A_ap$timeline),month(A_ap$timeline),1,sep="-"))

monthly_sentiment_ap <- ddply(A_ap, ~month, summarize, 
                           anger = mean(anger), 
                           anticipation = mean(anticipation), 
                           disgust = mean(disgust), 
                           fear = mean(fear), 
                           joy = mean(joy), 
                           sadness = mean(sadness), 
                           surprise = mean(surprise), 
                           trust = mean(trust))
monthly_sentiment_ap <- melt(group_by(monthly_sentiment_ap,month),id.vars="month")
names(monthly_sentiment_ap) <- c("month", "sentiment", "meanvalue")
ggplot(data = monthly_sentiment_ap, aes(x = month, y = meanvalue, group = sentiment)) +
  geom_line(size = 0.5, alpha = 1, aes(color = sentiment)) +
  geom_point(size = 0.5)

#plot(A_ap$sad, A_ap$timeline)
anger = data.frame(monthly_sentiment_ap$sentiment[1:13],monthly_sentiment_ap$month[1:13],monthly_sentiment_ap$meanvalue[1:13])
anger <- melt(group_by(anger,timeline),id.vars="timeline")
names(anger) <- c("sentiment","month" , "meanvalue")
ggplot(data = anger, aes(x = month, y = meanvalue, group = sentiment)) +
  geom_line(size = 0.5, alpha = 1, aes(color = sentiment)) +
  geom_point(size = 0.5)

wordcloud_A = c(
  paste(A$text[A$anger > 0], collapse=" "),
  paste(A$text[A$anticipation > 0], collapse=" "),
  paste(A$text[A$fear > 0], collapse=" "),
  paste(A$text[A$disgust > 0], collapse=" "),
  paste(A$text[A$sadness > 0], collapse=" "),
  paste(A$text[A$joy > 0], collapse=" "),
  paste(A$text[A$surprise > 0], collapse=" "),
  paste(A$text[A$trust > 0], collapse=" ")
)

wordcloud_A = removeWords(wordcloud_A, c(stopwords("english"), 'trump','donald','rt','realdonaldtrump',"duh", "whatever","amp"))
#
# create corpus
corpus_A = Corpus(VectorSource(wordcloud_A))
#
# create term-document matrix
matrix_A = TermDocumentMatrix(corpus_A)
#
# convert as matrix
matrix_A = as.matrix(matrix_A)
#
# add column names
colnames(matrix_A) = c('anger', 'anticipation', 'fear','disgust', 'sadness','joy', 'surprise', 'trust')
#
# Plot comparison wordcloud
layout(matrix(c(1, 2), nrow=2), heights=c(1, 4))
par(mar=rep(0, 4))
plot.new()
text(x=0.5, y=0.5, 'Emotion Comparison Word Cloud ')
comparison.cloud(matrix_A, random.order=FALSE,title.size=1.5, max.words=250,colors = c("#00B2FF", "red", "#FF0099", "#6600CC", "green", "orange", "blue", "brown"))





Ig <- graph(edges=c("matrix_A$anger","matrix_A$fear",directed=FALSE))
plot(Ig)

#graph1 = graph(edges = c("A_a[$anger","A_ap$fear"), directed = FALSE)
#is.directed(graph1)
#summary(graph1)
#plot(graph1)

#degree(graph1)

tweets_desc_ap <- data_frame(id = tweetdata$id_str, desc = tweetdata$text)
tweets_desc_ap <- tweets_desc_ap %>% unnest_tokens(word,desc) %>% anti_join(stop_words)
tweets_desc_ap %>% count(word, sort = TRUE)
tweets_desc_ap

my_stopwords <- data.frame(word = c(as.character(1:10),"rt","donald","trump","realdonaldtrump","amp","whatever","duh"))
tweets_desc_ap <- tweets_desc_ap %>% anti_join(my_stopwords)

desc_word_pairs_ap <- tweets_desc_ap %>% pairwise_count(word, id, sort=TRUE, upper=FALSE)
desc_word_pairs_ap

#plot graph
set.seed(1234)
desc_word_pairs_ap %>%
  filter(n >= 50) %>%
  graph_from_data_frame() %>%
  ggraph(layout = "star") +
  geom_edge_link(aes(edge_alpha = n, edge_width = n), edge_colour = "blue") + 
  geom_node_point(size = 2.5) + 
  geom_node_label(aes(label = name), repel = TRUE,point.padding = unit(0.25, "lines"),label.size=0.05) +
  theme_void()
