import streamlit as st
import requests



from dotenv import load_dotenv
import os

load_dotenv()
access_key = os.getenv("UNSPLASH_API_KEY")





st.title("🌈Image Generator ")
st.write("Type any keyword(like nature , mountain,laptop, phone,cars,toys) to see top  images:")
keyword = st.text_input("Enter any keyword","Nature")
per_page = st.slider("Number of images", 1, 10, 5)
is_button_click= st.button("Search")

if is_button_click:
    if not keyword:
        st.warning("Please enter any keyword")
    else :
        url= f"https://api.unsplash.com/search/photos?per_page={per_page}&query={keyword}&client_id={access_key}"
        with st.spinner('Fetching images...'):
             response= requests.get(url)
        status=response.status_code
        if status==200:
            data= response.json()
            results= data ["results"]
            if len (results)==0:
                st.warning("No image found!")
            else :
                for dic in results:
                    url= dic ["urls"]["small"]
                    st.image(url)  
            
        else:
            st.error("Something went wrong !!")