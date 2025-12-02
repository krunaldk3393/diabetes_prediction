# 🩺 Diabetes Prediction System

A **Streamlit-based web application** that predicts the likelihood of diabetes using a trained Machine Learning model.  
Users enter basic health information, and the system instantly generates a prediction.

## 🚀 Features

- ✔️ Simple, interactive Streamlit UI  
- ✔️ Handles both categorical and numerical inputs  
- ✔️ Uses a trained ML model (`regressor.pkl`)  
- ✔️ Scales data using preprocessing scaler (`scaler.pkl`)  
- ✔️ Clear output messages (High Risk / Low Risk)  

## 📁 Project Structure

```
├── app.py                         # Streamlit web application
├── Diabetes_Prediction.ipynb      # Notebook used for training the model
├── diabetes_prediction_dataset.csv # Dataset used for training
├── regressor.pkl                  # Saved ML model
├── scaler.pkl                     # Saved scaler for preprocessing
└── README.md                      # Project documentation
```

## 🛠️ Technologies Used

- Python  
- Streamlit  
- Pandas, NumPy  
- Scikit-learn  
- Pickle  

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Start the Streamlit App
```bash
streamlit run app.py
```

## 🧠 Model Inputs

The app collects:

- Gender  
- Age  
- Hypertension  
- Heart Disease  
- Smoking History  
- BMI  
- HbA1c Level  
- Blood Glucose Level  

Prediction result:
- **1 → High Diabetes Risk**  
- **0 → Low/No Diabetes Risk**

## 📚 Dataset
`diabetes_prediction_dataset.csv`

## 🤖 Model Files
- `regressor.pkl`  
- `scaler.pkl`

## 🙌 Contributions
Contributions are welcome!

## 📄 License
MIT License

## 📫 Contact Me
- LinkedIn: [krunal patel](www.linkedin.com/in/krunal-patel-798465367)
- Email: patelkrunal2025.utran@gmail.com
- GitHub: [Krunal Patel](https://github.com/krunaldk3393)
