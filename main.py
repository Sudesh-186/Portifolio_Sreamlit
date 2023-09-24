from pathlib import Path
import requests
import streamlit as st
# from streamlit_lottie import st_lottie
from PIL import Image

#----General Settings----
page_title = 'Portifolio | Sudesh V'
page_icon = ':wave:'
name = 'Sudesh'
Email = 'sudesh.mailin@gmail.com'
description = '''
Web developer in Python using Flask and Streamlit.
Can write code for web scrapping and automation.
'''

#----Page Layout----
st.set_page_config(page_title= page_title, page_icon=page_icon)

#----Lottie Load Function----
def load_lottie_url(url):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

#----Path Settings----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
my_pic = current_dir / "assets" / "profile_pic.png"

#----Load Profile Pic, Lottie, Local CSS----
my_pic = Image.open(my_pic)
lottie_file = load_lottie_url('https://lottie.host/d3a7d1a5-b2a7-49ac-90bf-292ae2e70004/eD65SoWc1u.json')

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# local_css("style/style.css")

#----About Me----
with st.container():

	col1, col2 = st.columns([0.3,0.7])

	with col1:
		st.image(my_pic)

	with col2:
		st.title(f"Hi, I'm {name} :wave:")
		st.write(description)
		st.write(':email:', Email)

#----What can I do----
with st.container():
	st.write('---')
	col1, col2 = st.columns(2)
	with col1:
		st.header('What Can I Do')
		st.write('##')
		st.write(
			'''
			- Web Development using Flask and Streamlit dataframes.
			- Extract data from a website using web scraping and save that data with python.
			- Create a Discord bot using python.
			- Create workflow automations.
			'''
			)
	with col2:
		st.empty()
		# st_lottie(lottie_file, height=300, key='coding')

#----My Projects----
with st.container():
	st.write('---')
	st.header('My Projects')
	st.write('##')
	#----Remove this tag & create columns----

#----Contact Form----
with st.container():
	st.write('---')
	st.header('Get In Touch!')
	st.write('##')

	#----https://formsubmit.co/ Change Email----
	contact_form = '''
	<form action="https://formsubmit.co/sudesh.mailin@gmail.com" method="POST">
		<input type="hidden" name="_captcha" value="false">
		<input type="text" name="name" placeholder="Your Name" required>
		<input type="email" name="email" placeholder="Your Email" required>
		<textarea name="message" placeholder="Type Your Messsage Here!" required></textarea>
		<button type="submit">Send</button>
</form>
'''

col1, col2 = st.columns(2)
with col1:
	st.markdown(contact_form, unsafe_allow_html=True)
with col2:
	st.empty()
