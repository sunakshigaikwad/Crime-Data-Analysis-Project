# 🚔 Crime Data Analysis and Prediction with ML, Power BI, and Web App

A full-stack data science project that combines **Machine Learning**, **Power BI visualizations**, and a **Flask web application** to analyze and predict crime patterns from a large dataset. This project aims to provide data-driven insights and real-time crime prediction through an interactive dashboard and web interface.

---

## 📁 Project Structure

Crime-Data-Analysis-Project/
├── model/
│ ├── crime_model_building.ipynb # Jupyter Notebook for ML model training
│ └── Untitled.ipynb # (Optional - clean or remove)
├── templates/
│ └── index.html # Frontend page (Flask)
├── app.py # Flask web application backend
├── crime.csv.csv # Crime dataset (excluded from GitHub)
├── .gitignore # Git ignore file for large/unwanted files
└── README.md # You're here!

yaml
Copy code

---

## 🧠 Key Features

- ✅ **Machine Learning model** to predict crime category based on inputs
- ✅ **Power BI Dashboard** to visualize crime trends and patterns
- ✅ **Flask Web App** with user-friendly interface for predictions
- ✅ **Cloud Deployable** using platforms like Render
- ✅ Modular and well-documented project structure

---

## 📊 Tools & Technologies Used

- Python, Pandas, NumPy, Scikit-learn
- Flask (Web Framework)
- Power BI (Visualization)
- Git, GitHub (Version Control)
- Render (Cloud Hosting)
- Jupyter Notebook (for model building)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sunakshigaikwad/Crime-Data-Analysis-and-Prediction-with-ML-Power-BI-and-Web-App.git
cd Crime-Data-Analysis-Project
2. Install Required Packages
bash
Copy code
pip install -r requirements.txt
If requirements.txt does not exist yet, create it with:

nginx
Copy code
flask
pandas
numpy
scikit-learn
joblib
🚀 Running the App Locally
Make sure your trained model (model.pkl) is saved in the model/ folder.

bash
Copy code
python app.py
Open your browser and go to http://127.0.0.1:5000.

🧪 Model Training
You can train your own model using the Jupyter Notebook:

Open model/crime_model_building.ipynb

Load and preprocess the dataset

Train the model (e.g., Random Forest, Logistic Regression)

Save it using:

python
Copy code
import joblib
joblib.dump(model, 'model/model.pkl')
Make sure the model path matches the one in app.py.

📈 Power BI Dashboard
A comprehensive Power BI dashboard provides insights like:

Crime frequency by state/year

Crime types distribution

Crime trends over time

🔗 [Add your Power BI dashboard link here OR embed using iframe]

🌐 Deployment on Render (or any cloud platform)
Push your project to GitHub ✅

Sign up at Render

Create a new Web Service

Connect your GitHub repo

Set:

Build Command: pip install -r requirements.txt

Start Command: python app.py

Deploy! Your app will be live on the web 🌍

🧾 Dataset
The original dataset (crime.csv.csv) is too large for GitHub (232 MB).

📥 Download Crime Dataset from Google Drive

Be sure to place it in the project root folder to run Jupyter notebooks properly.

💡 Future Improvements
Add Google Maps/Folium heatmap visualizations

User authentication in web app

Crime prediction with geolocation

REST API for mobile use

Email notification or alerts system

✍️ Author
Sunakshi Gaikwad
📧 Email: sunakshigaikwad2@gmail.com
🔗 GitHub: sunakshigaikwad
🔗 LinkedIn: linkedin.com/in/sunakshigaikwad

🌟 Show Your Support
If you liked this project:

⭐ Star the repository

🛠️ Fork and customize it

🤝 Share with your network
