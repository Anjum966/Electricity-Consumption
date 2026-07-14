# ⚡ Plugging into the Future: An Exploration of Electricity Consumption Patterns

## 📖 Project Overview

This project analyzes electricity consumption patterns across different states and regions of India using Business Intelligence techniques. The data is stored and managed in MySQL and visualized using Tableau to provide interactive dashboards, charts, maps, and reports. The project helps identify electricity usage trends, compare yearly consumption, and support better energy planning and decision-making.

---

## 🎯 Objectives

- Analyze electricity consumption data.
- Compare electricity usage between 2019 and 2020.
- Identify high and low electricity consuming states.
- Visualize state-wise and region-wise electricity consumption.
- Create interactive dashboards using Tableau.
- Support data-driven decision-making.

---

## 🛠 Technologies Used

- MySQL Workbench
- Tableau Desktop
- Tableau Public
- Microsoft Excel (Dataset)
- Windows Operating System

---

## 📂 Project Structure

```
Electricity-Consumption-Analysis/
│
├── Dataset/
│   └── Electricity_Consumption.csv
│
├── SQL/
│   └── electricity_queries.sql
│
├── Tableau/
│   ├── Electricity_Dashboard.twb
│   ├── Electricity_Dashboard.twbx
│   └── Story.twb
│
├── Screenshots/
│   ├── Dashboard1.png
│   ├── Dashboard2.png
│   ├── Dashboard3.png
│   ├── Dashboard4.png
│   ├── Dashboard5.png
│   └── Dashboard6.png
│
├── Documentation/
│   └── Final_Project_Report.pdf
│
└── README.md
```

---

## 📊 Features

- Interactive Tableau Dashboard
- State-wise Electricity Consumption
- Region-wise Electricity Analysis
- Monthly Consumption Analysis
- Quarterly Consumption Analysis
- Year-wise Comparison
- Top N and Bottom N States
- Interactive Maps
- Tableau Story Presentation

---

## 📈 Dashboard Visualizations

The project includes the following visualizations:

- India State Map (2019)
- India State Map (2020)
- Region-wise Consumption
- Total Electricity Consumption
- Monthly Usage Analysis
- Quarterly Usage Analysis
- Top N States
- Bottom N States
- Year-wise Comparison
- Tableau Story Dashboard

---

## 🗄 Database

The project uses **MySQL** to store and manage electricity consumption data.

### Sample SQL Commands

```sql
CREATE DATABASE electricity;

USE electricity;

SELECT * FROM consumption;

SELECT States, Regions
FROM consumption;

SELECT *
FROM consumption
ORDER BY Dates;
```

---

## 🚀 How to Run the Project

1. Install MySQL Workbench.
2. Create the database.
3. Import the electricity consumption dataset.
4. Execute the SQL queries.
5. Open Tableau Desktop.
6. Connect Tableau to MySQL.
7. Open the Tableau Workbook (.twb/.twbx).
8. Explore the dashboards and stories.

---

## 📌 Results

The project successfully provides:

- Electricity consumption comparison for 2019 and 2020.
- Region-wise electricity analysis.
- State-wise electricity analysis.
- Interactive maps and dashboards.
- Business Intelligence reports for better visualization.

---

## 🎯 Future Scope

- Real-time electricity monitoring.
- IoT-based smart energy management.
- Machine Learning for electricity demand prediction.
- AI-powered anomaly detection.
- Cloud database integration.
- Web-based dashboard deployment.
- Mobile dashboard application.

---

## 👨‍💻 Author

**Project:** Plugging into the Future: An Exploration of Electricity Consumption Patterns

Developed using **MySQL** and **Tableau** for Business Intelligence and Data Visualization.

---

## 📄 License

This project is created for educational and academic purposes.
