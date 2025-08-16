# Step 1: Import the pandas library
import pandas as pd

# Step 2: Load your raw data
# Use a raw string (r"...") for the file path to avoid errors
file_path = r"C:\Users\GayathriHarshitha\Desktop\Uber_Analytics_Project\Uber_Data_Cleaned.xlsx.csv"
df = pd.read_csv(file_path)

# --- DATA CLEANING ---

# Step 3: Remove duplicate bookings based on 'Booking ID'
df.drop_duplicates(subset='Booking ID', inplace=True)

# Step 4: Drop completely empty columns
columns_to_drop = [
    'Cancelled Rides by Customer',
    'Reason for cancelling by Customer',
    'Cancelled Rides by Driver',
    'Driver Cancellation Reason'
]
# Use errors='ignore' in case a column doesn't exist
df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Step 5: Clean text columns by trimming whitespace
text_columns = [
    'Booking Status', 'Vehicle Type', 'Pickup Location', 'Drop Location',
    'Incomplete Rides Reason', 'Payment Method'
]
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# Step 6: Correct data types and combine Date/Time
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce').dt.time

# IMPORTANT: Drop any rows where the date or time could not be properly read
df.dropna(subset=['Date', 'Time'], inplace=True)

# Combine Date and Time into a single 'BookingTimestamp' column
# This is the modern, correct way to combine them.
df['BookingTimestamp'] = df.apply(
    lambda row: pd.Timestamp.combine(row['Date'].date(), row['Time']),
    axis=1
)

# Now that we have the combined timestamp, we can drop the original columns
df.drop(columns=['Date', 'Time'], inplace=True)


# Step 7: Convert other numeric columns
numeric_columns = ['Booking Value', 'Ride Distance', 'Driver Ratings', 'Customer Rating']
for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Step 8: Handle potential outliers
if 'Ride Distance' in df.columns:
    df = df[df['Ride Distance'] <= 500]

# --- FINAL CHECKS & SAVE ---

print("--- Cleaned Data Sample ---")
print(df.head())
print("\n--- Data Types After Final Cleaning ---")
df.info()

# Step 9: Save the cleaned data to a new CSV file
output_file_path = 'Uber_Data_Cleaned.csv'
df.to_csv(output_file_path, index=False)

print(f"\n✅ Final cleaning complete! Cleaned data saved to '{output_file_path}'")