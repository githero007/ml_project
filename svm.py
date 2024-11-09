# -*- coding: utf-8 -*-
"""SVM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B1Kiro-htLeEpiahsOfxAyrQibUVcxwA
"""

# prompt: read this dataset

import pandas as pd

df = pd.read_csv('/content/cleanedDataset.csv')

print(df.head())

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.cluster import KMeans
import numpy as np

# Preprocessing
# Encode categorical variables into numeric values
label_encoder = LabelEncoder()

# Encoding categorical columns
categorical_columns = ['Platform', 'Post Type', 'Audience Gender', 'Audience Location', 'interest']
for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])

# Selecting features for clustering
features = ['Platform', 'Post Type', 'Likes', 'Comments', 'Shares', 'Impressions',
            'Reach', 'Engagement Rate', 'Audience Age', 'Audience Gender', 'Audience Location']

X = data[features]

# Standardizing the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce dimensionality
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Apply SVM for clustering
# Since SVM is not typically used for clustering, we'll combine
# We'll use KMeans for clustering first, and SVM for classification-like behavior based on the clusters.

# Prepare to train SVM with the identified clusters
svm_model = SVC(kernel='linear')
svm_model.fit(X_pca, clusters)

clusters[:10], kmeans.cluster_centers_  # Return the first few cluster assignments and cluster centers
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.cluster import KMeans
import numpy as np


df = pd.read_csv('/content/cleanedDataset.csv')

print(df.head())

# Preprocessing
# Encode categorical variables into numeric values
label_encoder = LabelEncoder()
data = df.copy() # Make a copy of the dataframe to avoid modifying the original

# Encoding categorical columns
categorical_columns = ['Platform', 'Post Type', 'Audience Gender', 'Audience Location', 'interest']
for col in categorical_columns:
    if col in data.columns:
        data[col] = label_encoder.fit_transform(data[col].astype(str)) # Ensure data type is string for label encoding

# Selecting features for clustering
features = ['Platform', 'Post Type', 'Likes', 'Comments', 'Shares', 'Impressions',
            'Reach', 'Engagement Rate', 'Audience Age', 'Audience Gender', 'Audience Location']
selected_features = [col for col in features if col in data.columns]  # Ensure features are in the dataframe

X = data[selected_features]

# Standardizing the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce dimensionality
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Apply KMeans for clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_pca)
clusters = kmeans.labels_

# Print the first few cluster assignments and cluster centers
print(clusters[:10])
print(kmeans.cluster_centers_)



import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.cluster import KMeans
import numpy as np


df = pd.read_csv('/content/cleanedDataset.csv')

print(df.head())

# Preprocessing
# Encode categorical variables into numeric values
label_encoder = LabelEncoder()
data = df.copy() # Make a copy of the dataframe to avoid modifying the original

# Encoding categorical columns
categorical_columns = ['Platform', 'Post Type', 'Audience Gender', 'Audience Location', 'interest']
for col in categorical_columns:
    if col in data.columns:
        data[col] = label_encoder.fit_transform(data[col].astype(str)) # Ensure data type is string for label encoding

# Selecting features for clustering
features = ['Platform', 'Post Type', 'Likes', 'Comments', 'Shares', 'Impressions',
            'Reach', 'Engagement Rate', 'Audience Age', 'Audience Gender', 'Audience Location']
selected_features = [col for col in features if col in data.columns]  # Ensure features are in the dataframe

X = data[selected_features]

# Standardizing the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce dimensionality
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Apply KMeans for clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_pca)
clusters = kmeans.labels_

# Print the first few cluster assignments and cluster centers
print(clusters[:10])
print(kmeans.cluster_centers_)

# prompt: generate visualisations of this cdeo

import matplotlib.pyplot as plt

# Visualize the clusters using a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis')
plt.title('KMeans Clustering with PCA')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()
plt.show()

# You can also create a bar chart to visualize the number of data points in each cluster
cluster_counts = np.bincount(clusters)
plt.figure(figsize=(6, 4))
plt.bar(range(len(cluster_counts)), cluster_counts)
plt.title('Cluster Distribution')
plt.xlabel('Cluster')
plt.ylabel('Number of Data Points')
plt.show()


# Visualize the cluster centers if you want
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=200, c='red', label='Centroids')
plt.title('KMeans Clustering with PCA and Centroids')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.colorbar()
plt.show()

# prompt: apply SVM on this

# Apply SVM for classification based on the clusters
svm_model = SVC(kernel='linear')
svm_model.fit(X_pca, clusters)
predicted_clusters = svm_model.predict(X_pca)
print(predicted_clusters[:10])

# Evaluate the SVM model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(clusters, predicted_clusters)
print("Accuracy:", accuracy)

if X_pca.shape[1] == 2:  # Only for 2D data
    plt.figure(figsize=(8, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis')

    # Create a meshgrid
    x_min, x_max = X_pca[:, 0].min() - 1, X_pca[:, 0].max() + 1
    y_min, y_max = X_pca[:, 1].min() - 1, X_pca[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

    # Predict the cluster for each point in the meshgrid
    Z = svm_model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot the decision boundaries
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
    plt.title('SVM Decision Boundaries for Clusters')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()
else:
    print("Visualization of SVM decision boundaries is only possible for 2D data.")
