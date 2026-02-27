# 🎓 Students Analytics Dashboard

> A Modern Student Data Analytics Dashboard built using **Streamlit** and **FastMCP (MCP Server Integration)**.

---

## 📌 Overview

The **Students Analytics Dashboard** is an interactive web application that allows users to:

- Load student data
- Perform analytics using MCP tools
- Interact through a chatbot interface
- View KPI metrics
- Manage chat history

This project demonstrates integration between **Streamlit (Frontend UI)** and **FastMCP (Backend Tool Calling Server)**.

---

## 🚀 Features

- 🟣 Custom Styled Sidebar Control Panel
- 📊 "Student Data Controls" Clickable Loader
- ⏳ Spinner Animation While Loading
- ✅ Success Confirmation Message
- 📈 KPI Metrics Cards
- 💬 Chat-Based Query System
- 🧠 MCP Tool Integration
- 🗑️ Clear Chat History
- 🎨 Clean Dashboard Layout

---

## 🏗️ Project Structure

```bash
project-folder/
│
├── streamlit_chatbot.py   # Main Streamlit Application
├── main.py                # MCP Server (FastMCP tools)
├── requirements.txt       # Project Dependencies
└── README.md              # Documentation
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/students-analytics-dashboard.git
cd students-analytics-dashboard
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

Example `requirements.txt`:

```txt
streamlit
fastmcp
uvicorn
matplotlib
```

---

## ▶️ Running the Application

### Step 1: Start MCP Server

```bash
uvicorn main:app --reload
```

MCP Server runs at:

```
http://localhost:8000/mcp
```

---

### Step 2: Run Streamlit App

```bash
streamlit run streamlit_chatbot.py
```

The application will open in your browser.

---

## 💬 Example Queries

You can ask the chatbot:

- Total number of students
- Average GPA
- Students per department
- Top GPA students
- Graduation year distribution
- Youngest student
- Oldest student

---

## 🧠 How It Works

1. User clicks **Student Data Controls** in sidebar.
2. Spinner shows loading state.
3. Success message confirms data loading.
4. User submits a query.
5. Query maps to appropriate MCP tool.
6. MCP server processes the request.
7. Response is displayed in chat format.

---

## 🎨 UI Layout

### 🔹 Sidebar
- Student Data Controls Button
- Example Questions
- Clear History Button

### 🔹 Main Dashboard
- Dashboard Header
- KPI Metrics Row
- Chat Interface

---

## 🔮 Future Enhancements

- 📊 Interactive Charts (Plotly)
- 🎯 Advanced Filtering
- 🔐 Authentication System
- 📈 Real-Time Data Updates
- 📤 Export Reports (PDF/Excel)
- 🌍 Cloud Deployment (Streamlit Cloud / AWS / Render)

---

## 🛠️ Tech Stack

- Python
- Streamlit
- FastMCP
- Uvicorn
- Asyncio
- Matplotlib (Optional for Charts)

---

## 📷 Screenshots

_Add dashboard screenshots here after deployment._

---

## 📄 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

Built as a Student Data Analytics Dashboard Project.

---

⭐ If you like this project, consider giving it a star on GitHub!

