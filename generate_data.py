import pandas as pd
import numpy as np
from datetime import datetime

def generate_mock_energy_data():
    print("Generating 15-minute interval smart meter data...")
    start_date = datetime(2026, 1, 1)
    end_date = datetime(2026, 12, 31, 23, 45)
    
    time_index = pd.date_range(start=start_date, end=end_date, freq='15min')
    df = pd.DataFrame(index=time_index)
    
    df['Hour'] = df.index.hour
    df['Month'] = df.index.month
    df['DayOfWeek'] = df.index.dayofweek
    
    base_load = 0.2  # kW
    tod_profile = np.zeros(24)
    tod_profile[7:10] = 0.6
    tod_profile[17:23] = 1.2
    
    seasonal_profile = {1: 1.4, 2: 1.2, 3: 0.9, 4: 0.8, 5: 1.1, 6: 1.5, 7: 1.8, 8: 1.7, 9: 1.2, 10: 0.8, 11: 1.0, 12: 1.3}
    
    consumption = []
    for dt in df.index:
        hour = dt.hour
        month = dt.month
        is_weekend = dt.dayofweek >= 5
        
        load = base_load + tod_profile[hour]
        load *= seasonal_profile[month]
        
        if is_weekend:
            load *= 1.15
            
        load += np.random.normal(0, 0.1)
        load = max(0.05, load)
        
        kwh = load * 0.25
        consumption.append(kwh)
        
    df['Consumption_kWh'] = consumption
    df['HVAC_kWh'] = df['Consumption_kWh'] * df['Month'].map({1:0.5, 2:0.4, 3:0.1, 4:0.1, 5:0.4, 6:0.6, 7:0.65, 8:0.6, 9:0.4, 10:0.1, 11:0.2, 12:0.4})
    df['Lighting_Entertainment_kWh'] = df['Consumption_kWh'] * 0.25
    df['Always_On_kWh'] = df['Consumption_kWh'] - df['HVAC_kWh'] - df['Lighting_Entertainment_kWh']
    df['Always_On_kWh'] = df['Always_On_kWh'].clip(lower=0.01)
    
    df.to_csv("household_energy_data.csv")
    print("Dataset saved successfully as 'household_energy_data.csv'!")

if __name__ == "__main__":
    generate_mock_energy_data()
