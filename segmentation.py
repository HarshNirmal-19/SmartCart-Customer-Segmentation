import streamlit as st 
import pandas as pd
import numpy as np 
import joblib 

kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")
pca = joblib.load("pca.pkl")

st.title("SmartCart Customer Segmentation App")
st.write( "Analyze customer behavior and predict the most relevant customer segment,  "
 "using a machine learning-based KMeans clustering model.")

# Customer Information

st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("Age", min_value=18, max_value=100, value=35)

with col2:
    Income = st.number_input("Income", min_value=0, value=50000)

col3, col4 = st.columns(2)

with col3:
    Customer_Tenure_Days = st.number_input(
        "Customer Tenure (Days)",
        min_value=0,
        value=365
    )

with col4:
    Total_Children = st.number_input(
        "Total Children",
        min_value=0,
        max_value=10,
        value=1
    )

# Purchase Behaviour

st.header("Purchase Behavior")

col1, col2 = st.columns(2)

with col1:
    Total_Spending = st.number_input(
        "Total Spending",
        min_value=0,
        value=500
    )

with col2:
    NumDealsPurchases = st.number_input(
        "Number of Deals Purchases",
        min_value=0,
        value=2
    )

col3, col4 = st.columns(2)

with col3:
    NumWebPurchases = st.number_input(
        "Number of Web Purchases",
        min_value=0,
        value=5
    )

with col4:
    NumCatalogPurchases = st.number_input(
        "Number of Catalog Purchases",
        min_value=0,
        value=3
    )

col5, col6 = st.columns(2)

with col5:
    NumStorePurchases = st.number_input(
        "Number of Store Purchases",
        min_value=0,
        value=5
    )

# Online Behavior 

st.header("Online Behavior")

col1, col2 = st.columns(2)

with col1:
    NumWebVisitsMonth = st.number_input(
        "Web Visits per Month",
        min_value=0,
        value=5
    )

with col2:
    Recency = st.number_input(
        "Recency (Days Since Last Purchase)",
        min_value=0,
        value=30
    )

# Customer Interaction

st.header("Customer Interaction")

col1, col2 = st.columns(2)

with col1:
    Complain = st.selectbox(
        "Has the customer complained?",
        ["No", "Yes"]
    )

with col2:
    Response = st.selectbox(
        "Did the customer respond to the campaign?",
        ["No", "Yes"]
    )

# Demographic Information

st.header("Demographic Information")

col1, col2 = st.columns(2)

with col1:
    Education = st.selectbox(
        "Education",
        ["Graduate", "Postgraduate", "Undergraduate"]
    )

with col2:
    Living_With = st.selectbox(
        "Living With",
        ["Alone", "Partner"]
    )

# convert yes/no into 1/0
Complain_value = 1 if Complain == "Yes" else 0
Response_value = 1 if Response == "Yes" else 0

# Convert Education into the 3 one-hot columns
Education_Graduate = 1 if Education == "Graduate" else 0
Education_Postgraduate = 1 if Education == "Postgraduate" else 0
Education_Undergraduate = 1 if Education == "Undergraduate" else 0

# Convert Living_With into the 2 one-hot columns
Living_With_Alone = 1 if Living_With == "Alone" else 0
Living_With_Partner = 1 if Living_With == "Partner" else 0


#  input DataFrame 

input_data = pd.DataFrame([{
    "Income": Income,
    "Recency": Recency,
    "NumDealsPurchases": NumDealsPurchases,
    "NumWebPurchases": NumWebPurchases,
    "NumCatalogPurchases": NumCatalogPurchases,
    "NumStorePurchases": NumStorePurchases,
    "NumWebVisitsMonth": NumWebVisitsMonth,
    "Complain": Complain_value,
    "Response": Response_value,
    "Age": Age,
    "Customer_Tenure_Days": Customer_Tenure_Days,
    "Total_Spending": Total_Spending,
    "Total_Children": Total_Children,
    "Education_Graduate": Education_Graduate,
    "Education_Postgraduate": Education_Postgraduate,
    "Education_Undergraduate": Education_Undergraduate,
    "Living_With_Alone": Living_With_Alone,
    "Living_With_Partner": Living_With_Partner
}])


# Prediction button

if st.button("Predict Segment"):

    input_scaled = scaler.transform(input_data)

    input_pca = pca.transform(input_scaled)

    cluster = kmeans.predict(input_pca)[0]

    cluster_names = {
        0: "Low-Value Partnered Customers",
        1: "High-Value Multi-Channel Customers",
        2: "Premium High-Value Customers",
        3: "Low-Value Solo Customers"
    }

    segment_name = cluster_names[cluster]

    recommendations = {
        0: "Focus on targeted discounts and engagement campaigns to encourage more purchases.",
        1: "Use personalized offers across web, catalog, and store channels to maintain engagement.",
        2: "Prioritize premium offers, loyalty rewards, and personalized campaigns to retain this high-value customer.",
        3: "Use targeted promotions and personalized recommendations to convert browsing activity into purchases."
    }

    st.subheader("Prediction Result")

    st.success(f"Customer Segment: {segment_name}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Cluster", cluster)

    with col2:
        st.write("Recommended Business Action : ")
        st.info(recommendations[cluster])