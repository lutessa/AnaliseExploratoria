import pandas as pd

# Separa fotos do City_Street_View_Dataset pelas regiões
city_bounds = {
    'San Francisco': {'lat_min': 37.6, 'lat_max': 37.9, 'lon_min': -123.0, 'lon_max': -122.3},
    'Detroit': {'lat_min': 42.2, 'lat_max': 42.5, 'lon_min': -83.3, 'lon_max': -82.9},
    'Chicago': {'lat_min': 41.6, 'lat_max': 42.1, 'lon_min': -88.0, 'lon_max': -87.5},
    'Washington': {'lat_min': 38.8, 'lat_max': 39.0, 'lon_min': -77.1, 'lon_max': -76.9},
    'New York City': {'lat_min': 40.5, 'lat_max': 40.9, 'lon_min': -74.3, 'lon_max': -73.7}
}


original_file = r'C:\Users\Raissa\Documents\dev\TCC\City_Street_View_Dataset\picture_coords.csv'
df = pd.read_csv(original_file, header=None, names=['latitude', 'longitude'])


df['line_number'] = df.index + 1


def determine_city(lat, lon):
    for city, bounds in city_bounds.items():
        if (bounds['lat_min'] <= lat <= bounds['lat_max']) and (bounds['lon_min'] <= lon <= bounds['lon_max']):
            return city
    return None


df['city'] = df.apply(lambda row: determine_city(row['latitude'], row['longitude']), axis=1)

for city in city_bounds.keys():
    city_df = df[df['city'] == city]
    if not city_df.empty:
        output_file = f'{city}.csv'
        city_df[['latitude', 'longitude', 'line_number']].to_csv(output_file, index=False)
    