# Importing Libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")

# Importing dataset from file CC.csv
dataset = pd.read_csv('CC.csv')

# Replacing null values with by the mean Slide#40
dataset.loc[(dataset['MINIMUM_PAYMENTS'].isnull()==True),'MINIMUM_PAYMENTS']=dataset['MINIMUM_PAYMENTS'].mean()
dataset.loc[(dataset['CREDIT_LIMIT'].isnull()==True),'CREDIT_LIMIT']=dataset['CREDIT_LIMIT'].mean()

# Shaping dataset since there are a replacement of null values Slide#37
x = dataset.iloc[:,1:-1]
y = dataset.iloc[:,-1]

# Within Cluster Sum of Squares Slid#35
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,max_iter=300,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
print('Within Cluster Sum of Squares: \n\n',wcss, '\n\n')

# Applying Kmeans Slides#33&34
km = KMeans(n_clusters=3)
km.fit(x)

# Calculating the silhouette score for the above clustering Slide#34
y_cluster_kmeans= km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette Score: \n',  score)