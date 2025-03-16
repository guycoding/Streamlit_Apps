import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from streamlit import columns, button

otc_acute_conditions = [
    "Headache",
    "Muscle pain",
    "Back pain",
    "Toothache",
    "Menstrual cramps",
    "Fever",
    "Common cold",
    "Sore throat",
    "Cough",
    "Nasal congestion",
    "Sinus pressure",
    "Allergies",
    "Heartburn",
    "Indigestion",
    "Nausea",
    "Diarrhea",
    "Constipation",
    "Minor cuts and scrapes",
    "Insect bites",
    "Sunburn",
    "Minor burns",
    "Athlete's foot",
    "Itching",
    "Hemorrhoids",
    "Mild acne",
    "Motion sickness",
    "Insomnia"
]
otc_conditions_with_sa_brands = {
    "Headache": ["Panado", "Grand-Pa", "Adco-Dol"],
    "Muscle pain": ["Mybulen", "Cataflam", "Voltaren Gel"],
    "Back pain": ["Mybulen", "Cataflam", "Voltaren Gel"],
    "Toothache": ["Panado", "Adco-Dol", "Dentapain Gel"],
    "Menstrual cramps": ["Mybulen", "Cataflam", "Ponstan"],
    "Fever": ["Panado", "Grand-Pa", "Adco-Dol"],
    "Common cold": ["Benylin Cold & Flu", "Corenza C", "Sinutab"],
    "Sore throat": ["Strepsils", "Protex Lozenges", "Betadine Sore Throat Gargle"],
    "Cough": ["Benylin Dry Cough", "Broncleer Cough Syrup", "Tixylix Cough Syrup"],
    "Nasal congestion": ["Iliadin Nasal Spray", "Sinutab", "Drixine Nasal Spray"],
    "Sinus pressure": ["Sinutab", "Corenza C", "Panado Sinus"],
    "Allergies": ["Allergex", "Zyrtec", "Telfast"],
    "Heartburn": ["Gaviscon", "Rennie", "Eno"],
    "Indigestion": ["Gaviscon", "Rennie", "Eno"],
    "Nausea": ["Valoid", "Stemetil", "Ginger T"],
    "Diarrhea": ["Imodium", "Rehidrat", "Enterogermina"],
    "Constipation": ["Laxette", "Durolax", "Lactulose"],
    "Minor cuts and scrapes": ["Savlon Antiseptic Cream", "Dettol Antiseptic Liquid", "Elastoplast Plasters"],
    "Insect bites": ["Eurax Cream", "Tabard Roll-On", "Calamine Lotion"],
    "Sunburn": ["E45 Cream", "Nivea Sun After Sun Lotion", "Calamine Lotion"],
    "Minor burns": ["Burnshield", "E45 Cream", "Savlon Antiseptic Cream"],
    "Athlete's foot": ["Canesten Cream", "Daktarin Cream", "Lamisil Cream"],
    "Itching": ["Eurax Cream", "Calamine Lotion", "Aveeno Anti-Itch Cream"],
    "Hemorrhoids": ["Proctosedyl Ointment", "Anusol Cream", "Preparation H"],
    "Mild acne": ["Epiduo Gel", "Acne-Aid Soap", "Clearasil Cream"],
    "Motion sickness": ["Valoid", "Stugeron", "Ginger T"],
    "Insomnia": ["Dormeasan", "Sedaplus", "Calmsure"]
}



df = pd.DataFrame(otc_conditions_with_sa_brands)

img = Image.open("v793-ning-06.jpg")
st.title("OTC BUDDY")
st.image(image=img, width=50)
def Login():
    st.write("Login")
    c1,c2 = st.columns(2)
    user_name= c1.text_input("User Name".lower(),placeholder="user_Name")
    password = c2.text_input("Password",type = "password", placeholder="password")
    if st.button("login"):
        if user_name == "admin".lower() and password =="2025":
            st.session_state.logged_in = True
            st.success("logged in")
        else:
            st.error("wrong user name or password")
def log_out():
    if st.button("log out"):
        st.session_state.logged_in =False


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if st.session_state.logged_in:
    with st.sidebar:
        st.title("OTC BUDY")
        st.image(image=img, width=50)
        conditions = st.multiselect("Your Condition", otc_acute_conditions)
        button = st.button("Confirm")
        log_out()
        st.info("created by charles, github account : guycoding")
    if button:
        if conditions:
            for condition in conditions:
                st.subheader(f"Medications for {condition}:")
                medications = df[condition].to_list()
                if medications:
                    st.dataframe(pd.DataFrame(medications, columns=[""]),hide_index=True)
                else:
                    st.warning(f"No medications found for {condition}.")
        else:
            st.warning("Please select at least one condition.")

else:
    Login()
