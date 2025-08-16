import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time

# --- SETUP ---
# Initialize the geocoder. The user_agent is important.
# You can name it after your project.
geolocator = Nominatim(user_agent="uber_analytics_dashboard")

# Use a rate limiter to avoid overwhelming the free geocoding service.
# This makes 1 request per second.
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# --- LOAD DATA ---
try:
    df = pd.read_csv('Uber_Data_Cleaned.csv')
except FileNotFoundError:
    print("Error: 'Uber_Data_Cleaned.csv' not found. Make sure it's in the same folder.")
    exit()

# Get a unique list of pickup locations
locations = df['Pickup Location'].unique()
print(f"Found {len(locations)} unique pickup locations to geocode.")

# --- GEOCODING PROCESS ---
results = []
for location in locations:
    try:
        # We add ", Delhi, India" to help the geocoder be more accurate
        full_location_name = f"{location}, Delhi, India"
        
        location_data = geocode(full_location_name)
        
        if location_data:
            lat = location_data.latitude
            lon = location_data.longitude
            results.append({'Pickup Location': location, 'Latitude': lat, 'Longitude': lon})
            print(f"✅ Found: {location} -> ({lat}, {lon})")
        else:
            results.append({'Pickup Location': location, 'Latitude': None, 'Longitude': None})
            print(f"❌ Not Found: {location}")
            
    except Exception as e:
        print(f"An error occurred for {location}: {e}")
        results.append({'Pickup Location': location, 'Latitude': None, 'Longitude': None})

# --- SAVE RESULTS ---
# Convert the results list to a DataFrame
coordinates_df = pd.DataFrame(results)

# Save the DataFrame to a CSV file
output_file = 'location_coordinates.csv'
coordinates_df.to_csv(output_file, index=False)

print(f"\nGeocoding complete! Results saved to '{output_file}'.")
print("You can now join this file with your main data in Tableau.")