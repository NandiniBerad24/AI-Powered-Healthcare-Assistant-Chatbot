import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


chatbot = pipeline("text-generation",model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please Consult Doctor for Accurate Advice"
    elif "appointment" in user_input:
        return "Would you like to Schedule an Appointment with Doctor?"
    elif "medication" in user_input:
        return "It's Important to take Medicines as Prescribed By Doctor"
    else:
        response = chatbot(user_input,max_length =100,num_return_sequences=1)
        return response[0]['generated_text']
      
def main():
    st.title("AI based Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I Assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User :",user_input)
            with st.spinner("Processing your Query,Please Wait..."):
                response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant:",response)
            print(response)
        else:
            st.write("Please enter a Message to get a Response")

main()
