import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Labor für Umweltmesstechnik", page_icon=":earth_americas:", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")

# Lottie Animation
plane = load_lottieurl("https://lottie.host/d99b0174-2d31-495e-84fc-58699c143c13/BvjiHLrA6L.json")
lottieMeasure = load_lottieurl("https://lottie.host/0d793123-abf8-4279-8c0f-4b1d5bf74c20/8AP9ngMh7w.json")
img_brenk = Image.open("images/Formation.jpg")
img_mess1 = Image.open("images/Messkampagne1.jpg")

# Header Section
with st.container():
    st.subheader("Labor für Umweltmesstechnik")
    st.title("Willkommen im Labor für Umweltmesstechnik")
    st.write("Wir sind ein Labor der Hochschule Düsseldorf und beschäftigen uns mit der Messung von Umweltparametern.")
    st.write("[Lerne mehr>](https://mv.hs-duesseldorf.de/studium/fachgebiete/physik_und_umwelttechnik/Seiten/default.aspx)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Messungen")
        st.write("##")
        st.write("Hier finden Sie die Ergebnisse der Messungen des Labor für Umweltmesstechnik der Hochschule Düsseldorf.")
        st.write("[Ergebnisse>](https://mv.hs-duesseldorf.de/studium/fachgebiete/physik_und_umwelttechnik/ver%C3%B6ffentlichungen)")
    with right_column:
        st_lottie(lottieMeasure, height=300, key="measure")

with st.container():
    st.write("---")
    st.header("Unsere Projekte")
    st.write("##")
    st.write("Hier finden Sie eine Übersicht über unsere Projekte.")
    st.write("[Lerne mehr>](https://mv.hs-duesseldorf.de/)")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_brenk)
    with text_column:
        st.subheader("Troposphärenforschung")
        st.write(
            """
            Das Team des Labors für Umweltmesstechnik der HSD und die Firma Brenk Systemplanung, beauftragt durch das Bundesamt für Strahlenschutz, haben im Rahmen eines laufenden Forschungsprojektes die ersten Untersuchungen einer Untersuchungsreihe zur Ausbreitung eines Tracerstoffes in der Atmosphäre durchgeführt.​​
            """
        )
        st.markdown("[Erfahre mehr...](https://mv.hs-duesseldorf.de/aktuelles/meldungen/20230906-troposph%C3%A4renforschung-made-in-nrw?showarrows=1&sid=bfz1tmacwrno1ywxfvz12rn0)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_mess1)
    with text_column:
        # write something about this project with a header: https://mv.hs-duesseldorf.de/aktuelles/meldungen/20230420_messkampagne?showarrows=1&sid=bfz1tmacwrno1ywxfvz12rn0
        st.subheader("Messkampagne")
        st.write(
            """
            ​​2022 hat das Labor für Physik und Umweltmesstechnik die Messung von Schadstoffen mit Hilfe von Drohnen erfolgreich ausgebaut und war europaweit an Industriestandorten zur Bestimmung diffuser Quellen im Einsatz. 
            """
        )
        st.markdown("[Erfahre mehr...](https://mv.hs-duesseldorf.de/aktuelles/meldungen/20230420_messkampagne?showarrows=1&sid=bfz1tmacwrno1ywxfvz12rn0)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/marcel.oliveirabrito@hs-duesseldorf.de" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()