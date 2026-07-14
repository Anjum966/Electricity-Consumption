import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="EnergyPulse Analytics", layout="wide", page_icon="⚡")

st.title("⚡ Plugging into the Future")
st.subheader("An Exploration of Smart Meter Electricity Consumption Patterns")

if not os.path.exists("household_energy_data.csv"):
    st.info("Historical data file not found. Generating a fresh 1-year smart meter simulation dataset...")
    import generate_data
    generate_data.generate_mock_energy_data()

@st.cache_data
def load_data():
    df = pd.read_csv("household_energy_data.csv", parse_dates=[0], index_col=0)
    return df

df = load_data()

st.sidebar.header("Dashboard Controls")
view_mode = st.sidebar.selectbox("Analysis View", ["Historical Trends", "What-If Optimization Sandbox"])
selected_month = st.sidebar.slider("Filter Analysis by Month", 1, 12, 7)

month_names = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
month_df = df[df['Month'] == selected_month]

if view_mode == "Historical Trends":
    st.markdown(f"### Historical Consumption Analysis: **{month_names[selected_month]}**")
    
    total_kwh = month_df['Consumption_kWh'].sum()
    avg_daily_kwh = total_kwh / len(month_df.index.normalize().unique())
    est_cost = total_kwh * 0.16
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Monthly Consumption", f"{total_kwh:,.1f} kWh")
    m2.metric("Average Daily Footprint", f"{avg_daily_kwh:.2f} kWh/day")
    m3.metric("Estimated Cost (@ $0.16/kWh)", f"${est_cost:,.2f}")
    
    st.markdown("---")
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("#### Typical 24-Hour Load Curve")
        hourly_profile = month_df.groupby('Hour')[['HVAC_kWh', 'Lighting_Entertainment_kWh', 'Always_On_kWh']].sum()
        days_in_sub = len(month_df.index.normalize().unique())
        hourly_profile = (hourly_profile / days_in_sub) * 4
        
        fig_hourly = px.line(hourly_profile, labels={"value": "Average Demand (kW)", "Hour": "Hour of Day"})
        fig_hourly.update_layout(legend_title_text="Load Category", hovermode="x unified")
        st.plotly_chart(fig_hourly, use_container_width=True)
        
    with c2:
        st.markdown("#### Consumption Share by Category")
        shares = [month_df['HVAC_kWh'].sum(), month_df['Lighting_Entertainment_kWh'].sum(), month_df['Always_On_kWh'].sum()]
        labels = ['HVAC (Climate Control)', 'Lighting & Appliances', 'Always On / Standby']
        fig_pie = px.pie(values=shares, names=labels, hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)

else:
    st.markdown("### 🛠️ Demand-Side Management Sandbox")
    st.write("Simulate how retrofitting appliance efficiencies or shifting usage profiles impacts peak curves and power bills.")
    
    col_sb1, col_sb2 = st.columns(2)
    with col_sb1:
        hvac_upgrade = st.slider("Improve HVAC System Efficiency (%)", 0, 50, 20)
        peak_shift = st.slider("Percentage of Evening Peak Usage shifted to Off-Peak Hours", 0, 100, 30)
    with col_sb2:
        base_rate = st.number_input("Standard/Off-Peak Power Cost ($/kWh)", value=0.12)
        peak_rate = st.number_input("Peak Penalty Cost ($/kWh) [5 PM - 10 PM]", value=0.32)

    sandbox_df = month_df.copy()
    efficiency_factor = 1 - (hvac_upgrade / 100.0)
    
    profile = sandbox_df.groupby('Hour')[['HVAC_kWh', 'Lighting_Entertainment_kWh', 'Always_On_kWh']].mean()
    profile['Mod_HVAC'] = profile['HVAC_kWh'] * efficiency_factor
    profile['Mod_Other'] = profile['Lighting_Entertainment_kWh']
    
    peak_hours = [17, 18, 19, 20, 21]
    off_peak_hours = [0, 1, 2, 3, 4, 5, 22, 23]
    
    shifted_energy = 0
    for ph in peak_hours:
        amt = profile.loc[ph, 'Mod_Other'] * (peak_shift / 100.0)
        shifted_energy += amt
        profile.loc[ph, 'Mod_Other'] -= amt
        
    allocated_per_hour = shifted_energy / len(off_peak_hours)
    for oph in off_peak_hours:
        profile.loc[oph, 'Mod_Other'] += allocated_per_hour
        
    profile['Baseline_Total_kW'] = (profile['HVAC_kWh'] + profile['Lighting_Entertainment_kWh'] + profile['Always_On_kWh']) * 4
    profile['Optimized_Total_kW'] = (profile['Mod_HVAC'] + profile['Mod_Other'] + profile['Always_On_kWh']) * 4
    
    fig_comp = go.Figure()
    fig_comp.add_trace(go.Scatter(x=profile.index, y=profile['Baseline_Total_kW'], name='Original Load Curve', line=dict(color='firebrick', width=3, dash='dot')))
    fig_comp.add_trace(go.Scatter(x=profile.index, y=profile['Optimized_Total_kW'], name='Optimized Sandbox Curve', line=dict(color='green', width=4)))
    
    fig_comp.update_layout(title="Flattening the Duck Curve: Demand Modulation Impact", xaxis_title="Hour of Day", yaxis_title="Power Demand (kW)")
    st.plotly_chart(fig_comp, use_container_width=True)
    
    orig_total_kwh = month_df['Consumption_kWh'].sum()
    days_count = len(month_df.index.normalize().unique())
    mod_total_kwh = (profile['Mod_HVAC'].sum() + profile['Mod_Other'].sum() + profile['Always_On_kWh'].sum()) * days_count
    
    c_m1, c_m2 = st.columns(2)
    c_m1.metric("Original Monthly Total", f"{orig_total_kwh:,.1f} kWh")
    c_m2.metric("Optimized Sandbox Total", f"{mod_total_kwh:,.1f} kWh", delta=f"{mod_total_kwh - orig_total_kwh:,.1f} kWh")
