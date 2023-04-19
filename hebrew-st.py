# this app takes in english words in streamlit and then uses the openAI api to get 
# the translation and the pronunciation for the input

import streamlit as st
import openai


# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to get pronunciation and translation from OpenAI API
def get_pronunciation_and_translation(text, gender):
    prompt = f"""
               Assuming a speaker is {gender} speaking, translate the English phrase `{text}` into Hebrew. Provide the pronunciation as well.  I want you to respond with the format: \n `Hebrew: \n Pronunciation:`
               """
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.3,
    )

    response_text = response.choices[0].text.strip()
    print(response_text)
    translation, pronunciation  = response_text.split("\n")

    return translation, pronunciation

# Streamlit app
st.title("English to Hebrew Translation With Pronunciation")

# get gender from user
gender = st.selectbox("Choose an option:", ['male','female'])


user_input = st.text_input("Enter the English phrase you want to translate:")

if st.button("Submit"):
    translation, pronunciation = get_pronunciation_and_translation(user_input, gender)
    st.write("---\n## ",pronunciation)
    st.write("## ",translation)
