"""
Step 02: Hourly energy aggregation and data quality handling

- Loads validated minute-level energy data
- Converts sub-metering values from Wh to kWh
- Aggregates energy consumption to hourly totals
- Identifies hours with zero consumption across all meters
- Marks likely data gaps as NA
- Exports a clean hourly dataset for analysis and reporting

Input: 01_minute_level_energy_validation_summary.csv
Output: 02_hourly_energy_consumption_clean.csv
"""


import pandas as pd

# Load minute level validated energy data (output from step 01)

clean_file=pd.read_csv(

    "outputs/01_minute_level_energy_validation_summary.csv",
    na_values=["?","NA","N/A"]
)

clean_file["datetime"]=pd.to_datetime(clean_file["datetime"])

# Convert sub metering values from wh to kwh

clean_file["Sub_metering_kwh_1"]=clean_file["Sub_metering_1"]/1000
clean_file["Sub_metering_kwh_2"]=clean_file["Sub_metering_2"]/1000
clean_file["Sub_metering_kwh_3"]=clean_file["Sub_metering_3"]/1000

clean_file=clean_file.set_index("datetime")

energy_minute_df=clean_file[
    [
        "energy_kwh",
        "Sub_metering_kwh_1",
        "Sub_metering_kwh_2",
        "Sub_metering_kwh_3"
    ]
]

# Aggregate minute level energy data into hourly totals

energy_hourly_df=energy_minute_df.resample("h").sum()

# Identify hours where all energy readings are zero (Likely data gaps)

all_zero_rows=(
    (energy_hourly_df[
        ["energy_kwh","Sub_metering_kwh_1","Sub_metering_kwh_2","Sub_metering_kwh_3"]
    ]==0).all(axis=1)
)

print("no of rows where all columns are zero:")
print(all_zero_rows.sum())

print("number of zeroes in each column (hourly):")
zero_counts_per_column=(energy_hourly_df==0).sum()
print(zero_counts_per_column)

# Set fully zero hours to NA to avoid misrepresenting consumption

energy_hourly_df.loc[
    all_zero_rows,
    ["energy_kwh","Sub_metering_kwh_1","Sub_metering_kwh_2","Sub_metering_kwh_3",]
]=pd.NA

print(energy_hourly_df.isna().sum())

energy_hourly_df.to_csv(
    "outputs/02_hourly_energy_consumption_clean.csv"
)

print("Saved:02_hourly_energy_consumption_clean.csv")