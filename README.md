🎓 Students Analytics Dashboard (MCP + Streamlit)

A modern interactive Students Data Analytics Dashboard built using Streamlit and FastMCP.
This project allows users to load student data, analyze it using MCP tools, and interact with the dataset through a chatbot interface.

🚀 Features

📊 Sidebar Data Control Panel

🟣 Custom Styled "Student Data Controls" Button

⏳ Spinner While Loading Data

✅ Success Confirmation Message

📈 KPI Metrics Section (Total Students, Average GPA, Departments)

💬 Chat-Based Query System

🧠 MCP Tool Integration for Data Analysis

🗑️ Clear Chat History Option

🎨 Clean Dashboard UI

🏗️ Project Structure
project-folder/
│
├── streamlit_chatbot.py   # Main Streamlit App
├── requirements.txt       # Dependencies
└── README.md              # Project Documentation
⚙️ Installation
1️⃣ Clone the Repository
git clone <your-repo-url>
cd project-folder
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate    # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
📦 Required Libraries

Make sure your requirements.txt includes:

streamlit
fastmcp
asyncio
matplotlib
▶️ Running the Application

Start your MCP server first:

uvicorn main:app --reload

Then run the Streamlit app:

streamlit run streamlit_chatbot.py

The app will open in your browser automatically.

💬 Example Queries

You can ask:

Total number of students

Average GPA

Students per department

Top GPA students

Graduation year distribution

Youngest student

Oldest student

🧠 How It Works

User clicks Student Data Controls to load data.

Data loading spinner appears.

Success message confirms loading.

User enters a query in chat.

Query is matched to MCP tool.

MCP processes request.

Response is displayed in chat format.

🎨 UI Overview
Sidebar

Student Data Controls

Example Questions

Clear History Button

Main Dashboard

Dashboard Header

KPI Metrics

Chat Interface

🔮 Future Improvements

📊 Interactive Charts (Plotly)

🎯 Smart Filters

🔐 Authentication System

📈 Real-time Data Refresh

📤 Export Reports (PDF/Excel)

🌍 Cloud Deployment

🛠️ Tech Stack

Python

Streamlit

FastMCP

Asyncio

Matplotlib (optional for charts)
