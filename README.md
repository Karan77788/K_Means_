# K_Means_

# K-Means Clustering of City GPS Coordinates
```
This project demonstrates **unsupervised learning** using the **K-Means clustering algorithm** to group cities based on their **latitude and longitude** coordinates. The results are visualized through an interactive Flask web application using **Plotly**.
```
---

##  Project Structure
```
K_Means_/
│
├── app.py # Flask backend
├── kmeans_model.py # KMeans model training script
├── gps_coordinates.csv # Sample dataset (30 city points)
├── templates/
│ └── index.html # Frontend HTML template
├── static/
│ └── style.css # CSS styling
├── requirements.txt # Dependencies
└── README.md # Project documentation
```
---

##  Dataset
```
- **Source**: Simulated 30 GPS points (Latitude, Longitude).
- **Format**: CSV
- **Columns**:
  - `City`: City name (optional)
  - `Latitude`: Float
  - `Longitude`: Float
```
---

##  ML Model
```
- **Algorithm**: K-Means Clustering
- **Library**: scikit-learn
- **Number of clusters**: 3 (can be changed)
- **Use Case**: Cluster cities into regions (e.g., delivery zones, service areas)
```
---

##  Web App Features
```
- Submit the number of clusters (k)
- Visualize results using an interactive Plotly scatter plot
- Each cluster shown in a different color with labeled centroids
```
---

##  How to Run

### 1. Clone the repo

```
git clone https://github.com/yourusername/K_Means_GPS_App.git
cd K_Means_GPS_App
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Train the model (optional)
```
python kmeans_model.py
```
4. Run the Flask app
```
python app.py
```

#  Requirements
Listed in requirements.txt:
```
Flask
pandas
plotly
scikit-learn
```
```
pip install -r requirements.txt
```
# Example Screenshot

![alt text](<Screenshot 2025-08-03 154800.png>)
![alt text](<Screenshot 2025-08-03 154815.png>)
![alt text](<Screenshot 2025-08-03 154835.png>)
![alt text](<Screenshot 2025-08-03 154926.png>)