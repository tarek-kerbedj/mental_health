import streamlit as st
import pandas as pd 
from streamlit_option_menu import option_menu
def anxiety():
    
    
    st.title('Anxiety Resources')
    podcasts_df = pd.read_excel('anxiety_resources.xlsx',sheet_name="podcasts",usecols=lambda col: col not in  ["Description","spotify_ids"])
    books_df= pd.read_excel('anxiety_resources.xlsx',sheet_name="Books")

    # Create submenu as a sidebar or secondary navigation

    anxiety_submenu = {
        "Anxiety": ["General Info", "Podcasts", "Youtube channels", "Books"]
    }
    selected_submenu = option_menu(
        None,
        anxiety_submenu["Anxiety"],
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa", "margin": "0px"},
            "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#90EE90"},  # Lighter green for submenu
        }
    )

    # Content based on submenu selection
    if selected_submenu == "General Info":
        st.write("General information about anxiety...")
    elif selected_submenu == "Podcasts":
        st.write("Podcasts that mainly discuss Anxiety and Anxiety disorders")
        st.table(podcasts_df)
        # Create a new column with the formatted links
        st.data_editor(
        podcasts_df,
        column_config={
            "Apple": st.column_config.LinkColumn(
                "Apple",
                help="Click to open the podcast link",
                validate="url",  # Try using the simpler 'url' validator
                display_text="Open Apple podcasts Link",
                max_chars=200,
            ),
            "Spotify": st.column_config.LinkColumn(
                "Spotify Link",
                help="Click to open the podcast link",
                validate=r"^https?://.*$",
                display_text="Open Spotify Link",
                max_chars=200,
            ),
      
        },use_container_width=True,
        hide_index=True,

)
    #     st.data_editor(
    #     podcasts_df,
    #     column_config={
    #         "Spotify": st.column_config.LinkColumn(
    #             "Spotify Link",
    #             help="Click to open the podcast link",
    #             validate=r"^https?://.*$",
    #             display_text="Open Spotify Link",
    #             max_chars=200,
    #         ),
    #         "Apple": st.column_config.LinkColumn(
    #             "Apple links",
    #             help="Click to open the podcast link",
    #             validate=r"^https?://.*$",  # Added validate parameter
    #             display_text="Open Apple Link",
    #             max_chars=200,  # Added max_chars parameter
    #         ),
    #     },
    #     hide_index=True,
    # )
  
    #     st.data_editor(
    #     podcasts_df,
    #     column_config={
    #         "Spotify": st.column_config.LinkColumn(
    #             "Spotify Link",
    #             help="Click to open the podcast link",
    #             validate=r"^https?://.*$",
    #             display_text="Open Spotify Link",  # Replace "PodcastName" with your actual column name
    #             max_chars=200,
    #         ),

    #         "Apple": st.column_config.LinkColumn(
    #         "Apple links",
    #         help="Click to open the podcast link",
    
    #         display_text="Open apple link"
    #     ),
    #     },
    #     hide_index=True,
    # )


    elif selected_submenu=="Books":
        st.write("Books that mainly discuss Anxiety and Anxiety disorders")
        #st.dataframe(books_df,hide_index=True)
        
# Use st.data_editor with correctly formatted LinkColumn
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
        hide_index=True,
    )
