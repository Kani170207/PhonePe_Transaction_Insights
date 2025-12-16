PhonePe Transaction Insights

A data analytics and visualization project that analyzes PhonePe transaction data across India and presents interactive insights using **Python, SQL, and Streamlit**.

🔗 **Live App:**  
[https://phonepetransactioninsights-hzkk6fceufhxqrnlrgybtq.streamlit.app/](https://phonepetransactioninsights-hzkk6fceufhxrqnlrgybtq.streamlit.app/)

🔗 **GitHub Repository:**  
https://github.com/Kani170207/PhonePe_Transaction_Insights

---

## 📌 Project Overview

With the rapid growth of digital payments in India, understanding transaction trends is crucial.  
This project explores **PhonePe transaction data** to uncover patterns across **states, years, and categories**, enabling data-driven insights through an interactive dashboard.

---

## 🎯 Objectives

- Analyze PhonePe transaction data across India
- Identify top-performing states and trends over time
- Visualize transaction volume and value using charts and maps
- Build an interactive, user-friendly dashboard

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Database:** SQLite
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Plotly
- **Dashboard:** Streamlit
- **Version Control:** Git & GitHub
- **Deployment:** Streamlit Cloud

---

## 📂 Project Structure

PhonePe_Transaction_Insights/
│
├── dashboard/
│ └── app.py # Streamlit dashboard
│
├── data/
│ ├── aggregated/ # Raw aggregated data
│ ├── map/ # Geo data
│ ├── top/ # Top states/districts data
│ └── phonepe_transaction_insights.db
│
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── notebooks/
└── phonepe_analysis.ipynb

yaml
Copy code

---

## 📊 Dashboard Features

✔ **Key Performance Indicators (KPIs)**
- Total Transactions
- Total Transaction Amount
- Average Transaction Value

✔ **Interactive Visualizations**
- State-wise transaction bar chart
- Year-wise filtering
- India state-level transaction map

✔ **User Controls**
- Year selection dropdown
- Dynamic chart updates

---

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository
git clone https://github.com/Kani170207/PhonePe_Transaction_Insights.git
cd PhonePe_Transaction_Insights
2️⃣ Create Virtual Environment (Optional)
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the Streamlit App
bash
Copy code
streamlit run dashboard/app.py
☁️ Deployment
The application is deployed using Streamlit Cloud and connected directly to the GitHub repository for continuous deployment.

📈 Business Use Cases
Customer Behavior Analysis

Regional Market Insights

Digital Payment Growth Tracking

Data-Driven Decision Making

Product & Marketing Strategy Optimization

🚀 Future Enhancements
District & Pincode level analysis

Time-series trend visualizations

User growth and category-wise insights

Advanced filters and UI enhancements

👤 Author
Kani
Aspiring Data Analyst | Python | SQL | Streamlit
🔗 GitHub: https://github.com/Kani170207
