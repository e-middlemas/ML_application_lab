from IPython.display import display, Markdown
class unsupervised():
    def answer1():
        display(Markdown("[Here is a link to the wiki page](https://en.wikipedia.org/wiki/Cluster_analysis#Centroid-based_clustering). Centroids are what are used to define the clusters in K-means clustering. A point is grouped into a specific cluster based on that point's distance from the centroid. In our case, we randomly start with some centroids, and then the algorithm repeatedly chooses new centroids in order to minimize the distances between points and each centroid."))
    
    def answer2():
        display(Markdown("The diurnal cycle would dominate over seasonality and k-means would struggle to correctly separate seasons."))
        
    def answer3():
        display(Markdown("K-means has a much harder time separating seasons. Because the algorithm works based on the distance between points, the features with the highest variance will dominate the clustering algorithm."))
        
    def answer4():
        display(Markdown("Finding the separability between two centroids results in larger distance and this larger separability than that among four centroids for the same amount of data. This idea touches upon [the curse of dimensionality](https://deepai.org/machine-learning-glossary-and-terms/curse-of-dimensionality). When trying to predict four different outcomes instead of two, the data becomes too sparse to accurately separate. Side note: what would make separability easier is if all of the features were independent of each other, i.e., had zero correlation, but some features are collinear."))
    
    def answer5():
        display(Markdown("The answer depends on which feature is removed. Some features are better predictors of season than others. For example, removing insolation would have a bigger effect than windgust."))
     

class supervised():
    def answer1():
        display(Markdown("Let's say you perform feature scaling before the train-test split. This means the scaling of the unseen data (the testing data) *depends on* the training data. <br><br>Now, imagine you are provided the model trained on this data from an external source. You'd like to use the model to determine if some meteorological conditions are going to produce rain. Since the data used to train the model depends on the outcome you're trying to predict, neither you nor the model knows how to scale the new input data in such a way that the model can make an educated guess. The model is unable to contextualize the unseen data. The importance of the order of data preparation is why building *__data preparation pipelines__* is so important in using Machine Learning. The 'gotcha' described above - i.e., performing a test-train split *after* other data preparation - is called *__data leakage__*."))


    def answer2():
        display(Markdown("No one likes an incorrect weather forecast, but people are probably more upset when the forecast calls for a sunny day and it ends up raining. In our case, that means the model would be predicting no precipitation when there actually is precipitation - a false negative. Revisit the equations for accuracy & recall in section 2.1.B, Q7 above. Accuracy and recall contain the number of false negatives in the denominator. Thus, maximizing these metrics require minimizing the number of false negatives. <br><br>Predicted precipitation probability provides a sanity test for us to make sure the model isn't way off base. It allows us to see for ourselves: given X meteorological conditions and our own understanding of meteorology, would rain seem likely? Is the model actually doing something realistic?"))


    def answer3():
        display(Markdown("<br>1. __Logistic regression__ tends to overgeneralize or underfit data, but is easy to implement, to understand and easy to back out feature importance.<br>2. __Singular Vector Machines__ are great at capturing complex relationships, but cannot back out feature importance. Plus, the use of the kernel makes them hard to interpret.<br>3. __Random forests__ are easier to understand, generally do not overfit, and can capture complex relationships, and can provide feature importance, but they can be slow to train and there are a lot of hyperparameters to choose from.<br>4. __Neural Networks__ are great at capturing complex relationships. But they are slow to train and are susceptible to overfitting."))


    def answer4():
        display(Markdown("First, we should assess which features are collinear. If we don't have that many features, we could use our meteorological expertise to simply remove one of the features that shares collinearity with other features. Another way to address collinearity is to use **feature regularization**, or add weights that penalize features that add noise, ultimately reducing model complexity.<br><br>Below, I try re-training the Random Forest model after removing wind_mph, wind_dir, dewtemp_F, windgust_dir, and SOLIN_Wm2.<br><br>"))

        display('Uncomment & run %load collinearity_solution.py below')
    
    
