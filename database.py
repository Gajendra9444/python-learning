"""
simple chat agent hat uses a language model to respond to user queries.

"""

import streamlit as st  
from groq import Groq

st.title("Simple Chat Agent")
st.write("This is a simple chat agent that uses a language model to respond to user queries.")

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

user_query = st.text_input("Enter your query:")
send_btn = st.button ("send")

system_prompt ={
    "role": "system",
    "content": "You are a helpful assistant that provides information and answers to your best ability. "

}

if send_btn and user_query:
    user_query_prompt = {
        "role": "user",
        "content": user_query
    }

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[system_prompt, user_query_prompt],
        max_tokens=1500,
        temperature=0.7
    )

    result = response.choices[0].message.content
    st.write(f"**Response:** {result}")
