import streamlit as st
import asyncio
import time 
from fastmcp import Client

MCP_SERVER = "http://localhost:8000/mcp"

# --------- SIDEBAR ---------
with st.sidebar:


     # ----- Custom Button Styling -----
    st.markdown("""
        <style>
        div.stButton > button {
            background-color:#0072C6 ;
            color: Black;
            font-size: 18px;
            font-weight: bold;
            border-radius: 8px;
            height: 50px;
            width: 100%;
        }
        div.stButton > button:hover {
            background-color: #0072C6;
            color: Black;
        }
        </style>
    """, unsafe_allow_html=True)

    # Session state
    if "data_loaded" not in st.session_state:
        st.session_state.data_loaded = False

    # ---- Styled Button ----
    load_data = st.button("📊 Student Data Controls", key="load_data_btn")

    if load_data:
        with st.spinner("Loading students data..."):
            time.sleep(2)
            st.session_state.data_loaded = True

    if st.session_state.data_loaded:
        st.success("Students Data Loaded Successfully ✅")

   
   
    st.markdown(
        "<h2 style='color:#0072C6;text-align:center;'>💡 Example Questions</h2>",
        unsafe_allow_html=True
    )

    example_questions = [
        "Total number of students",
        "Average GPA",
        "Students per department",
        "Top GPA students",
        "Graduation year distribution",
        "Average GPA by department",
        "Youngest student",
        "Oldest student"
    ]

    for q in example_questions:
        st.markdown(
            f"<li style='margin-bottom:8px;font-size:16px;'>{q}</li>",
            unsafe_allow_html=True
        )

    # Flexible Spacer (pushes button downward)
    st.markdown("<div style='height:100px;'></div>", unsafe_allow_html=True)

    # Bottom Button
    clear_history = st.button("🗑️ Clear History", key="clear_btn")

# --------- MAIN UI ---------
st.markdown(
    "<h1 style='color:#005288;text-align:center;'>🎓 Students Data Chatbot (MCP)</h1>",
    unsafe_allow_html=True
)

# --------- SESSION STATE ---------
if "history" not in st.session_state:
    st.session_state.history = []

if clear_history:
    st.session_state.history = []

# --------- MCP CALL ---------
async def call_mcp(tool_name, params=None):
    async with Client(MCP_SERVER) as client:
        result = await client.call_tool(tool_name, params or {})
        return result

def run_async(tool_name, params=None):
    return asyncio.run(call_mcp(tool_name, params))

# --------- CHAT FORM ---------
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask me Here:", key="user_input")
    submitted = st.form_submit_button("Submit", key="submit_btn")

if submitted and user_input:
    query = user_input.lower()

    if "total" in query:
        result = run_async("total_students")
    elif "average gpa by department" in query:
        result = run_async("average_gpa_by_department")
    elif "average gpa" in query:
        result = run_async("average_gpa")
    elif "department" in query:
        result = run_async("students_per_department")
    elif "top" in query:
        result = run_async("top_gpa_students", {"n": 5})
    elif "graduation" in query:
        result = run_async("graduation_year_distribution")
    elif "youngest" in query or "oldest" in query:
        result = run_async("youngest_and_oldest")
    else:
        result = None

    # Extract clean text
    if result and hasattr(result, "content") and len(result.content) > 0:
        bot_reply = result.content[0].text
    else:
        bot_reply = "Sorry, I can't perform that analysis."

    st.session_state.history.append((user_input, bot_reply))

# --------- DISPLAY CHAT ---------
if st.session_state.history:
    for user, bot in st.session_state.history:
        st.markdown(
            f"<div style='background:#f0f0f0;padding:8px;border-radius:6px;margin-bottom:4px'>"
            f"<b>You:</b> {user}</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<div style='background:#e6f7ff;padding:8px;border-radius:6px;margin-bottom:10px'>"
            f"<b>Bot:</b> {bot}</div>",
            unsafe_allow_html=True
        )