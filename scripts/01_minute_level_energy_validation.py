
"""
Step 01: Minute-level energy validation and preparation

- Loads raw residential electricity consumption data
- Constructs datetime index
- Converts Global Active Power (kW) to energy per minute (kWh)
- Exports a clean, validated minute-level dataset for aggregation

Input: house_power_consumption.txt (raw data)
Output: 01_minute_level_energy_validation_summary.csv
"""


import pandas as pd

df=pd.read_csv(
    "data/house_power_consumption.txt",
    sep=";",
    na_values="?",
    low_memory=False
)

df["datetime"]=pd.to_datetime(
    df["Date"]+" "+df["Time"],
    format="%d/%m/%Y %H:%M:%S"
)

df=df.set_index("datetime")
df=df.drop(columns=["Date","Time"])

# Convert Global Active Power (kW) to energy per minute (kWh)
# Dataset is minute-level, so: kW × (1/60 hour)

df["energy_kwh"]=df["Global_active_power"]/60

print(df[["Global_active_power","energy_kwh"]].head())

# Prepare validation output

export_df=df[
[
    "energy_kwh",
    "Sub_metering_1",
    "Sub_metering_2",
    "Sub_metering_3",
]

].copy()

export_df=export_df.reset_index()

export_df.to_csv(

    "outputs/01_minute_level_energy_validation_summary.csv",
    index=False
)

print("CSV exported to outputs/01_minute_level_energy_validation_summary.csv")

