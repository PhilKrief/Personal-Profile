import streamlit as st
from weasyprint import HTML
from io import BytesIO
import pandas as pd
import os


business_plan_content = [
        ("Overview", "Our wealth management firm aims to provide personalized, automated, and cost-effective investment solutions to young professionals aged 25 to 40. We leverage cutting-edge technology and data-driven strategies to tailor portfolios that align with each client's risk tolerance, financial goals, and investment preferences. By streamlining our operations and targeting a similar audience, we can efficiently manage assets and offer competitive fees."),
        ("Target Audience", "Our primary target audience is young professionals seeking professional investment management services but are deterred by high fees charged by traditional firms. These individuals are tech-savvy, prefer digital solutions, and value convenience and simplicity. We will focus on clients who have moderate risk tolerance and a long-term investment horizon. Ideally, we will atract a similar age cohort to ensure a similar risk profile for all clients. This will also allow us to manage a similar portfolio for all clients, rolling from higher risk to lower risk as time goes on. "),
        ("Automated Technologies", 'We embrace the power of automation, developping and deploying automated processes to reduce middle office work. We will also use tehnology and AI to implement an investment strategy. This technology-driven approach allows us to minimize human intervention, reduce operational costs, and pass on the benefits to our clients in the form of lower fees. For a more detailed description of automated technologies, please refer to the report "The Future of Wealth Management"'),
        ("Portfolio Construction", "Using the aggregated data from clients with similar risk profiles, we will create model portfolios that represent the majority of assets under management (AUM). These model portfolios will be diversified across various asset classes and investment vehicles, ensuring efficient risk management and potential for long-term growth. While the majority of AUM will be invested in the model portfolios, we understand that each client has unique financial goals. Therefore, we will provide clients with the option to customize their portfolios by incorporating certain preferences, such as responsible investing (ESG), specific industries, or asset exclusions."),
        ("Fee Structure", "Our fee structure will be transparent and competitive, appealing to our target audience. We will charge a percentage-based fee on AUM, significantly lower than traditional wealth management firms. Additionally, we may offer tiered pricing to incentivize clients as their assets grow. In implementing automation, we will be able to reduce costs and pass some of the savings onto the client. "),
        ("Financial Projections", ""),
        ("Customer Support and Education", "We will prioritize financial education by offering educational content, webinars, and investment insights tailored to the needs of our young professional clients. Empowering clients with knowledge will help them make informed financial decisions and reinforce our value proposition. We will also tailor newletters to the clients portfolios, which can be sent at a frequency for their choice (weekly, monthly, quarterly). While technology-driven, we understand the importance of personalized service. Our clients will have access to a dedicated team of financial advisors who can provide guidance, answer queries, and offer assistance when needed. We will also offer periodic portfolio reviews to ensure alignment with changing life circumstances."),
        ("Marketing Strategy and Compliance", "Our marketing efforts will focus on digital channels, social media platforms, and partnerships with young professional organizations. Engaging content, testimonials, and referral programs will be used to attract and retain clients. As a wealth management firm, we will adhere to all relevant financial regulations, providing transparent disclosures and complying with legal requirements to ensure the trust and confidence of our clients."),
    ]


def create_pdf(business_plan_content, financialModel):
    # Business plan content
    title = "Business Plan"

    # Create HTML for PDF
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Business Plan</title>
        <style>
        /* Your CSS styles here */
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }}
        .section-container {{
            padding: 2rem;
            background-color: #f0f0f0;
            margin: 1rem 0;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }}
        .section h2 {{
            color: #007bff;
            font-size: 24px;
        }}
        .section p {{
            margin: 1rem 0;
            color: #333;
            font-size: 16px;
        }}
        </style>
    </head>
    <body>
        <h1 style="text-align: center;">{title}</h1>
    """

    for i, (section_title, section_content) in enumerate(business_plan_content):
        if section_title == "Financial Projections":
            df = financialModel.to_html(classes='dataframe section-table', index=True)
            html_content +=  f""" <div class='section-container'>
                    <h2>Financial Projections</h2>
                {df}
                </div>"""
        else:
            html_content += f"""
            <div class="section-container">
                <h2>{i+1}. {section_title}</h2>
                <p>{section_content}</p>
            </div>
            """

    html_content += """
        </body>
        </html>
    """

    # Generate PDF
    pdf_buffer = BytesIO()
    HTML(string=html_content).write_pdf(pdf_buffer)
    pdf_buffer.seek(0)

    return pdf_buffer

def business_plan_app(business_plan_content, financialModel):
    st.markdown(
        """
        <style>
        /* Your CSS styles here */
        .section-container {
            padding: 2rem;
            background-color: #f0f0f0;
            margin: 1rem 0;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        .section h2 {
            color: #007bff;
        }
        .section p {
            margin: 1rem 0;
            color: #333;
        }
        footer {
            background-color: #f0f0f0; /* Lighter gray color */
            color: #333;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
        }   
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Business Plan")

    for i, (section_title, section_content) in enumerate(business_plan_content):
        if section_title == "Financial Projections":

            df = financialModel.to_html(classes='dataframe section-table', index=True)
            html_content =  f""" <div class='section-container'>
                    <h2>Financial Projections</h2>
                {df}
                </div>"""
            st.markdown(html_content, unsafe_allow_html=True)

        else:
            html_content = f"""
            <div class="section-container">
                <h2>{i+1}. {section_title}</h2>
                <p>{section_content}</p>
            </div>
            """
            st.markdown(html_content, unsafe_allow_html=True)



    # PDF generation button
    if st.button("Generate PDF"):
        pdf_buffer = create_pdf(business_plan_content, financialModel)
        st.download_button("Download Business Plan PDF", data=pdf_buffer, file_name="business_plan.pdf", mime="application/pdf")
    
    pdf_file_path = os.path.join("assets", "20230713 - Wealth Management & AI - Philipe Elkrief.pdf")

# Create a download button
    if os.path.exists(pdf_file_path):
        st.download_button(
            label="Download Wealth Management & AI report",
            data=open(pdf_file_path, "rb").read(),
            file_name="your_file.pdf",
            mime="application/pdf",
        )
    st.markdown(
        """
        <footer>
            <p>Contact: philipelkrief@gmail.com | Phone: (514) 465-0763</p>
        </footer>
        """,
        unsafe_allow_html=True
    )



if __name__ == "__main__":
    averageClients = st.sidebar.number_input("Annual Client's Signed: ", value=20)
    averageAUM = st.sidebar.number_input("Average AUM: ", value=100000)
    annualContributions = st.sidebar.number_input("Average Annual Contribution: ", value=25000)
    fees = st.sidebar.number_input("Fees", step = 0.1, format="%0.3f", value=1.15)
    RevSplit = st.sidebar.number_input("Revenue Split (Take Home)", value=50, min_value=0, max_value=100)
    Costs = float(st.sidebar.number_input("Costs Percentage (Brokerage) ", value=40, min_value=0, max_value=100))
    OtherMiscCosts = st.sidebar.number_input("Other Misc. Costs", value=10000)
    taxRate = st.sidebar.number_input("Tax Rate", value=25)
    averageReturns =  st.sidebar.number_input("Average Annual Return",value=8)

    financialModel =  pd.DataFrame(columns=[1,2,3,4,5], index=['Client count', 'Average AUM', 'AUM', 'Fees', 'Revenue', 'Costs (brokerage)', 'Other Misc. Costs', 'Total Costs', 'Net Income Before Split and Taxes', 'Net Income Post Split', 'Income Taxes',  'Net Income'])



    for col in financialModel.columns:
        financialModel.loc['Client count', col] = averageClients * col
        if col == 1:
            financialModel.loc['Average AUM', col] = averageAUM
        else:
            financialModel.loc['Average AUM', col] = financialModel.loc['Average AUM', col-1] *((1+averageReturns/100)) + annualContributions
        financialModel.loc['AUM', col] = financialModel.loc['Client count', col] * financialModel.loc['Average AUM', col] 
        financialModel.loc['Fees', col] = fees
        financialModel.loc['Revenue', col] = financialModel.loc['AUM', col] * fees/100
        financialModel.loc['Costs (brokerage)', col] = financialModel.loc['Revenue', col] * Costs/100
        financialModel.loc['Other Misc. Costs', col] = OtherMiscCosts
        financialModel.loc['Total Costs', col] = financialModel.loc['Costs (brokerage)', col] + financialModel.loc['Other Misc. Costs', col] 
        financialModel.loc['Net Income Before Split and Taxes', col] = financialModel.loc['Revenue', col] - financialModel.loc['Total Costs', col]
        financialModel.loc['Net Income Post Split', col] =financialModel.loc['Net Income Before Split and Taxes', col] * RevSplit/100
        financialModel.loc['Income Taxes', col] =max(0,taxRate/100 * financialModel.loc['Net Income Post Split', col])
        financialModel.loc['Net Income', col] = financialModel.loc['Net Income Post Split', col] - financialModel.loc['Income Taxes', col]
    financialModel[financialModel.columns] = financialModel[financialModel.columns].astype(float).round(2)
    business_plan_app(business_plan_content, financialModel)




    
