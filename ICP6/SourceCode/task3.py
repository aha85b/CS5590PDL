# Importing Libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
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
y_cluster_kmeans= km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)

# Scaling dataset before applying PCA Slide#37&38
scaler = StandardScaler()
scaler.fit(x)
x_scaler = scaler.transform(x)
pca = PCA(16)
x_pca = pca.fit_transform(x_scaler)
dataset2 = pd.DataFrame(data=x_pca)
datasetfinal = pd.concat([dataset2,dataset[['TENURE']]],axis=1)

# Applying PCA at KMeans
km = KMeans(n_clusters=3)
km.fit(x_pca)

# Calculating the silhouette score for the above clustering Slide#34
y_cluster_kmeans= km.predict(x_pca)
score = metrics.silhouette_score(x_pca, y_cluster_kmeans)
print('Silhouette Score: \n',  score)

