# 🍼 Survival Analysis of Child Mortality (Synthetic Dataset)

This repository contains a **Python-based synthetic dataset generator** designed to simulate child mortality outcomes in **Rural vs Urban areas** of Nigeria.
It was developed for **academic and research purposes**, specifically for survival analysis projects when real-world survey data (e.g., NDHS) is not immediately accessible.

---

## 📖 Project Overview

Child mortality is a critical indicator of population health, influenced by socio-economic and environmental factors.
This synthetic dataset mimics the structure of survey data by including key variables:

* **Survival Variables**

  * `time` → Survival time (in months) until event/censoring
  * `event` → Mortality status (1 = child died, 0 = censored/alive)

* **Demographics & Household Variables**

  * `area` → Rural vs Urban (focus variable for comparison)
  * `sex` → Male/Female
  * `mother_age` → Age of mother at child’s birth
  * `education_level` → Mother’s education (None, Primary, Secondary, Higher)
  * `household_income` → Simulated household economic level
  * `access_healthcare` → Binary indicator of healthcare access
  * `water_source` → Type of water source (Safe/Unsafe)
  * `sanitation` → Sanitation facility (Improved/Unimproved)

---

## 🛠️ Features

* Generates **10,000+ rows of synthetic survey-like data**.
* Captures the contrast between **rural and urban areas**.
* Built using **NumPy** and **Pandas** (lightweight, reproducible).
* Output saved as a clean CSV file for analysis in Python, R, Stata, or SPSS.

---

## 🚀 Usage

### 1. Install Requirements

```bash
pip install numpy pandas
```

### 2. Run Script

```bash
python synthetic_child_mortality.py
```

### 3. Output

* The script generates a file named:

  ```
  synthetic_child_mortality.csv
  ```
* You can open this file in **Excel**, **Python**, **R**, or any statistical package.

---

## 📊 Applications

* Survival analysis (Kaplan–Meier, Cox regression).
* Comparative studies: Rural vs Urban child mortality.
* Teaching & training in biostatistics.
* Academic projects where real NDHS data isn’t readily available.

---

## ⚠️ Disclaimer

This dataset is **synthetic** and should be used **only for educational or methodological purposes**.
For real-world analysis, please use the **Nigeria Demographic and Health Survey (NDHS)** or similar national survey data.

---

## 👨‍💻 Author

Developed by **Uthman Adesola (SUNEXUS)** 🌞

* ✉️ Email: [uthmanrsm@gmail.com](mailto:uthmanrsm@gmail.com)
* 🌐 Blog: [sunexus.blogspot.com]
* 🐦 Twitter/X: [@sir_uthy]

✨ *Illuminating data, innovation, and solutions.*
