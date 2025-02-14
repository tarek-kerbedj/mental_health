import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd 

def miscellaneous():
    yt_df = pd.read_excel('miscellaneous.xlsx',sheet_name="channels",usecols=lambda col: col not in  ["Description","spotify_ids"])
    books_df= pd.read_excel('miscellaneous.xlsx',sheet_name="Books")

    miscellaneous_submenu = {
        "miscellaneous": ["therapy websites", "Podcasts", "Youtube channels", "Books"]
    }


    selected_submenu = option_menu(
            None,
            miscellaneous_submenu["miscellaneous"],
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa", "margin": "0px"},
                "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#90EE90"},
            }
        )
    # Content based on submenu selection
    if selected_submenu == "Books":
        st.write("General information books / Self help")
        st.data_editor(
        books_df,
        column_config={
            "Link": st.column_config.LinkColumn(
                "Book Link",
                help="Click to open the book",
                validate=r"^https?://.*$",  # Accepts any valid HTTP/HTTPS link
                max_chars=200  # Allow longer URLs if needed
            )
        },
        use_container_width=True,
        hide_index=True,
    )
    elif selected_submenu == "Youtube channels":
        st.write("Youtube channels that discuss mental health in general")
        st.data_editor(
        yt_df,
        column_config={
            "Link": st.column_config.LinkColumn(
                "Channel Link",
                help="Click to open the book",
                validate=r"^https?://.*$",  # Accepts any valid HTTP/HTTPS link
                max_chars=200  # Allow longer URLs if needed
            )
        },
        use_container_width=True,
        hide_index=True,
    )
