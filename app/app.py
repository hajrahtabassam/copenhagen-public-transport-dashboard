import pandas as pd
import streamlit as st

# read data file 
df = pd.read_csv("data/data.csv")
st.dataframe(df)

# Select modes dynamically
modes = st.multiselect("Select travel modes to display", options=df["transport_mode"].unique(), default=df["transport_mode"].unique())

# Filter by selected modes
filtered = df[df["transport_mode"].isin(modes)]
# Hour slider
hour_range = st.slider(
    "Select hour range",
    min_value=int(df['hour'].min()),
    max_value=int(df['hour'].max()),
    value=(int(df['hour'].min()), int(df['hour'].max()))
)

# Filter by hour
filtered = filtered[(filtered['hour'] >= hour_range[0]) & (filtered['hour'] <= hour_range[1])]


# Pivot so each mode is a column
pivoted = filtered.pivot(index="hour", columns="transport_mode", values="service_count")

# Plot
st.line_chart(pivoted)
# Summary statistics
st.write("### Summary")
st.write("Total passengers:", filtered['service_count'].sum())
st.write("Busiest hour:", filtered.groupby('hour')['service_count'].sum().idxmax())
st.write("Top mode:", filtered.groupby('transport_mode')['service_count'].sum().idxmax())
st.download_button(
    label="Download filtered data as CSV",
    data=filtered.to_csv(index=False),
    file_name="filtered_passengers.csv",
    mime="text/csv"
)
