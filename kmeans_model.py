import pandas as pd
from sklearn.cluster import KMeans
import joblib

df = pd.read_csv('city_coordinates.csv')  
X = df[['Latitude', 'Longitude']]

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

joblib.dump(kmeans, 'kmeans_model.pkl')
print("Model saved.")
