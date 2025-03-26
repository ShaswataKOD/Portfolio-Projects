# 🚀 Industrial Machine Anomaly Detection

## 📌 Project Overview
This project focuses on detecting **anomalies in industrial machines** using **unsupervised machine learning models**. By analyzing sensor data (e.g., temperature, pressure, vibration, and humidity), we identify unusual behavior that may indicate potential machine failures.

✅ **Key Goal:** Predict and detect machine failures **before they occur** to reduce downtime and maintenance costs.

## 🔍 Problem Statement
Industrial machines generate vast amounts of sensor data. Manually monitoring this data is inefficient, and **failures can lead to costly repairs and production losses**. This project automates anomaly detection using **Isolation Forest** and **Local Outlier Factor (LOF)** to identify abnormal patterns.

## 🎯 Features
- **Unsupervised Learning:** No need for labeled failure data.
- **Real-time Anomaly Detection:** Detects potential failures early.
- **Scalable Approach:** Works on large datasets efficiently.
- **Visualization:** Graphical representation of anomalies for better insights.

---

## 🛠 Tech Stack
- **Programming Language:** Python 🐍
- **Libraries:** Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning Models:**
  - Isolation Forest 🌲
  - Local Outlier Factor (LOF) 🔍

---

## 📂 Dataset
The dataset contains machine sensor readings with the following features:
- **Temperature (°C)** 🌡️
- **Pressure (Pa)** 🏭
- **Vibration (Hz)** 🔧
- **Humidity (%)** 💦

We preprocess the dataset using **MinMax Scaling** to normalize the values before feeding them into the models.

---

## 📊 Model Implementation
### 1️⃣ **Data Preprocessing**
- Load and clean the dataset
- Normalize sensor data using **MinMaxScaler**
- Convert it into a structured format

### 2️⃣ **Anomaly Detection Models**
#### 🔹 **Isolation Forest (IF)**
- Works by randomly partitioning data and isolating anomalies
- Anomalies are detected when they require fewer splits

#### 🔹 **Local Outlier Factor (LOF)**
- Identifies anomalies based on the density of data points
- Anomalies have significantly lower densities than normal points

### 3️⃣ **Evaluating Results**
- Compare models using **Precision-Recall Curve** 📈
- Identify the most effective model for anomaly detection
- Visualize anomalies using **scatter plots & histograms**

---

## 🚀 Running the Project
### 🛠 Installation
Ensure you have Python installed and run the following:
```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

### ▶️ Run the Code
```python
python anomaly_detection.py
```

---

## 📈 Results & Insights
✅ **Detected potential failures early** based on unusual sensor readings.  
✅ **Reduced false positives** using optimized model parameters.  
✅ **Provided interpretable visualizations** for engineers to analyze machine behavior.

---

## 🤝 Future Enhancements
🔹 Integrate **real-time streaming data** 📡 for real-time anomaly detection.  
🔹 Implement **Hybrid Model** combining IF & LOF for better accuracy.  
🔹 Deploy as a **Web App** using Flask or FastAPI.  

---

## 📢 Conclusion
This project provides an effective **predictive maintenance solution** using machine learning. It can be applied in **manufacturing, aerospace, and other industries** where machine failures must be minimized.

🚀 **Want to contribute?** Feel free to fork the repository and improve the models! 🎯

---

📧 **Contact:** If you have any questions, feel free to reach out!


