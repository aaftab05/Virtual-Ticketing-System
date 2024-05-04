import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Way",page_icon=":ticket:",layout="wide") 


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_booking = load_lottieurl("https://lottie.host/d1554c2e-2f1e-49d9-b789-91e5486ddffe/9UuIyMJtSP.json")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("<mark>Virtual Ticketing System</mark>", unsafe_allow_html=True)
        st.title("My Way :ticket:")
        st.write('''Welcome to My Way,
                    A virtual ticketing system developed by 4 students of Ballari Institute of Technology and Management
                    who are as of 2024 in their 2nd year pursuing AI & ML.
                    This is a project we were asked to develop as a part of our internship program under the guidance of 
                    Mr Bijen Singha Sir. 
                    This project is purely based on python and use of streamlit for the UI and deployment.
                    ''')
        st.divider()
    with right_column:
        st_lottie(lottie_booking, height=300, key="booking")


st.write("[GitHub link >](https://github.com/aaftab05/Virtual-Ticketing-System)")
st.divider()
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.markdown("<mark>:mailbox: Get in touch with us</mark>", unsafe_allow_html=True)
contact_form='''
<form action="https://formsubmit.co/aaftabzohra@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>'''
st.markdown(contact_form,unsafe_allow_html=True)


# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")