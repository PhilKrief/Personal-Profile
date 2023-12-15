from pathlib import Path

import streamlit as st
from PIL import Image,  ImageDraw, ImageOps


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
#resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "2.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Philipe Elkrief"
PAGE_ICON = ":barchart:"
NAME = "Philipe Elkrief, CFA"
DESCRIPTION = """
Finance Professional and CFA Chartholder leveraging AI and automation to optimize wealth management operations and effeciently manage portfolios.
"""
EMAIL = "philipeelkrief@gmail.com"
#Linkedin ="https://linkedin.com"



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout='wide' )


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
#with open(resume_file, "rb") as pdf_file:
#    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# Define a function to create a rounded image effect
def create_rounded_image(image,):
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
    result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    result.putalpha(mask)
    return result

# Apply rounded image effect
rounded_pic = create_rounded_image(profile_pic)

# Display the rounded image


# Continue with the rest of your app co



# --- HERO SECTION ---
col1, col2 = st.columns([0.2, 0.8])
with col1:
    st.image(rounded_pic,)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    #st.download_button(
    #    label=" 📄 Download Resume",
        #data=PDFbyte,
        #file_name=resume_file.name,
    #    mime="application/octet-stream",
    #)
    st.write(f"""{EMAIL}""")
    #st.write(Linkedin)


# --- Summary ---
st.write('\n')
st.subheader("Summary")
st.write("---")
st.markdown(
    """ 
Dedicated Finance Professional and CFA Chartholder with 5+ years of experience. Expertise in automating financial processes and implementing AI solutions for wealth managers. Developed tools for portfolio analysis, benchmarking, stress testing, dashboards, and monthly reporting. Skilled developer and financial expert bridging the gap between finance and technology.
""", unsafe_allow_html=True
)

# --- EXPERIENCE & QUALIFICATIONS --
st.write('\n')
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
    """
- ✔️ 5+ Years experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ In-depth financial expertise 
- ✔️ Excellent understanding of statistical principles and their respective applications
- ✔️ Team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, LangChain, OpenAI) 
- 📊 Data Visulization: Streamlit, PowerBI, MS Excel, Plotly
- 📈 Finance: Portfolio Management, Financial Analysis, Financial Modeling, Financial Reporting
- 📚 Modeling: Linear Regression, Logistic Regression, Decision Trees, Neural Network
- 🗄️ Databases: Postgres, SQLlite, MongoDB
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Projects")
st.write("---")
st.markdown("""<a href="https://wealth-management-tool.streamlit.app">📈 Wealth Management Tool: Tool to Automate and Modernize Client Meetings </a>
            <a href="https://filbot.streamlit.app"> 🤖 Filbot : Finance Oriented Chatbot </a>
            <a href="https://filbot.streamlit.app/scenario_analysis"> ❔ Scenario Analysis Tool : Demonstrate Scenario Analysis to clients  </a>
    
            """, unsafe_allow_html=True)


st.write(
    """
- 
- 

"""
)




# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Advisor - Business Development | Desjardins**")
st.write("06/2022 - Present")
st.write(
    """
- Used PowerBI and SQL to redeﬁne and track private fund performance. Created comparative dashboard for benchmarking and portfolio analysis which allowed senior management to contrast private funds with internal and external public funds
- Led multiple projects to develop automated tools to generate comprehensive monthly reports, enhancing transparency and reducing manual efforts. This allowed gave financial advisors material which they had not had access to before
- Responsible for analyzing prospective clients' portfolios and conducting comparative assessments against internal portfolios to provide strategic investment recommendations.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Consultant - Analyst | Accuracy**")
st.write("10/2020 - 06/2022")
st.write(
    """
- Developed and implemented code for stress testing at two major banks to assess financial resilience and mitigate risk.
- Designed and built an automated tool for seamless revenue recognition across a diverse portfolio of contracts, enhancing accuracy and efficiency.
- Collaborated as part of a team of consultants to assist a major real estate manager in strategically unloading an asset class, optimizing their portfolio and maximizing returns.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Tradefan**")
st.write("07/2019 - 10/2020")
st.write(
    """
- Analyzed data to calculate Lifetime Value (LTV) and Customer Acquisition Cost (CAC), providing valuable insights for business decision-making.
- Created models for multiple sports, with results matching biggest sports books odds.
- Assessed existing processes and recommending changes to optimize revenue generation and maximize profitability.
- Collaborated to identify and address data architecture issues, improving data quality, accessibility, and reliability for enhanced organizational efficiency.
"""
)
