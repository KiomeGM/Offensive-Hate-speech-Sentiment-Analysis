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
         
with tab2:
   st.write(f"""
            Offensive language and hate speech linked to a global increase in violence toward minorities.\n
            Social media companies and governments have unfortunately been forced to impose limitations to freedom of speech.\n
            We aim to provide a preventive measure that will proactively sustain harmony in the social circles.\n
            """)
   st.header("The Visionaries")
   
   imageCarouselComponent = components.declare_component("image-carousel-component", path="app/")

   imageUrls = [
      "https://images.unsplash.com/photo-1522093007474-d86e9bf7ba6f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
      "https://images.unsplash.com/photo-1610016302534-6f67f1c968d8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1075&q=80",
      "https://images.unsplash.com/photo-1516550893923-42d28e5677af?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=872&q=80",
      "https://images.unsplash.com/photo-1541343672885-9be56236302a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
      "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
      "https://images.unsplash.com/photo-1528728329032-2972f65dfb3f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
      "https://images.unsplash.com/photo-1557744813-846c28d0d0db?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1118&q=80",
      "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
      "https://images.unsplash.com/photo-1595867818082-083862f3d630?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
      "https://images.unsplash.com/photo-1622214366189-72b19cc61597?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
      "https://images.unsplash.com/photo-1558180077-09f158c76707?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
      "https://images.unsplash.com/photo-1520106212299-d99c443e4568?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
      "https://images.unsplash.com/photo-1534430480872-3498386e7856?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
      "https://images.unsplash.com/photo-1571317084911-8899d61cc464?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
      "https://images.unsplash.com/photo-1624704765325-fd4868c9702e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
    ]
   selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)

   if selectedImageUrl is not None:
      st.image(selectedImageUrl)
   # col1, col2, col3, col4 = st.columns(4, gap = "small")
   
   # with col1:
   #    st.image()
   #    st.write(f"""
            
   #          """)
      
      
   
   

