#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import tweepy
import json

def search_as_df(search_word,n_results):
    columns = set()
    allowed_types = [str, int,bool]
    tweets_data = []
    for status in tweepy.Cursor(api.search,q=search_words, lang="es", tweet_mode='extended').items(n_results):        
        try:
            status_dict = dict(vars(status))
            keys = status_dict.keys()
            single_tweet_data = {"author": status.author.screen_name,"author_id":str(status.author.id)}
            for k in keys:
                try:
                    v_type = type(status_dict[k])
                except:
                    v_type = None
                if v_type != None:
                    if v_type in allowed_types:
                        single_tweet_data[k] = status_dict[k]
                        columns.add(k)
            if 'retweeted_status' in keys:
                single_tweet_data['full_text'] = status.retweeted_status.full_text
            tweets_data.append(single_tweet_data)
        except:
            continue
    header_cols = list(columns)
    header_cols.append('author')
    header_cols.append("author_id")
    df = pd.DataFrame(tweets_data, columns=header_cols)
    return df


# In[ ]:




