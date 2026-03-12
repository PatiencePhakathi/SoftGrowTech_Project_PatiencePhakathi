import requests
import folium

response = requests.get("http://ip-api.com/json/")
data = response.json()

lat = data['lat']
lon = data['lon']
city = data['city']
country = data['country']

print("Location:", city, country)

map = folium.Map(location=[lat, lon], zoom_start=10)

folium.Marker(
    [lat, lon],
    popup=f"{city}, {country}"
).add_to(map)

map.save("location_map.html")

print("Map saved as location_map.html")
