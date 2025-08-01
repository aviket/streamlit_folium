import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import os

# -------------------------------
# City coordinates
city_coords = {
    "Mumbai": [19.0760, 72.8777],
    "Pune": [18.5204, 73.8567],
    "Chennai": [13.0827, 80.2707],
    "Delhi": [28.6139, 77.2090],
    "Bhopal": [23.2599, 77.4126],
    "Ahmadabad": [23.0225, 72.5714],
    "Bengluru": [12.9716, 77.5946],
}

geojson_folder = "geojsons"

# -------------------------------
# Sidebar
st.sidebar.title("Navigation Panel")
selected_city = st.sidebar.selectbox("Choose a City", list(city_coords.keys()))

# -------------------------------
# Main Area
st.title("Interactive City Map Viewer")

coords = city_coords[selected_city]
geojson_path = os.path.join(geojson_folder, f"{selected_city}.geojson")
print(f"Loading GeoJSON from: {geojson_path}")
# Initialize map centered on selected city
m = folium.Map(location=coords, zoom_start=11)

# If city's GeoJSON file exists, load and display it
if os.path.exists(geojson_path):
    gdf = gpd.read_file(geojson_path)

    # Add city boundary with tooltip
    folium.GeoJson(
        gdf,
        name=selected_city,

    ).add_to(m)
else:
    st.warning(f"No GeoJSON file found for {selected_city}")

# Add a marker for the city
folium.Marker(
    location=coords,
    popup=selected_city,
    tooltip=f"You are viewing {selected_city}"
).add_to(m)

# Display map
st_folium(m, width=950, height=600)
