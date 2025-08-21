# 🏡 Housing Price Prediction

This project is an **end-to-end machine learning pipeline** that predicts housing prices using regression models.  
It demonstrates data preprocessing, model training, model comparison, saving, and verification — making it suitable for real-world deployment.

---

## 📊 Project Overview
The goal of this project is to build a model that can accurately predict housing prices based on features such as location, size, and furnishing status.  
We compare **Linear Regression, Random Forest, and Gradient Boosting**, and select the best model based on performance metrics.

---

## ⚙️ Workflow
1. **Data Loading & Cleaning**
   - Load dataset (`Housing (4).csv`)
   - Handle missing values and duplicates
   - Clean numeric columns (remove currency symbols, commas, etc.)

2. **Exploratory Data Analysis (EDA)**
   - Distribution plots of housing prices
   - Correlation heatmap
   - Boxplots for categorical vs numeric features

3. **Preprocessing**
   - Encode categorical features (OneHotEncoder)
   - Scale numeric features (StandardScaler)
   - Train-test split

4. **Model Training & Comparison**
   - Linear Regression
   - Random Forest Regressor
   - Gradient Boosting Regressor
   - Evaluation with RMSE, MAE, and R² score

5. **Best Model Selection**
   - Select best model (lowest RMSE, highest R²)
   - Save as `housing_model.pkl` (includes preprocessing + model)

6. **Verification**
   - Reload model
   - Predict housing price on a sample input
   - Compare predicted vs actual value

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Joblib (for saving model)

---

## 📈 Results
- Compared three models: **Linear Regression, Random Forest, Gradient Boosting**
- Random Forest/Gradient Boosting typically performed best (lowest RMSE, higher R²)
- Final model saved as `housing_model.pkl`

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/ajay-hum/housing-price-prediction.git
   cd housing-price-prediction
2. Install requirements:  
   `pip install -r requirements.txt`
3. Run app:  
   `python app.py`

---

## 👨‍💻 Author
**Justus Asogwa**  
📧 [justuschimeremueze@gmail.com](mailto:justuschimeremueze@gmail.com)  
🌐 [LinkedIn](https://www.linkedin.com/in/justus-asogwa-726427293)  
💻 [GitHub](https://github.com/Ajay-hum)
