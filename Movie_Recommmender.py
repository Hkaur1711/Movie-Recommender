#!/usr/bin/env python
# coding: utf-8

# In[21]:


#Loading the ratings dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('ratings.csv')
data.head(10)


# In[22]:


#Loading the movies dataset
movie_titles_genre = pd.read_csv("movies.csv")
movie_titles_genre.head(10)


# In[23]:


#Combining the two datasets
data = data.merge(movie_titles_genre,on='movieId', how='left')
data.head(10)


# In[24]:


#Finding out the average rating for each movie in the dataset
Average_ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
Average_ratings.head(10)


# In[25]:


#Total ratings(count) for each movie
Average_ratings['Total Ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())
Average_ratings.head(10)


# In[26]:


#Histogram for number of ratings
plt.figure(figsize=(8,6))
Average_ratings['Total Ratings'].hist(bins=50)


# In[27]:


#Histogram for average ratings
plt.figure(figsize=(8,6))
Average_ratings['rating'].hist(bins=50)


# In[28]:


#average rating vs no. of ratings
plt.figure(figsize=(8,8))
sns.jointplot(x='rating', y='Total Ratings', data=Average_ratings, alpha=0.4)


# In[29]:


#Matrix representing the rating for each movie by each user
movie_user = data.pivot_table(index='userId',columns='title',values='rating')
movie_user.head(10)


# In[30]:


#Finding the correlation of the selected movie with the other movies in the data
correlations = movie_user.corrwith(movie_user['Toy Story (1995)'])
correlations.head(10)


# In[31]:


#Removing the empty values and merging the total ratings with the correlation table
recommendation = pd.DataFrame(correlations,columns=['Correlation'])
recommendation.dropna(inplace=True)
recommendation = recommendation.join(Average_ratings['Total Ratings'])
recommendation.head(10)


# In[32]:


#Filtering all the movies with a correlation value to 'Toy Story(1995)' and with atleast 100 ratings
recc = recommendation[recommendation['Total Ratings']>100].sort_values('Correlation',ascending=False).reset_index()


# In[33]:


#Merging the movies dataset for verifying the recommendation
recc = recc.merge(movie_titles_genre,on='title', how='left')
recc.head(10)


# In[ ]:




