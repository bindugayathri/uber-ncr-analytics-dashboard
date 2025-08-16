<img width="1920" height="996" alt="Screenshot 2025-08-15 195259" src="https://github.com/user-attachments/assets/7a9781dc-ccd4-4901-b66f-e285b0e66268" />
# Uber Ride Analytics Dashboard (Delhi NCR, 2024)

## Project Overview

This project provides a comprehensive analysis of Uber's ride-sharing operations in the Delhi National Capital Region (NCR) for the year 2024. The primary goal was to process, clean, and visualize a raw dataset to uncover actionable insights related to booking patterns, operational efficiency, customer behavior, and financial performance.

The final output is a complete, interactive dashboard built in Tableau, designed to serve as an operational command center.

---

## Key Features & Insights

* **Peak Hour Analysis:** The dashboard clearly identifies the morning (9-10 AM) and evening (5-8 PM) rush hours, providing crucial data for driver incentive programs and demand forecasting.
* **High Success Rate:** A 91% ride success rate indicates strong service reliability.
* **Geospatial Hotspots:** A detailed map visualizes the most popular pickup locations across the NCR, allowing for strategic driver placement.
* **Financial Breakdown:** Analysis shows a strong preference for digital payments, with UPI being the dominant method.
* **Operational Efficiency:** KPIs for driver arrival time (VTAT) and customer wait time (CTAT) provide a measure of the service's real-time performance.

---

## Technical Workflow

### 1. Data Cleaning (Python)
* The raw dataset was cleaned using the **Pandas** library in Python (`clean_data.py`).
* Tasks included removing duplicates, dropping empty columns, trimming whitespace from text fields, and converting data types.

### 2. Geocoding (Python)
* A separate script (`geocode_locations.py`) used the **GeoPy** library to convert unique pickup location names into precise latitude and longitude coordinates.
* The resulting coordinate file (`location_coordinates.csv`) was used to enable map-based visualizations.

### 3. Data Visualization (Tableau)
* The cleaned data and coordinate files were joined and visualized in Tableau.
* The final dashboard (`Uber_Analytics_Dashboard.twbx`) is fully interactive, allowing users to filter the entire dataset by clicking on locations, vehicle types, payment methods, and more.

---

## How to View the Dashboard

1.  Download the `Uber_Analytics_Dashboard.twbx` file from this repository.
2.  Open the file using Tableau Reader (a free tool) or Tableau Desktop.
3.  Interact with the dashboard by clicking on various charts and map points to filter the data.
