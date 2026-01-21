# 🐧 ML-Based Linux Update Stability Engine

A system-level project that collects real Linux update data, stores it in a structured database, and prepares a machine learning pipeline to analyze update stability and risk.

---

## 📌 Problem Statement

Linux system updates—especially on rolling-release distributions—can sometimes introduce instability.
Users often update their systems without knowing whether an update could potentially cause issues.

This project focuses on analyzing historical Linux update behavior and building a pipeline that can classify update risk using machine learning.

---

## 🧠 What This Project Does

1. Reads real Linux update logs from the system  
2. Extracts package and system update information  
3. Stores structured update data in a SQLite database  
4. Builds features required for machine learning  
5. Trains a classification model when enough data exists  

The project uses real system data, not fake or pre-made datasets.

---

## 🏗️ System Architecture

Linux System → Pacman Logs (`/var/log/pacman.log`) → Data Collection Layer → SQLite Database → Feature Engineering → Machine Learning Pipeline

---

## ⚙️ Technologies Used

- Python – core programming language  
- SQLite – structured data storage  
- Pandas & NumPy – data processing  
- Scikit-learn – machine learning  
- Linux (pacman) – real system data source  

---

## 📂 Project Structure

- **src/**
  - **collectors/** – collects update data from Linux logs  
  - **features/** – feature engineering logic  
  - **models/** – machine learning model  
  - **utils/** – logging utilities  
  - **main.py** – pipeline entry point  
- **sql/** – database schema  
- **notebooks/** – exploratory analysis  
- **requirements.txt** – project dependencies  
- **README.md** – project documentation  

---

## ▶️ How to Run the Project

Activate the virtual environment:  
source .venv/bin/activate.fish

Collect real Linux update data:  
python -m src.collectors.pacman

Run the machine learning pipeline:  
python -m src.main

If there is not enough historical update data, the system safely skips ML training instead of failing.

---

## 🤖 Machine Learning Overview

Problem Type: Classification  
Model Used: Random Forest  

Features:
- Number of packages updated  
- Kernel update indicator  

Output:
- Update risk classification (safe / risky)

The ML pipeline is designed to activate automatically when sufficient historical data is available.

---

## 🔍 Key Highlights

- Uses real Linux system update logs  
- End-to-end ML-ready pipeline  
- Handles low-data scenarios safely  
- Modular and explainable design  
- Focused on system-level data engineering  

---

## 🚀 Future Improvements

- Time-series analysis of update history  
- Support for multiple Linux distributions  
- Background monitoring service  
- Improved risk scoring logic  
- Visualization dashboard  

---

## 👤 Author

**Jagadheesan (Jd)**  
GitHub: https://github.com/jxgadheesan  
Interests: Linux, Python, Machine Learning, System-Level Engineering
