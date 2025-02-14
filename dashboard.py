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






    ---
    """, unsafe_allow_html=True)
    st.header(":mailbox: Get in touch / Feedback")



    contact_form2= """<style>
    .contact-form {
    max-width: 400px;
    margin: 20px 0;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  .contact-form label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
  }
  .contact-form input,
  .contact-form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
  }
  .contact-form button {
    width: 100%;
    padding: 10px;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    transition: background 0.3s;
  }
  .contact-form button:hover {
    background: #0056b3;
  }
</style>

<form class="contact-form" action="https://formspree.io/f/xqaedrjr" method="POST" style="text-align: left;">
  <label>Your email:
    <input type="email" name="email" required>
  </label>
  <label>Your message:
    <textarea name="message" required></textarea>
  </label>
  <button type="submit">Send</button>
</form>

"""

    st.markdown(contact_form2, unsafe_allow_html=True)
    