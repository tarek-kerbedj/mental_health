import streamlit as st
from streamlit_option_menu import option_menu
from Anxiety import anxiety
from Depression import depression
from Miscellaneous import miscellaneous
from utils import show_disclaimer

st.set_page_config(page_title=None,page_icon=None, layout="wide")
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
elif selected_main=="Miscellaneous":
    miscellaneous()

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
    All of the resources were **manually curated** to make sure that they follow best practices, in addition to other factors such as :
    - Personal experience
    - High praise from listeners and therapists alike
    - Approachability

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
    st.header(":mailbox: Get In Touch With Me!")


    # contact_form = """
    # <form action="https://formsubmit.co/e76bae1b49ba1ef7b9c9d80a1c74fcb6 " method="POST">
    #     <input type="hidden" name="_captcha" value="false">
    #     <input type="text" name="name" placeholder="Your name" required>
    #     <input type="email" name="email" placeholder="Your email" required>
    #     <textarea name="message" placeholder="Your message here"></textarea>
    #     <button type="submit">Send</button>
    # </form>
    # """
    contact_form2="""
<form
  action="https://formspree.io/f/xqaedrjr" method="POST">
  <label>
    Your email:
    <input type="email" name="email">
  </label>
  <label>
    Your message:
    <textarea name="message"></textarea>
  </label>
  <!-- your other form fields go here -->
  <button type="submit">Send</button>
</form>"""

    st.markdown(contact_form2, unsafe_allow_html=True)

    # # Use Local CSS File
    # def local_css(file_name):
    #     with open(file_name) as f:
    #         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#     local_css("style/style.css")
    with st.form("contact form"):
        title = st.text_input('title')
        email=st.text_input('email')
        content = st.text_area('content')
        
        st.form_submit_button('Submit')



 
    