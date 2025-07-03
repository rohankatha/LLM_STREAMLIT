import streamlit as st

grok_key = "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"
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
model=Ollama(model = "llama3.2:latest")

prompt = ChatPromptTemplate([
    ("system","Translate the text given into telugu"),("user","{text}")
])
parser = StrOutputParser()
chain = prompt|model|parser

st.title("Translate to telugu")
input_text = st.text_input("Write what you want to translate")

if input_text:
    st.write(chain.invoke({"text":input_text}))