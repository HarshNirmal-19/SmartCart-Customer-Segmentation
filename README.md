# SmartCart Customer Segmentation


# LIVE DEMO : Open SmartCart Customer Segmentation App

 link:  https://smartcart-customer-segmentation-app.streamlit.app/



## 📌 Project Overview

SmartCart Customer Segmentation is an unsupervised machine learning project developed to identify meaningful groups of customers based on their demographic characteristics, purchasing behaviour, website activity, and customer engagement.

The project uses **KMeans Clustering** to segment customers into different groups with similar characteristics.

A **Streamlit web application** was also developed to allow users to enter customer details and predict the customer's segment using the trained machine learning model. The application also provides a business recommendation based on the predicted segment.

---

## 🎯 Problem Statement

SmartCart is an e-commerce platform that has collected customer data containing demographic information, purchase behaviour, website activity, and customer response information.

Using the same marketing and engagement strategy for every customer can result in inefficient marketing, missed opportunities to retain high-value customers, and difficulty understanding different customer behaviour patterns.

To address this problem, an intelligent customer segmentation system is developed using **unsupervised machine learning** to discover groups of customers with similar characteristics and support data-driven marketing decisions.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze customer demographic and purchasing behaviour.
- Clean and preprocess the customer dataset.
- Handle missing values and outliers.
- Perform feature engineering to create meaningful customer features.
- Convert categorical variables into numerical features.
- Standardize the features before clustering.
- Apply Principal Component Analysis (PCA) for dimensionality reduction.
- Determine the appropriate number of customer clusters.
- Perform customer segmentation using KMeans clustering.
- Analyze and interpret the characteristics of each customer segment.
- Develop a Streamlit application for customer segment prediction.
- Provide a recommended business action for each customer segment.

---

## 📊 Dataset

The original dataset contains **2,240 customer records and 22 attributes** describing customer demographics, purchase behaviour, website activity, and customer response.

Each row represents an individual customer.

### Customer Demographics

 Feature -- Description 

 `ID` -- Unique customer identifier 
 `Year_Birth` -- Year of birth of the customer 
 `Education` -- Highest education level achieved 
 `Marital_Status` -- Marital status of the customer 
 `Income` -- Yearly household income 
 `Kidhome` -- Number of small children in the household 
 `Teenhome` -- Number of teenagers in the household 
 `Dt_Customer` -- Date when the customer enrolled 

### Purchase Behaviour — Amount Spent

 Feature -- Description 

 `MntWines` -- Amount spent on wine products 
 `MntFruits` -- Amount spent on fruit products 
 `MntMeatProducts` -- Amount spent on meat products 
 `MntFishProducts` -- Amount spent on fish products 
 `MntSweetProducts` -- Amount spent on sweet products 
 `MntGoldProds` -- Amount spent on gold products 

### Purchase Behaviour — Frequency
 Feature -- Description 

 `NumDealsPurchases` -- Purchases made using discounts 
 `NumWebPurchases` -- Purchases made through the website 
 `NumCatalogPurchases` -- Purchases made through the catalog 
 `NumStorePurchases` -- Purchases made through physical stores 
 `NumWebVisitsMonth` --- Number of website visits per month 

### Customer Feedback and Activity

 Feature -- Description 

 `Recency` -- Number of days since the last purchase 
 `Complain` -- Whether the customer complained 
 `Response` -- Customer response to the marketing campaign 

---

## 🧹 Data Preprocessing

Several preprocessing and feature engineering steps were performed before applying the clustering algorithm.

### 1. Handling Missing Values

Missing values in the `Income` feature were handled using the **median value**.

### 2. Feature Engineering

The following meaningful features were created:

- `Age`
- `Customer_Tenure_Days`
- `Total_Spending`
- `Total_Children`

### 3. Feature Transformation

The following transformations were performed:

- Education categories were simplified.
- Marital status was transformed into a `Living_With` feature.
- Original features that were no longer required after feature engineering were removed.

### 4. Outlier Handling

Outliers were handled using appropriate threshold-based filtering, particularly for features such as:

- `Age`
- `Income`

### 5. Categorical Encoding

Categorical variables were converted into numerical features using **One-Hot Encoding**.

After preprocessing and feature engineering, the final dataset used for modelling contained **18 features**.

---

## ⚖️ Feature Scaling

The final features have different numerical ranges.

Therefore, **StandardScaler** from Scikit-learn was used to standardize the features before applying PCA and clustering.

---

## 📉 Principal Component Analysis (PCA)

After feature scaling, **Principal Component Analysis (PCA)** was applied for dimensionality reduction.

The final PCA model uses:
Number of Components = 3
The three principal components were then used as the input features for the KMeans clustering model.

## 🔢 Selecting the Number of Clusters

The appropriate number of clusters was determined using two techniques:

Elbow Method

The Elbow Method was used to analyze the relationship between the number of clusters and within-cluster variation.

Silhouette Method

The Silhouette Method was used to evaluate how well-separated the resulting clusters were.

Based on these methods, the selected number of clusters was: K = 4

## 🤖 KMeans Clustering

The final customer segmentation model was built using KMeans Clustering with four clusters.

The overall machine learning workflow is:
Customer Dataset
       ↓
Data Cleaning
       ↓
Feature Engineering
       ↓
Categorical Encoding
       ↓
Feature Scaling
       ↓
PCA
       ↓
KMeans Clustering
       ↓
Customer Segments

The trained model and preprocessing objects were saved using joblib.

Saved artifacts:

kmeans_model.pkl
scaler.pkl
pca.pkl

## 👥 Customer Segments

The KMeans clustering analysis resulted in four customer segments.

| Cluster | Customer Segment                   |
| ------- | ---------------------------------- |
|       0 | Low-Value Partnered Customers      |
|       1 | High-Value Multi-Channel Customers |
|       2 | Premium High-Value Customers       |
|       3 | Low-Value Solo Customers           |

🟢 Cluster 0 — Low-Value Partnered Customers

Customers in this segment generally show relatively low spending and lower purchasing activity.

They can be targeted with discounts and engagement campaigns to encourage additional purchases.

🔵 Cluster 1 — High-Value Multi-Channel Customers

Customers in this segment demonstrate relatively strong purchasing activity across web, catalog, and store channels.

Personalized offers across multiple channels can be used to maintain engagement and encourage repeat purchases.

🟣 Cluster 2 — Premium High-Value Customers

This segment represents the highest-value customer group based on characteristics such as income and spending.

Premium offers, loyalty rewards, and personalized campaigns can be used to retain these customers.

🟠 Cluster 3 — Low-Value Solo Customers

Customers in this segment generally show lower spending and purchasing activity and are characterized by living alone.

Targeted promotions and personalized product recommendations can be used to encourage more purchases.


## 💼 Business Recommendations

The Streamlit application provides a recommended business action based on the predicted customer segment.

| Customer Segment                   | Recommended Action                                                     |
| ---------------------------------- | ---------------------------------------------------------------------- |
| Low-Value Partnered Customers      | Focus on targeted discounts and engagement campaigns                   |
| High-Value Multi-Channel Customers | Use personalized offers across web, catalog, and store channels        |
| Premium High-Value Customers       | Prioritize premium offers, loyalty rewards, and personalized campaigns |
| Low-Value Solo Customers           | Use targeted promotions and personalized recommendations               |

## 🌐 Streamlit Application
A Streamlit web application was developed to make the customer segmentation model interactive.
The application allows users to enter customer information such as:
Age
Income
Customer tenure
Number of children
Total spending
Deal purchases
Web purchases
Catalog purchases
Store purchases
Monthly website visits
Recency
Customer complaints
Campaign response
Education
Living arrangement

The entered customer information is transformed into the same feature structure used during model training.

Prediction Workflow:
User Input
    ↓
Feature Preparation
    ↓
StandardScaler
    ↓
PCA Transformation
    ↓
KMeans Prediction
    ↓
Customer Segment
    ↓
Business Recommendation

## 📁 Project Structure

SmartCart-Customer-Segmentation/
│
├── kmeans_model.pkl
├── pca.pkl
├── scaler.pkl
│
├── segmentation.py
├── smartcart_customers.csv
├── SmartCart_model.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore

## File Description
File  --	Description
SmartCart_model.ipynb --> Complete machine learning workflow including data analysis, preprocessing, feature engineering, PCA, and clustering
segmentation.py	 --> Streamlit application for customer segment prediction
smartcart_customers.csv	  --> Customer dataset used for the project
kmeans_model.pkl -->   Trained KMeans clustering model
scaler.pkl	-->  Fitted StandardScaler
pca.pkl	-->   Fitted PCA transformation
requirements.txt -->	Python dependencies required to run the application
.gitignore	-->  Files and folders excluded from Git tracking
README.md	-->  Project documentation

# 🛠️ Technologies Used
--Programming Language
  Python
--Libraries
  Pandas
  NumPy
  Scikit-learn
  Matplotlib
  Seaborn
  Joblib
  Streamlit
  Kneed
--Machine Learning Techniques
  Data Cleaning
  Feature Engineering
  One-Hot Encoding
  Standardization
  Principal Component Analysis (PCA)
  KMeans Clustering
  Elbow Method
  Silhouette Method
  Agglomerative Clustering for comparison

# ⚙️ Installation

1. Clone the Repository 
git clone <YOUR_GITHUB_REPOSITORY_URL>

2. Navigate to the Project Directory 
cd SmartCart-Customer-Segmentation

3. Install Dependencies
pip install -r requirements.txt

# ▶️ Run the Streamlit Application

Run the following command:
python -m streamlit run segmentation.py  ---> The Streamlit application will open in your web browser.

# 💾 Model Artifacts
The Streamlit application uses three saved machine learning artifacts:
kmeans_model.pkl
scaler.pkl
pca.pkl

These files allow the application to use the already-trained model and preprocessing transformations without retraining the model every time the application starts.

