install.packages(c('ggplot2', 'e1071', 'caret', 'quanteda', 'irlba', 'randomForest'))

#read file and view
spam.raw<- read.csv("C:\\Users\\Harshil\\Desktop\\R Text Analysis\\spam.csv", stringsAsFactors = FALSE)
View(spam.raw)

#Clean dataframe and view
spam.raw<- spam.raw[,1:2]  #this is to select first two columns and all rows
names(spam.raw)<- c("Label","Text")
View(spam.raw)

#Check for missing values
length(which(!complete.cases(spam.raw)))

#Convert into factor
spam.raw$Label<- as.factor(spam.raw$Label)

#Explore data and look at class label (ham vs label)
prop.table(table(spam.raw$Label))

#get text length
spam.raw$TextLength<- nchar(spam.raw$Text)
summary(spam.raw$TextLength)

#Visualization and adding segementation
library(ggplot2)

ggplot(spam.raw, aes(x = TextLength, fill = Label)) +
       theme_bw() +
      geom_histogram(binwidth=5) +
      labs(y = "Text Count", x = "Length of text",
        title = "Distribution of text length with Labels")

library(caret)
help(package = "caret")

# we need caret to make 70/30 split of the model
#Seed for reproducibility

set.seed(32984)
indexes <- createDataPartition(spam.raw$Label, times = 1, p=0.7, list = FALSE)

train <- spam.raw[indexes,]
test <- spam.raw[-indexes,]

#Verify Proportion
prop.table(table(train$Label))
prop.table(table(test$Label))

#Lets explore some examples for data exploration!
train$Text[21]
train$Text[38]
train$Text[357]

library(quanteda)
help(package = "quanteda")

train.tokens <- tokens(train$Text, what = "word", remove_numbers = TRUE, 
                      remove_punct = TRUE, remove_symbols = TRUE, remove_hyphens = TRUE)

train.tokens[357]

#lowercase everything
train.tokens <- tokens_tolower(train.tokens)
train.tokens[357]

#Use built-in stopword in Quanteda

train.tokens <- tokens_select(train.tokens, stopwords(), selection = "remove")
train.tokens[357]

# Now we do stemming. This changes the similar word like ran, running, run into single word run.
train.tokens <- tokens_wordstem(train.tokens, language = "english")
train.tokens[357]

#Create our first bag of word model.
train.tokens.dfm <- dfm(train.tokens, tolower = FALSE)

#Transform to matrix and inspect
train.tokens.matrix <- as.matrix(train.tokens.dfm)
View(train.tokens.dfm[1:20,1:100])
dim(train.tokens.matrix)

#Investigating the effects of stemming
colnames(train.tokens.matrix)[1:50]


#Setup a feature dataframe with labels
train.tokens.df <- cbind(Label = train$Label, as.data.frame(train.tokens.dfm))

#tokenization require some additional preprocessing
names(train.tokens.df)[c(146, 148, 235, 238)]

#Cleanup column names
names(train.tokens.df) <- make.names(names(train.tokens.df))

names(train.tokens.df)[c(146, 148, 235, 238)]

#use caret to create stratified folds for 10 folds cross validation repeated
#3 times making it 30 random samples

set.seed(48743)
cv.folds <- createMultiFolds(train$Label, k = 10, times = 3)
cv.cntrl <- trainControl(method = "repeatedcv", number = 10, repeats = 3, index = cv.folds)

#doSNOW package to alow for multicore training in parallel
# WARNING- The code is configured to run on a workstationor server-class machine.
# Alter code to suit your HW environment
install.packages("doSNOW")
library(doSNOW)

#time the code execution
start.time <- Sys.time()

#Create a cluster to work on 10 logical core but we are working with 3 below as it takes a lot of time
cl <- makeCluster(3, type = "SOCK")
registerDoSNOW(cl)

# Use a single decision tree algo as our first model We use more powerful algo later when we
# shrink the size of our data rpart decision tree

rpart.cv.1 <- train(Label ~ ., data = train.tokens.df, method = "rpart",
                    trControl = cv.cntrl, tuneLength = 7)
# processing is done stop cluster
stopCluster(cl)

# total time of execution
total.time <- Sys.time() - start.time
total.time

#Check out the results
rpart.cv.1
