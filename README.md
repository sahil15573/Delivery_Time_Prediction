# 🍔 Food Delivery Time Prediction

A Machine Learning project that predicts food delivery time based on real-world factors like distance, weather, traffic, and preparation time. The project includes a fully interactive Streamlit web app for real-time predictions.

---

## 🌐 Live Demo

👉 https://sahil15573-delivery-time-prediction-main-pevgtk.streamlit.app/

---

## 📌 Business Problem

Accurate delivery time estimation is critical for food delivery platforms to enhance customer satisfaction and optimize logistics. Delays or incorrect estimates can lead to poor user experience and operational inefficiencies.

This project aims to:

* Predict delivery time using real-world conditions
* Improve estimation accuracy for better customer experience
* Understand key factors affecting delivery delays
* Build a scalable ML-based prediction system

---

## 📊 Dataset

* Dataset: **Food_Delivery_Times.csv**
* Contains features related to:

  * Distance
  * Weather conditions
  * Traffic levels
  * Time of day
  * Preparation time

---

## 🛠️ Data Preprocessing

* Handled missing and inconsistent values
* Encoded categorical variables using **Label Encoding**
* Feature selection based on correlation and domain understanding
* Removed irrelevant or low-impact features
* Train-test split performed for model evaluation

---

## 📈 Exploratory Data Analysis (EDA)

### Key Insights:

* 📏 **Distance vs Delivery Time** → Strong positive relationship
* 🚦 **Traffic Level** significantly increases delivery time
* 🌦️ **Weather conditions** (Rainy/Stormy) lead to delays
* ⏱️ **Preparation Time** directly impacts final delivery time

---

## 🧠 Model Development

### Algorithms Tested:

* Decision Tree Regressor
* Random Forest Regressor (Final Model)

### Final Model:

* **Random Forest Regressor**
* Selected based on better performance and generalization

---

## 📊 Model Performance

| Model         | Accuracy |
| ------------- | -------- |
| Decision Tree | ~0.51    |
| Random Forest | ~0.78    |

👉 Random Forest showed significantly better performance and stability.

---

## 🔍 Features Used

| Feature              | Description                                       |
| -------------------- | ------------------------------------------------- |
| Distance_km          | Distance between restaurant and delivery location |
| Weather              | Weather conditions (Sunny, Rainy, etc.)           |
| Traffic_Level        | Traffic intensity (Low, Medium, High)             |
| Time_of_Day          | Morning, Afternoon, Evening, Night                |
| Preparation_Time_min | Time taken to prepare the food                    |

---

## ⚙️ Model Pipeline

1. User inputs delivery details via UI
2. Categorical features encoded using saved label encoders
3. Data passed to trained Random Forest model
4. Model predicts delivery time
5. Result displayed instantly

---

## 💻 Streamlit Application

* Interactive UI for user input
* Real-time prediction
* Clean and user-friendly interface
* Deployed on Streamlit Cloud

---

## 📁 Project Structure

```
food_delivery_time_prediction/
│
├── main.py                          # Streamlit UI
├── best_random_forest_model.pkl     # Trained ML model
├── all_label_encoders.pkl           # Encoders
├── RF_project_model.ipynb           # Training notebook
├── requirements.txt                 # Dependencies
├── README.md                        # Documentation
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/sahil15573/Delivery_Time_Prediction.git
cd Delivery_Time_Prediction
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the app

```
streamlit run main.py
```

---

## 📊 Key Insights & Findings

* Delivery time is highly influenced by **distance and traffic conditions**
* Weather has a noticeable but moderate impact
* Preparation time is a strong contributing factor
* Random Forest effectively captures non-linear relationships

---

## 🚀 Future Improvements

* Add real-time GPS/map integration 📍
* Use advanced models (XGBoost, LightGBM)
* Hyperparameter tuning for better accuracy
* Add feature importance visualization
* Deploy using Docker

---

## ⚠️ Note

* Model retrained to ensure compatibility with latest scikit-learn version
* `.pkl` files are required for running the app

---

## 👨‍💻 Author

**Sahil Kumar**

📧 Email: [sahilkr.15573@gmail.com](mailto:sahilkr.15573@gmail.com)
🔗 LinkedIn: https://www.linkedin.com/in/sahil-kumar-a945191a6/
💻 GitHub: https://github.com/sahil15573

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
