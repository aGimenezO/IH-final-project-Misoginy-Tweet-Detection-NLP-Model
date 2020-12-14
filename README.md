# IH-final-project

## Table of contents
1.[Motivation of this Project](#motivation)

2.[Steps](#steps)

  2.1.[Gather Data](#data)
  
  2.2. [Data Cleaning](#cleaning)
  
  2.3. [TF-IDF](#tfidf)
  
  2.4. [Word2vec](#word2vec)
  
  2.5. [Conclusions](#conclusions)
  
  
<a name="motivation"></a>
# Motivation of this project
It's impossible to not see that some areas of internet can be extremely sexist, as someone who uses twitter actively, I've come around all kind of messages and I had the idea for the final project, a Misogynic comments detector.
As someone who tries to fight against any kind of discrimination this seemed like both an ethical an exciting technically speaking project.

<a name="steps"></a>
# Steps

<a name="data"></a>
## Gather Data
To obtain my tweets I learned and used [Tweepy](https://www.tweepy.org/). While I was obtaining my data, since I first had to familiarize myself with twitter's API, I came accross a similar project another student from another promotion did before me, since I started to think I wouldn't have enough time to work on the next step since it also involved some technologies we didn't really delved really deep into (NLP) y prefered to use her dataset since it was already classfied and classifying my 7k would be really time consuming and I was afraid I couldn't make it to the deadline with a finished project. Credits for the data to Mar Cánovas.

Regardless of that The Data extraction notebook contains methods to obtain tweets both from a list of Id's and also from Queries, storing them on dataframes , so any further study could use those methods to investigate new sets of data.

<a name="cleaning"></a>
## Data Cleaning

After checking all the information I could retrieve from the tweets, all the information I required for the analysis was the text of it so the only data cleaning required was to keep only the Text.Line breaks were removed and also all punctuation signs and stopwords were removed from the text, although this last 2 items removed were done on the Tokenization step.

<a name="tfidf"></a>
## TF-IDF

Here I tokenized my texts using [Spacy](https://spacy.io/) using a pipeline, where I also tried several models (RandomForests,MLP,XGBooster) using RandomSearchCV first to narrow the hyperparameter optimization and later GridSearchCV to have more precision.


![TFIDFModel](https://i.gyazo.com/ec6f19874f4af6a9f64f1a96f992a2cc.png "TF-IDF + RandomForest")

<a name="word2vec"></a>
## Word2Vec

The other approach I tried is [Word2vec](https://en.wikipedia.org/wiki/Word2vec/), first using spacy as well , but the results were really poor, using all 3 models mentioned earlier, the issues with the NLP model was probably that it was trained used wikipedia and the syntax and usage of language may difer from what someone can expect on mysoginistic comments on twitter. 

After using [FastText] https://fasttext.cc/ model for spanish, which vectorized the sentences into 300 values , more than the double than spacy's models(128), I tried again with all models, and the results were far superior, by a 15% increase. Even tho the results weren't as successful as TF-IDF they were far more balanced.

![Word2VecModel](https://i.gyazo.com/408780c5606095685f05fe53af1430ca.png "Word2Vec + MLP")

<a name="conclusions"></a>
## Conclusions

The results of the models, even when optimized through the ussage of the tools described didn't feet really high accuracies, since the accuracy displayed on TF-iDF contained tons of bias and had lots of false positives. And Word2Vec had some more balanced results in terms of bias, but the accuracy overall wasn't sufficient to make any reasonable conclusions from its ussage. Therefore any posterior analysis of any Twitter groups/hastags, friends circle , is posponed until the accuracy of the models used is increased significantly.

This has been a really fun project, I've learnt a lot doing it, and certainly will try to learn more to improve it till it can be of relaiable on its results.
