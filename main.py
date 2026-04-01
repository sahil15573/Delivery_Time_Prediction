import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load Model & Encoders
# -------------------------------
model = pickle.load(open("best_random_forest_model.pkl", "rb"))
label_encoders = pickle.load(open("all_label_encoders.pkl", "rb"))

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Food Delivery Time Predictor",
    page_icon="🍔",
    layout="centered"
)

# -------------------------------
# Title & Description
# -------------------------------
st.title("🍔 Food Delivery Time Predictor")
st.markdown("Predict how long your food delivery will take based on real-world conditions.")

st.divider()

# -------------------------------
# User Inputs
# -------------------------------
st.subheader("📋 Enter Delivery Details")

distance = st.number_input("Distance (km)", min_value=0.0, step=0.1)

weather = st.selectbox("Weather", label_encoders['Weather'].classes_)

traffic = st.selectbox("Traffic Level", label_encoders['Traffic_Level'].classes_)

time_of_day = st.selectbox("Time of Day", label_encoders['Time_of_Day'].classes_)

prep_time = st.number_input("Preparation Time (minutes)", min_value=0, step=1)

# NOTE: Delivery_Time_min should NOT be an input (it's your target)
# If your model was trained including it (which is wrong), we will handle it safely

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("🚀 Predict Delivery Time"):

    try:
        # Encode categorical values
        weather_encoded = label_encoders['Weather'].transform([weather])[0]
        traffic_encoded = label_encoders['Traffic_Level'].transform([traffic])[0]
        time_encoded = label_encoders['Time_of_Day'].transform([time_of_day])[0]

        # Create input dataframe
        input_data = pd.DataFrame({
            'Distance_km': [distance],
            'Weather': [weather_encoded],
            'Traffic_Level': [traffic_encoded],
            'Time_of_Day': [time_encoded],
            'Preparation_Time_min': [prep_time]
        })

        # Prediction
        prediction = model.predict(input_data)[0]

        # -------------------------------
        # Output
        # -------------------------------
        st.success(f"⏱ Estimated Delivery Time: **{round(prediction, 2)} minutes**")

    except Exception as e:
        st.error(f"Error: {e}")

# -------------------------------
# Footer
# -------------------------------
st.divider()
st.caption("Built with ❤️ using Streamlit & Machine Learning")