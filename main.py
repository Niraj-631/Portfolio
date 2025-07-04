import streamlit as st
from streamlit_lottie import st_lottie
#import requests
from contact_form import contact_form
from lottie_animations import lottie_animations
import sqlite3 

# --- Page Config ---
st.set_page_config(page_title="Niraj's AI/ML Portfolio", layout="wide", page_icon="🤖")

st.markdown(
    """
    <style>
    /* Dark blue vertical divider on the right edge of sidebar */
    section[data-testid="stSidebar"] {
        border-right: 4px solid #00008B;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Navigation ---

st.sidebar.image("assets/profile.png", width=300)
st.sidebar.markdown(
    '<h1 style="color: red;">Niraj Kumar Yadav</h1>',
    unsafe_allow_html=True
)
st.sidebar.markdown(
    '<h2 style="color: #00cc66;">AI/ML & GenAI Developer</h2>',
    unsafe_allow_html=True
)
st.sidebar.divider()

section = st.sidebar.radio("📂 Sections", [
    "🏠 Home",  
    "📁 Projects", 
    "🧠 Skills", 
    "🎓 Education", 
    "📜 Certifications", 
    "✍️ Blog", 
    "📬 Contact"])

st.sidebar.markdown("---")
st.sidebar.markdown("**Connect**")

# LinkedIn icon using HTML (must set unsafe_allow_html=True)
st.sidebar.markdown(
    """
    <style>
        .sidebar-social a img {
            transition: transform 0.3s ease, filter 0.3s ease;
        }
        .sidebar-social a:hover img {
            transform: scale(1.2);
            filter: brightness(1.3);
        }
    </style>

    <div class="sidebar-social" style="display: flex; justify-content: center; gap: 20px;">  
        <a href="https://www.linkedin.com/in/your-linkedin-username" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="40" height="40">
        </a>
        <a href="https://github.com/Niraj-631" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/270/270798.png" alt="GitHub" width="40" height="40">
        </a>
        <a href="mailto:yadavnirajkumar631gmail.com" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email" width="40" height="40">
        </a>
    </div>    
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');

    .ai-heading-container {
        position: relative;
        margin-top: 40px;
        margin-bottom: 30px;
        height: 60px;
    }

    .ai-heading-text {
        position: absolute;
        top: -35px;
        left: 0;
        width: 100%;
        text-align: center;
        font-size: 28px;
        font-family: 'Orbitron', sans-serif;
        color: #0000cd; /* blue */
        text-shadow: 0 0 10px rgba(0, 77, 64, 0.8);
        animation: slide-blink 6s ease-in-out infinite;
    }

    .ai-line {
        height: 4px;
        width: 100%;
        background-color: #00a877 ;
    }

    @keyframes slide-blink {
        0%   { transform: translateX(-100%); opacity: 0; }
        25%  { opacity: 1; }
        50%  { transform: translateX(0); opacity: 1; }
        75%  { opacity: 1; }
        100% { transform: translateX(100%); opacity: 0; }
    }
    </style>

    <div class="ai-heading-container">
        <div class="ai-heading-text">Artificial Intelligence</div>
        <div class="ai-line"></div>
    </div>
    """,
    unsafe_allow_html=True
)




# --- Dynamic Metrics from SQLite ---
def get_metrics():
    conn = sqlite3.connect("data/metrics.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS metrics (label TEXT, value TEXT, change TEXT)''')
    c.execute("SELECT COUNT(*) FROM metrics")
    if c.fetchone()[0] == 0:
        sample = [
            ("🧠 GenAI Projects", "6", "+2 this month"),
            ("📈 ML Projects", "4", "+1 this month"),
            ("💰 Earnings from AI", "$150", "+$50 this month"),
            ("🛠 Tools Mastered", "12", "+3 this month"),
            ("✍️ Blog Posts", "5", "+1 this week")
        ]
        c.executemany("INSERT INTO metrics VALUES (?, ?, ?)", sample)
        conn.commit()
    c.execute("SELECT * FROM metrics")
    data = c.fetchall()
    conn.close()
    return data
# Home section
# --- Main Sections ---
if section == "🏠 Home":
    st.markdown("""
        <style>
        .home-title {
            font-size: 42px !important;
            font-weight: bold;
            color: #00b4d8;
        }
        .home-subtitle {
            font-size: 22px !important;
            color: #ffffff;
        }
        .highlight {
            color: #38b000;
            font-weight: bold;
        }
        .gradient-bg {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            padding: 2rem;
            border-radius: 12px;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("<div class='gradient-bg'>", unsafe_allow_html=True)
            st.markdown("<p class='home-title'>Hi, I'm <span class='highlight'>Niraj Kumar Yadav</span> 👋</p>", unsafe_allow_html=True)
            st.markdown("<p class='home-subtitle'>AI/ML & Generative AI Developer | Building the future with intelligent tools.</p>", unsafe_allow_html=True)
            st.markdown("""
                🔹 I specialize in building smart applications powered by AI and ML.  
                🔹 Skilled in Python, Streamlit, scikit-learn, and Hugging Face.  
                🔹 Currently working on GenAI tools, LLM apps, and chatbot automation.  
                🔹 Actively seeking remote/full-time roles in AI product development.
            """)
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st_lottie(lottie_animations["hero"], height=300)

    st.markdown("---")
    st.markdown("## 🔭 What I'm working on")
    left, right = st.columns([1, 1])
    with left:
        st.markdown("""
        - 🚀 **AI Resume Writer** – Uses OpenAI API + Streamlit + LangChain
        - 📊 **Finance Data Dashboard** – Python + Pandas + Plotly + Streamlit
        - 🤖 **Chatbot Automation Tool** – SQLite + LangChain + Memory
        - 🎥 **YouTube Automation** – Scripts + Shorts via LLM
        """)
    with right:
        st_lottie(lottie_animations["network"], height=250)

    st.markdown("---")
    st.markdown("""
    <div style='background-color: #f0f8ff; padding: 0px; border-radius: 8px;'>
        <h2 style='color: #00008B; margin: 0;'>🧭 Explore My Portfolio</h2>
    </div>
""", unsafe_allow_html=True)

    st.markdown("""
    Use the sidebar to navigate through OR <span style='color:red;'>Scroll Down to explore</span>:
    - 📁 Projects  
    - 🧠 Skills  
    - 🎓 Education  
    - 📜 Certifications  
    - ✍️ Blog  
    - 📬 Contact  
    """, unsafe_allow_html=True) 
    st.markdown("---")
    st.subheader("📁 Highlight Projects")
    st.markdown("### AI Webscraper")
    st.write("""
 🔹Features: Authentication (sign up, log in, log out, update profile), The objective is to build an automated solution that can extract, process, and analyze web data   efficiently while ensuring compliance with legal and ethical guidelines after that we can communicate with the extract data  
 🔹Technologies: Python, Streamlit, Ollama, Chrome, Chrome Driver, Selenium, BeautifulSoup, LangChain, streamlit and other related technologies.\n
 🔹Hosting: Streamlit.              
             
             """)
    st.markdown("[🔗 Live App](https://ai-webscraper-i7tjns439qy2zew4m5muqf.streamlit.app/) | [📂 GitHub](https://github.com/Niraj-631/AI-WEBSCRAPER)")

    st.markdown("### 📊 House Price Predictor (ML)")
    st.write("""Predicts housing prices using Linear Regression.\n
 🔹Developed a Streamlit web app to predict house prices based on location and nearby   amenities using a machine learning regression model. Integrated interactive user inputs, real-time predictions, and deployed on Streamlit Cloud for easy access.  
 🔹 Technologies: Python, Scikit-learn, NumPy, Pandas, Streamlit and related technologies.  
 🔹 Hosting: Streamlit. 

             """)
    st.markdown("[🔗 Live App](https://niraj-631-house-price-prediction-app-p4tvxk.streamlit.app/) | [📂 GitHub](https://github.com/Niraj-631/House-Price-Prediction)")
    
    
    st.markdown("---")
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 0px; border-radius: 8px;">
        <h2 style="color: #00a877; margin: 0;">🧠 Skills</h2>
    </div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - 🧠 **Generative AI**: ChatGPT, Claude, Midjourney, Prompt Engineering
        - 🤖 **AI & ML Frameworks**: scikit-learn, Keras, pandas, NumPy, Matplolib, Seaborn,
        - 🛠 **Tools & Platform**: Streamlit, LangChain, Hugging Face, SQLite, Git, Github, Jupiter, Hugging face, Google-Colab, VS-code
        - 💻 **Languages**: Python, SQL, HTML/CSS 
        - 💻 **Computer Fundatamentals**: OOPS,OS, DBMS, DSA
        """)
    with col2:
        st_lottie(lottie_animations["skills"], height=300)
    
    st.markdown("---") 
    st.markdown('<h1 style="color: #FFD700;">🎓 Education</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - **Bachelor of Technology (B.Tech)** – Computer Science Engineering
            - Institution: Panipat Institue of Engineering and Technology
            - Duration: 2021–2025
            - CGPA: 6.7/10

        - **NEB Board (Class XII)**:
            - School: Om National Academy, Birgunj
            - Duration: 2018-2029
            - Percentage: 66%
            
        - **SEE Board (Class X)**:
            - School: Saint Jhon's Secondary School, Birgunj
            - Duration: 2017
            - Percentage: 66%
        """)
    with col2:
        st_lottie(lottie_animations["education"], height=300)
    
    st.markdown("---")
    st.markdown('<h1 style="color: #00827f;">Achivement &🎓 Certifications</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
       st.markdown("""
### ✅ Work Experience
- 🧑‍💻 **Computer Assistant**  
  🏢 *Nepal Kinetic Courier and Cargo*, Nepal  
  🕒 2 years experience  

### 🏅 Certifications
- 🎓 Prompt Engineering – Coursera → [📄 View Certificate](https://pdf.ac/3TIbtb)
- 🧪 Machine Learning with Python – Cognitive Class → [📄 View Certificate](https://pdf.ac/2xTRpD)
- 💡 Python Pro Bootcamp – Udemy → [📄 View Certificate](https://pdf.ac/4SWEUV)
- 🔍 NLP with Hugging Face – Hugging Face Course 
""")

    with col2:
        st_lottie(lottie_animations["certification"], height=300) 
    
    st.markdown("---") 
    st.subheader("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            success = contact_form(name, email, message)
            if success:
                st.success("✅ Message sent successfully!")
            else:
                st.error("❌ Failed to send message. Try again later.")

    st.markdown("---")

# Projects section

elif section == "📁 Projects":
    st.subheader("📁 Highlight Projects")
    st.markdown("### AI Webscraper")
    st.write("""
 🔹Features: Authentication (sign up, log in, log out, update profile), The objective is to build an automated solution that can extract, process, and analyze web data   efficiently while ensuring compliance with legal and ethical guidelines after that we can communicate with the extract data  
 🔹Technologies: Python, Streamlit, Ollama, Chrome, Chrome Driver, Selenium, BeautifulSoup, LangChain, streamlit and other related technologies.\n
 🔹Hosting: Streamlit.              
             
             """)
    st.markdown("[🔗 Live App](https://ai-webscraper-i7tjns439qy2zew4m5muqf.streamlit.app/) | [📂 GitHub](https://github.com/Niraj-631/AI-WEBSCRAPER)")

    st.markdown("### 📊 House Price Predictor (ML)")
    st.write("""Predicts housing prices using Linear Regression.\n
 🔹Developed a Streamlit web app to predict house prices based on location and nearby   amenities using a machine learning regression model. Integrated interactive user inputs, real-time predictions, and deployed on Streamlit Cloud for easy access.  
 🔹 Technologies: Python, Scikit-learn, NumPy, Pandas, Streamlit and related technologies.  
 🔹 Hosting: Streamlit. 

             """)
    st.markdown("[🔗 Live App](https://niraj-631-house-price-prediction-app-p4tvxk.streamlit.app/) | [📂 GitHub](https://github.com/Niraj-631/House-Price-Prediction)")
    
# Skills section

elif section == "🧠 Skills":
    st.markdown('<h1 style="color: #00a877;">🧠 Skills</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - 🧠 **Generative AI**: ChatGPT, Claude, Midjourney, Prompt Engineering
        - 🤖 **AI & ML Frameworks**: scikit-learn, Keras, pandas, NumPy, Matplolib, Seaborn,
        - 🛠 **Tools & Platform**: Streamlit, LangChain, Hugging Face, SQLite, Git, Github, Jupiter, Hugging face, Google-Colab, VS-code
        - 💻 **Languages**: Python, SQL, HTML/CSS 
        - 💻 **Computer Fundatamentals**: OOPS,OS, DBMS, DSA
        """)
    with col2:
        st_lottie(lottie_animations["skills"], height=300)
# Education section
elif section == "🎓 Education":
    st.markdown('<h3 style="color: #FFD700;">🎓 Education</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - **Bachelor of Technology (B.Tech)** – Computer Science Engineering
            - Institution: Panipat Institue of Engineering and Technology
            - Duration: 2021–2025
            - CGPA: 6.7/10

        - **NEB Board (Class XII)**:
            - School: Om National Academy, Birgunj
            - Duration: 2018-2029
            - Percentage: 66%
            
        - **SEE Board (Class X)**:
            - School: Saint Jhon's Secondary School, Birgunj
            - Duration: 2017
            - Percentage: 66%
        """)
    with col2:
        st_lottie(lottie_animations["education"], height=300)
# Certifications section
elif section == "📜 Certifications":
    st.markdown('<h1 style="color: #00827f;">Achivement &📜 Certifications</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
### ✅ Work Experience
- 🧑‍💻 **Computer Assistant**  
  🏢 *Nepal Kinetic Courier and Cargo*, Nepal  
  🕒 2 years experience  

### 🏅 Certifications
- 🎓 Prompt Engineering – Coursera → [📄 View Certificate](https://pdf.ac/3TIbtb)
- 🧪 Machine Learning with Python – Cognitive Class → [📄 View Certificate](https://pdf.ac/2xTRpD)
- 💡 Python Pro Bootcamp – Udemy → [📄 View Certificate](https://pdf.ac/4SWEUV)
- 🔍 NLP with Hugging Face – Hugging Face Course 
""")
    with col2:
        st_lottie(lottie_animations["certification"], height=300)
# Blog section
elif section == "✍️ Blog":
    st.subheader("✍️ Latest Blog Posts")
    st.markdown("Coming soon: Blog integration from Hashnode or Medium!")
    st.markdown("Stay tuned for technical articles, case studies, and tutorials.")
# Contact section
elif section == "📬 Contact":
    st.subheader("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            success = contact_form(name, email, message)
            if success:
                st.success("✅ Message sent successfully!")
            else:
                st.error("❌ Failed to send message. Try again later.")


st.markdown(
    """
    <style>
        .social-icons a img {
            transition: transform 0.3s ease, filter 0.3s ease;
        }
        .social-icons a:hover img {
            transform: scale(1.2);
            filter: brightness(1.2);
        }
    </style>

    <div class="social-icons" style="display: flex; justify-content: center; gap: 20px;">
        <a href="https://www.linkedin.com/in/your-linkedin-username" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="40" height="40">
        </a>
        <a href="https://github.com/Niraj-631" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/270/270798.png" alt="GitHub" width="40" height="40">
        </a>
        <a href="mailto:yadavnirajkumar631gmail.com" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email" width="40" height="40">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown("---")

# Load local PDF (must be in assets/resume.pdf)
with open("assets/resume.pdf", "rb") as file:
    resume_bytes = file.read()

# Show a PDF icon with hover effects using CSS
st.markdown(
    """
    <style>
        .pdf-icon img {
            transition: transform 0.3s ease, filter 0.3s ease;
        }
        .pdf-icon:hover img {
            transform: scale(1.2);
            filter: brightness(1.3);
        }
    </style>
    <div class="pdf-icon" style="text-align: left;">
        <img src="https://cdn-icons-png.flaticon.com/512/337/337946.png" width="60" height="60">
    </div>
    """,
    unsafe_allow_html=True
)

# Show actual download button below
st.download_button(
    label="📄 Download My Resume",
    data=resume_bytes,
    file_name="Niraj_Resume.pdf",
    mime="application/pdf"
)
