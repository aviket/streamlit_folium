# 🌍 Interactive City Map Viewer

This is a **Streamlit-based web app** that lets you select a city and visualize its location and boundaries using **GeoJSON files** on an interactive map.

## 🚀 About the Project

This project combines three powerful Python libraries:

- Streamlit → A framework to turn Python scripts into interactive web apps quickly, without any frontend coding.
- GeoPandas → An extension of pandas designed to handle geospatial data, such as shapefiles and GeoJSON files.
- Folium → A Python wrapper for Leaflet.js to create interactive maps easily.


## 📂 Features

- Choose a city from the sidebar.
- View its location on an interactive map.
- Load and display corresponding GeoJSON boundaries (if available).
- Marker popup tooltip for quick identification.


## 🛠️ How to Run This App Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/aviket/streamlit_folium.git
cd streamlit_folium
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

Make sure you have Python 3.8+ installed, then run:

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

The app will start and you can open it in your browser (usually at http://localhost:8501).

## 🌐 Deploying on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to https://share.streamlit.io.
3. Connect your GitHub repo and deploy the app.
4. Access your hosted app via a public URL.


App in this repo is hosted at:
https://appfolium-be5fjfabcwvyqpmgqje9rv.streamlit.app/

## 📜 Credits

All GeoJSON files used in this project are credited to:
** 🔗 https://github.com/datta07/INDIAN-SHAPEFILES.git **
