import streamlit as st
import markdown2
from groq import Groq

client = Groq(api_key='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')

st.title("Business Idea Validator")

content = """
  - You are a Business adviser, Business Idea Validator  
  - Your task is to generate a report about this product idea
  - You have to give all the possible market competitors, suggestions, budget, timing, and locations to grow
  - You are a competitor analysis expert.
  - Your task is to research the current competitors for a new eco-friendly clothing line.
  - Identify the major players, their pricing strategies, product uniqueness, and marketing channels.
  - Provide suggestions on how the new brand can differentiate itself in the market.
  - You are a target market research expert.
  - Your task is to create a report on the potential target audience for a subscription-based meal delivery service focused on busy professionals.
  - Identify key demographic traits, behaviors, and preferences.
  - Offer suggestions on marketing channels, pricing models, and promotional strategies to reach this audience effectively.
  - You are a financial advisor.
  - Your task is to create a financial projection for a tech startup launching a home automation product.
  - Calculate the initial investment needed, estimate the break-even point, and forecast the revenue for the first three years.
  - Provide recommendations on potential investors or grants that could fund the venture.
  - You are a product launch strategist.
  - Your task is to develop a comprehensive product launch plan for an online educational platform offering AI-based learning tools.
  - Provide a timeline for product development, marketing strategies, and a rollout plan for local and international markets.
  - Suggest the best channels to create buzz and attract early adopters.

"""

business_idea = st.text_area("Enter your business idea:", placeholder="Describe your business idea...")

if st.button("Generate Report"):
    if business_idea:
        with st.spinner("Generating report..."):
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": content},
                    {"role": "user", "content": business_idea}
                ],
                model="llama3-8b-8192",
                temperature=0.5,
                max_tokens=1024,
                top_p=1,
                stop=None,
                stream=False
            )

            st.success("Report generated successfully!")
            
            # Convert the generated text to markdown
            markdown_content = markdown2.markdown(chat_completion.choices[0].message.content)
            st.markdown(markdown_content, unsafe_allow_html=True)
    else:
        st.error("Please enter a business idea.")
