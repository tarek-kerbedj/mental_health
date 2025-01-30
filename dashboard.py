import streamlit as st
from streamlit_option_menu import option_menu
from Anxiety import anxiety
from Depression import depression
from utils import show_disclaimer

# Show disclaimer at the top of every page
show_disclaimer()
# Main navigation
selected_main = option_menu(
    None,
    ["Home","Miscellaneous", "Anxiety", "Depression", 'FAQ'],
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)


# Show submenu based on main selection
if selected_main == "Anxiety":
    anxiety()


elif selected_main == "Depression":
    depression()

elif selected_main == "Home":
    st.title('Overview')
    st.write('This website includes a curated list of **verified** resources to help you deal with a variety of mental health issues')



elif selected_main == "FAQ":

 

    st.markdown("""
    # ❓ Frequently Asked Questions (FAQ)

    ### 🔹 Why aren't there more resources?
    The decision to limit the amount of resources was deliberate, overwhelming people with choices is only going to prevent them from getting the help that they need
    \n\n see **[Choice Overload](https://thedecisionlab.com/biases/choice-overload-bias)**
    ### 🔹 What's the thought process behind picking these resources?
    We currently support:
    - **Excel (.xlsx, .xls)**
    - **CSV (.csv)**
    - **JSON (.json)**

    ### 🔹 How do I extract podcast details?
    1. Enter the **Spotify Show ID**.
    2. Click the **Fetch Details** button.
    3. View the **podcast name, description, and hosts**.

    ### 🔹 Can I download the processed data?
    Yes! After processing, you can **download the modified file** by clicking the **Download** button.

    ### 🔹 Who can I contact for support?
    If you need help, please reach out via **email** or our **support chat**.

    ---
    """, unsafe_allow_html=True)

    #st.write(" Q1) **Why isnt there a lot of resources?**")
    