import streamlit as st

import requests
import base64

# Replace with your Spotify credentials
CLIENT_ID = st.secrets['CLIENT_ID']
CLIENT_SECRET = st.secrets['CLIENT_SECRET']

# Warning/Disclaimer Component
def show_disclaimer():
    st.markdown("""
    <style>
    .warning-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #fff3cd;
        border: 1px solid #ffeeba;
        margin-bottom: 1rem;
    }
    .warning-title {
        color: #856404;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .warning-text {
        color: #856404;
    }
    </style>
""", unsafe_allow_html=True)
    st.markdown("""
        <div class="warning-box">
            <div class="warning-title">⚠️ Important Disclaimer</div>
            <div class="warning-text">
                This website provides educational resources and support information only. It is not a substitute for professional medical advice, diagnosis, or treatment. If you're experiencing a mental health emergency, please contact emergency services or visit your nearest emergency room immediately.
                <br><br>
                Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
            </div>
        </div>
    """, unsafe_allow_html=True)





# Function to get access token
def get_access_token():
    auth_url = "https://accounts.spotify.com/api/token"
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    response = requests.post(auth_url, headers=headers, data=data)
    response_data = response.json()
    
    return response_data.get("access_token")

# Function to get podcast (show) details
@st.cache_resource(ttl=4800)
def get_podcast_info(show_id):
    access_token = get_access_token()
    if not access_token:
        print("Failed to retrieve access token.")
        return

    url = f"https://api.spotify.com/v1/shows/{show_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Example: Replace with your podcast's show ID
# show_id = "6t3lS8pB0XK9OyErfXS5aJ"  # Example show ID
# podcast_info = get_podcast_info(show_id)

# if podcast_info:
#     print("Podcast Name:", podcast_info["name"])
#     print("Publisher:", podcast_info["publisher"])
#     print("Description:", podcast_info["description"])
#     print("Total Episodes:", podcast_info["total_episodes"])
