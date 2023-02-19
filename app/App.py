import streamlit as st
import pandas as pd
import matplotlib
import streamlit.components.v1 as components

def add_bg_from_url():
    st.markdown(
         f"""
         <DOCTYPE html>
         <html lang='en'>
         <head>
            <meta charset='utf-8'>
            <title>HARMONeY</title>
         </head>
         <body>
            <p id="yKO2mWXkXTnECAKI" style="color:#008037;font-family:YAD-4Fp-fVw-0;line-height:1.4em;text-align:center;"><span id="Vu52fhCqoM983dXA" style="color:#008037;font-size:38px;">HARMONeY</span><br></p>
            <p id="fRhcZc0VZIRi1JHk" style="text-transform:uppercase;color:#008037;font-family:YAD-4Fp-fVw-0;line-height:1.4em;text-align:center;"><span id="aAQSols4Qb3di0LT" style="color:#008037;">BY STREAMLIT AI</span><br></p>
            <style>
               .stApp {{
                  background: rgba(0, 0, 0, 0);
                  background-attachment: fixed;
                  background-size: cover;
                  opacity: 1.0;
               }}
            </style>
         </body>
         </html>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

tab1, tab2 = st.tabs(['Detector','About'])

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 16px;
  background-color: white
}
</style>
"""
st.write(font_css, unsafe_allow_html=True)

with tab1:
      st.write("Will that text lead to social reproach? One way to find out:")
      col1, col2 = st.columns(2)
      with col1:
         with st.form('uploaded'):
            st.write('Select .txt file for upload:')
            st.file_uploader("Upload text",type = 'txt')
            submitted1 = st.form_submit_button("Submit")
      with col2:
         with st.form('inputted'):
            st.write('or just type that text here:')
            txt = st.text_input("Please input your text")
            submitted2 = st.form_submit_button("Submit")
      if submitted1:
         st.write("Greating")
      elif submitted2: 
         st.write("Greating again")
      
      
   
   

