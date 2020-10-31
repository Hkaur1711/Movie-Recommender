### Movie-Recommender

*Recommendation systems have become increasingly popular these days. Because of their ability to assign a preference or rating to a particular item they find a broad scope of application in domains like restaurants,movie,online shopping and so on*.

**This project demonstrates a simple content based movie recommendation system. Content based filtering uses similarity in content attributes to make suggestions to a user**. 

*The datasets used in the project can be downloaded from [MovieLens](https://grouplens.org/datasets/movielens/)*

*The first steps involve the exploratory data analysis followed by finding the <u>total ratings</u> and the <u>average rating</u> for each movie in the dataset shown by the plots below.*

![Total_ratings](E:\My_projects\Movie-Recommender\No._of_ratings.png)

​                                                                *Histogram for total ratings*

![average_rating](E:\My_projects\Movie-Recommender\average_rating.png)

​                                                            *Histogram for average rating*

*A particular movie from the dataset is selected and a correlation is calculated for every other movie with the selected movie. In this case the movie selected is <u>'Toy Story(1995)'</u>*

*The output is the list of top 10 most correlated movie with the selected movie*

![output](E:\My_projects\Movie-Recommender\Output.PNG)

> *The most correlated movie as the output shows is <u>'Toy Story(1995)'</u> itself. Thus, the model is working as expected*