# Forest Fire Weather Index (FWI) Prediction System

This project is an end-to-end Machine Learning web application that predicts the **Fire Weather Index (FWI)** using meteorological and fire-related parameters. The system uses a trained regression model deployed with a Flask backend and a simple web interface for user interaction.

The application allows users to input environmental conditions and instantly receive a predicted fire weather index value.

---

##  Project Overview

Forest fires are heavily influenced by environmental conditions such as temperature, humidity, wind speed, and fuel dryness. The **Fire Weather Index (FWI)** is an important indicator used to estimate fire intensity and risk.

This project:

* Cleans and analyzes wildfire data
* Trains multiple regression models
* Applies hyperparameter tuning
* Selects the best model
* Deploys the model using Flask
* Provides a simple web interface for predictions
* Deploys the application on AWS Elastic Beanstalk

---

##  Dataset Information

The dataset used is the **Algerian Forest Fires Dataset**, which contains meteorological observations and fire indicators from two regions of Algeria.

### Features Used

| Feature     | Description             |
| ----------- | ----------------------- |
| Temperature | Temperature in °C       |
| RH          | Relative Humidity (%)   |
| WS          | Wind Speed (km/h)       |
| RAIN        | Rainfall (mm)           |
| FFMC        | Fine Fuel Moisture Code |
| DMC         | Duff Moisture Code      |
| ISI         | Initial Spread Index    |
| CLASS       | Fire occurrence class   |
| REGION      | Geographic region       |

### Target Variable

* **FWI (Fire Weather Index)**

---

##  Data Preprocessing

The following preprocessing steps were performed:

1. Removed missing or inconsistent values
2. Converted categorical data to numerical format
3. Feature selection based on correlation analysis
4. Standardization using **StandardScaler**
5. Train-test split for model evaluation

Feature scaling was required because regression models perform better when features are normalized.

---

##  Exploratory Data Analysis (EDA)

EDA included:

* Distribution plots
* Correlation heatmaps
* Outlier detection
* Feature relationship analysis
* Regional fire comparisons

Insights from EDA helped in feature selection and model choice.

---

##  Machine Learning Models Used

Several regression models were evaluated:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Elastic Net Regression

---

##  Hyperparameter Tuning

Hyperparameter tuning was performed using **GridSearchCV** to optimize model performance.

### Elastic Net Parameters Tuned

| Parameter | Description                       |
| --------- | --------------------------------- |
| alpha     | Regularization strength           |
| l1_ratio  | Balance between L1 and L2 penalty |

The best hyperparameters were selected based on cross-validation performance.

---

##  Final Model Selection

After comparing models, **Ridge Regression** provided stable and reliable predictions with minimal overfitting.

Reasons for selection:

* Handles multicollinearity well
* Provides smooth coefficient shrinkage
* Good generalization on test data

---

##  Model Performance

Evaluation metrics used:

* R² Score
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

The final model achieved strong predictive performance on unseen data.

(You can insert your exact scores here)

Example:

```
Training R² Score: 0.98
Testing R² Score: 0.97
RMSE: 0.65
```

---

##  Model Saving

The trained model and scaler were saved using **pickle**:

* ridge.pkl → trained model
* scaler.pkl → feature scaler

This allows reuse without retraining.

---

##  Web Application

### Backend

* Flask (Python)
* Handles form input
* Loads model
* Performs prediction

### Frontend

* Simple HTML form
* User enters environmental parameters
* Displays predicted FWI

---

##  Deployment

The application is deployed using **AWS Elastic Beanstalk**.

Deployment steps:

1. Package Flask application
2. Configure environment
3. Upload application bundle
4. Launch web environment
5. Access live prediction service

---

##  Project Structure

```
Model_dep/
│
├── Models/
│   ├── ridge.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── EDA notebook
│   └── Model training notebook
│
├── templates/
│   └── index.html
│
├── application.py
├── requirements.txt
└── README.md
```

---

##  How to Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run Flask app:

```
python application.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

##  Prediction Workflow

1. User enters input values
2. Flask receives POST request
3. Data converted to DataFrame
4. Features scaled using StandardScaler
5. Model predicts FWI
6. Result displayed on webpage

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML
* AWS Elastic Beanstalk
* Pickle

---

##  Key Learnings

* End-to-end ML pipeline development
* Data preprocessing and scaling
* Hyperparameter tuning
* Model evaluation and selection
* Web deployment of ML model
* Cloud deployment with AWS

---

##  Author

Tarun

---

##  Future Improvements

* Better UI with Bootstrap
* Real-time weather API integration
* Model monitoring
* Docker container deployment
* Multiple model comparison dashboard

---

##  License

This project is for educational and research purposes.
