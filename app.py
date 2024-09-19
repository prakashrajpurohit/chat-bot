import streamlit as st
import markdown2
from groq import Groq

client = Groq(api_key='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')

st.title("Business Idea Validator")

content = """
  - You are a Business adviser, Business Idea Validator  
  - Your task is to generate a report about this product idea
  - You have to give all the possible market competitors, suggestions, budget, timing, and locations to grow
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
