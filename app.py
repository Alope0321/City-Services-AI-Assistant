import streamlit as st
import pandas as pd
import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

st.title("City Services Assistant")

df = pd.read_csv("city_servicesinfo.csv")

issue = st.text_input("What issue would you like to report?")

if issue:
    with st.spinner("Finding the appropriate city service"):
        try:
            prompt = f"""
            You are a City Services Assistant that helps recommend the correct department

            A user reported this issue:
            "{issue}" 

            Using the available city service information, recommend the correct department,
            explain why the department handles the issue in a clear response. 

            Current city service data:
            {df.to_string(index=False)}
            """

            response = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=prompt
            )

            st.success(response.text)

        except Exception as e:
            st.error(str(e))

