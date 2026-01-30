import streamlit as st
import pandas as pd

st.set_page_config(page_title="LB dashboard",layout="centered")

st.title("Welcome to streamlit")
st.write("Hello...userA")

Embed_model = st.text_input("Enter your Embedding model name:")
if Embed_model:
	st.write(f"Input model name is:{Embed_model}")

llm_model = st.text_input("Enter your llm model name:")
if llm_model:
	st.success(f"Input model name is:{llm_model}")


vector = st.slider("Select your vector range:")
if vector:
	st.write(f"selected vector range:{vector}")

vector = st.slider("Select your vector range:",500,1000)
if vector:
	st.write(f"selected vector range:{vector}")


vector = st.slider("Select your vector range:",5000,6000,5560)
if vector:
	st.write(f"selected vector range:{vector}")


st.select_slider("select your rate:",["Bad","Good","Excellent"])
st.selectbox("Select your model:",["gpt4.0","gpt5.0","lamma","gemma2:2b"])

st.multiselect("Select your model:",["gpt4.0","gpt5.0","lamma","gemma2:2b"])


file = st.file_uploader('select your input file:')
if file:
	st.success(f'Input file:{file.name} is loaded')
	df = pd.read_csv(file)
	st.write(df)

age = st.number_input('Enter your age:',5,90)
st.write(age)

st.checkbox("yes")
st.checkbox("no")

st.button("Click Me")
st.radio("Select your interface:",['eth0','eth1','eth2'])
st.date_input('Travel date:')



