import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to Generate Email
def generate_email(receiver, sender, purpose, tone):

    prompt = f"""
    You are an expert email writer.

    Write a complete email using the following details.

    Receiver: {receiver}
    Sender: {sender}
    Purpose: {purpose}
    Tone: {tone}

    The email should include:
    - Subject
    - Greeting
    - Email Body
    - Closing
    - Sender Name

    Generate only the email.
    """

    response = model.generate_content(prompt)

    return response.text


# Streamlit Page Configuration
st.set_page_config(
    page_title="AI Email Generator",
    page_icon="📧",
    layout="centered"
)

st.title("📧 AI Email Generator")
st.write("Generate professional emails using Gemini AI.")

# User Inputs
receiver = st.text_input("Receiver Name")

sender = st.text_input("Your Name")

purpose = st.text_area("Purpose of Email")

tone = st.selectbox(
    "Select Tone",
    [
        "Professional",
        "Formal",
        "Friendly",
        "Apology",
        "Thank You",
        "Request"
    ]
)

# Generate Button
if st.button("Generate Email"):

    if receiver and sender and purpose:

        with st.spinner("Generating Email..."):

            try:
                email = generate_email(receiver, sender, purpose, tone)

                st.success("Email Generated Successfully!")

                st.subheader("Generated Email")

                st.text_area(
                    "",
                    value=email,
                    height=350
                )

                st.download_button(
                    label="Download Email",
                    data=email,
                    file_name="generated_email.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please fill in all the fields.")
        