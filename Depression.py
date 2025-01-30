import streamlit as st
from streamlit_option_menu import option_menu

def depression():
    st.title('Depression Resources')
    depression_submenu = {
        "Depression": ["Overview", "Podcasts", "Youtube channels", "Books"]
    }


        
    selected_submenu = option_menu(
            None,
            depression_submenu["Depression"],
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa", "margin": "0px"},
                "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#90EE90"},
            }
        )