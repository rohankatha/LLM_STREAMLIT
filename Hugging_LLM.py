from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
import streamlit as st


#HF_TOKEN = OS.GET_TOKEN()


st.title("Image to text converter")
inoput = st.text_input(placeholder="Enter the prompt :) ",label="LLMPROMPT")
huggin_token = st.sidebar.text_input("Enter the Hugging face token")
model = InferenceClient(api_key=huggin_token)
if inoput:
 Img = model.text_to_image(inoput,model="black-forest-labs/FLUX.1-dev")
 string_name = inoput+".png"
 #Img.save(fp=string_name)
 st.image(Img)
