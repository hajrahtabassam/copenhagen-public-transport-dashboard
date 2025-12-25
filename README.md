![Python](https://img.shields.io/badge/python-3.10-blue)
![Streamlit](https://img.shields.io/badge/streamlit-v1.30-green)


# copenhagen-public-transport-dashboard

# Description:
This project explores and visualizes passenger trends in Copenhagen public transport. It builds on prior data cleaning and analysis work (from the previous repo), adding an interactive dashboard for deeper insights.

# Previous Work (from old repo):

Cleaned and processed raw CSV/GTFS data

Explored hourly passenger counts per mode (bus, train, metro, tram)

Performed basic statistical analysis to understand trends

# Dashboard Features:

Mode selection: Filter by bus, train, metro, or tram

Hour slider: Select specific hours of the day

KPIs: Total passengers, busiest hour, and top mode

Line chart: Passenger trends over time per selected mode

Download button: Export filtered data as CSV
)

# Setup & Run:

git clone <repo-url>
cd copenhagen-public-transport-dashboard
pip install -r requirements.txt
streamlit run app/app.py


# Dataset:

Cleaned CSV with hourly passenger counts per transport mode

Original raw data from Copenhagen public transport GTFS