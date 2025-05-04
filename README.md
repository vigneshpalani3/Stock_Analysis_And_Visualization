# 📊 Stock Analysis and Visualization

An interactive, data-driven project for analyzing and visualizing **Nifty 50** stock performance using **Python**, **Streamlit**, and **Power BI**.

---

## 🧭 Overview

This project aims to analyze the daily stock performance of the Nifty 50 index. It transforms raw YAML stock data into clean CSV formats and visualizes stock trends through interactive dashboards.

Key objectives:

- Clean and organize stock market data
- Generate CSVs from YAML files
- Build dashboards for insights
- Present historical stock performance in a user-friendly interface

---

## 🛠️ Features

✅ Data extraction from YAML to CSV  
✅ Interactive dashboard using **Streamlit**  
✅ Power BI dashboard for deeper insights  
✅ Sector-wise stock performance analysis  
✅ Organized and modular codebase  

---

## 📁 Project Structure

```
📦 Stock_Analysis_And_Visualization
├── datasets/               # Raw YAML data files
├── csv_files/              # Processed CSV files
├── pages/                  # Additional Streamlit pages
├── stocks_dashboard/       # Power BI dashboard files (.pbix)
├── Sector_data.csv         # Sector-wise metadata
├── home.py                 # Main Streamlit application
├── Stock_analysis.ipynb    # Jupyter notebook for stock insights
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.7+
- pip (Python package manager)

### 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/vigneshpalani3/Stock_Analysis_And_Visualization.git
cd Stock_Analysis_And_Visualization
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv env
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

### ▶️ Run the Streamlit App

```bash
streamlit run home.py
```

This will open the interactive dashboard in your default browser.

---

## 📊 Power BI Dashboard

To explore richer insights:

1. Install **[Power BI Desktop](https://powerbi.microsoft.com/desktop/)**  
2. Open the `.pbix` file inside the `stocks_dashboard/` directory  
3. Navigate through different views to explore sector and stock-level trends

---

## 📓 Data Analysis (Jupyter)

The `Stock_analysis.ipynb` notebook includes:

- Stock trend visualization
- Volatility analysis
- Top performing stocks
- Sector-wise metrics

Use it for exploration or expand it with your own models and visualizations.

---

## 🤝 Contributing

Contributions, feature requests, and feedback are welcome!

Feel free to fork the project, make improvements, and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 📬 Contact

**Author:** [Vignesh Palani](https://github.com/vigneshpalani3)  
📧 For questions, feel free to reach out via GitHub Issues or email.
