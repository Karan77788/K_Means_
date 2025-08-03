from flask import Flask, render_template, request
import pandas as pd
import joblib
import plotly.express as px
import plotly
import json

app = Flask(__name__)
model = joblib.load('kmeans_model.pkl')
data = pd.read_csv('city_coordinates.csv')

@app.route('/', methods=['GET'])
def index():
    X = data[['Latitude', 'Longitude']]
    data['Cluster'] = model.predict(X)
    
    fig = px.scatter_mapbox(
        data,
        lat='Latitude',
        lon='Longitude',
        color='Cluster',
        mapbox_style='open-street-map',
        zoom=3,
        title='K-Means Clustering of City Locations'
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)
