# run this code using this command
# streamlit run real_front_end.py --server.baseUrlPath /.streamlit/config.toml

import streamlit as st
import json
import streamlit.components.v1 as components
# Initialize a session state variable for page management and interests
import streamlit.components.v1
import warnings
from streamlit_lottie import st_lottie
import json
# Suppress the specific warning related to calling st.rerun() within a callback
warnings.filterwarnings('ignore', message="calling st.rerun() within a callback is a no-op")


if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'interests' not in st.session_state:
    st.session_state.interests = []
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1

# Function to create an iframe embedding a website
def create_website_iframe(url, width=100, height=300):
    iframe = f"""
    <iframe src="{url}" width="{width}%" height="{height}px" frameborder="0" allowfullscreen></iframe>
    """
    return iframe


def load_lottiefile(filepath: str):
    """ Load a Lottie animation from a JSON file located at filepath """
    with open(filepath, 'r') as file:
        return json.load(file)



def embed_website(url):
    iframe_style = """
    <style>
    .scrolling-wrapper {
        width: 100%;
        height: 600px; /* Set the desired height for the scrollable iframe */
        overflow-y: auto; /* Enable vertical scrollbar */
        border: 1px solid #ddd; /* Optional: Add border for visual clarity */
    }
    </style>

    """

    st.markdown(iframe_style, unsafe_allow_html=True)
    # st.markdown('<div class="scrolling-wrapper"><iframe src="https://en.wikipedia.org/wiki/Main_Page" width="100%" height="100%"></iframe></div>',unsafe_allow_html=True)
    st.markdown(
        f'<div class="scrolling-wrapper"><iframe src="{url}" width="100%" height="100%"></iframe></div>',
        unsafe_allow_html=True)

def main():

    # Home page
    if st.session_state.page == 'home':
        st.title("Buzz Feeds.AI")

        lottie_animation_path = "assets/Animation - 1714618233102.json"
        lottie_animation = load_lottiefile(lottie_animation_path)


        st_lottie(lottie_animation,height=300, width=600, key="example")
        st.markdown("""
            ### Use the buttons below to navigate through the application.
            """, unsafe_allow_html=True)


        # Input field for customer ID
        customer_id = st.text_input("Customer ID", "")

        # Manage input for interests with a key to manage its state
        if 'interest_input' not in st.session_state:
            st.session_state.interest_input = ""
        interest_input = st.text_input("Enter Interest", key="interest_input", value=st.session_state.interest_input)

        # Function to add interests to the list
        def add_interest():
            if interest_input:
                st.session_state.interests.append(interest_input)
                # Clear the interest input field after adding
                st.session_state.interest_input = ""
                st.experimental_rerun()

        # Button to add interests
        st.button("Add Interest", on_click=add_interest)

        # Display the interests in green boxes within 4 columns
        cols_per_row = 4
        rows = [st.columns(cols_per_row) for _ in range((len(st.session_state.interests) + cols_per_row - 1) // cols_per_row)]
        for index, interest in enumerate(st.session_state.interests):
            col = rows[index // cols_per_row][index % cols_per_row]
            with col:
                st.markdown(f"<div style='background-color: #76c7c0; padding: 5px; border-radius: 5px; display: inline-block;'>{interest} <span style='cursor: pointer;' onclick='window.location.reload();'>❌</span></div>", unsafe_allow_html=True)

        # Button to submit and navigate to the second page
        if st.button("Submit"):

            # send the data to back end from here
            if customer_id and st.session_state.interests:
                # Serialize and save data to a JSON file
                data = {
                    "customer_id": customer_id,
                    "interests": st.session_state.interests
                }
                with open('customer_data.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)



            else:
                st.error("Please fill in the customer ID and add at least one interest.")
            if customer_id and st.session_state.interests:
                st.session_state.page = 'second'

            st.experimental_rerun()

    # Second page
    elif st.session_state.page == 'second':

        st.set_page_config(layout="wide")
        st.title("Featured Videos")

        # Function to load video links from a file and display them
        def display_category_videos(category_name, file_name):
            st.header(category_name)

            # Read video links from the text file
            with open(file_name, 'r') as file:
                video_links = [link.strip() for link in file.readlines()]

            # Define the number of columns
            cols = st.columns(4)  # Creates 4 columns

            # Pagination logic
            num_columns = 4
            num_videos = len(video_links)
            num_pages = (num_videos - 1) // num_columns + 1

            # Ensure each category has its own page tracking
            if f'current_page_{category_name}' not in st.session_state:
                st.session_state[f'current_page_{category_name}'] = 1

            start_index = (st.session_state[f'current_page_{category_name}'] - 1) * num_columns
            end_index = min(start_index + num_columns, num_videos)

            # Display videos for the current page
            for index in range(start_index, end_index):
                with cols[index % num_columns]:
                    st.markdown(
                        f"""
                        <iframe width="100%" height="250px" src="{video_links[index].replace('watch?v=', 'embed/')}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                        """,
                        unsafe_allow_html=True
                    )
                    # Button for internal navigation
                    if st.button("View Section", key=f'view_{category_name}_{index}'):
                        st.session_state.page = 'third'
                        st.experimental_rerun()



            # Pagination controls
            if num_pages > 1:
                st.write("")  # Add some space between videos and pagination controls
                if st.session_state[f'current_page_{category_name}'] > 1:
                    if st.button("Previous", key=f'prev_{category_name}'):
                        st.session_state[f'current_page_{category_name}'] -= 1
                        st.experimental_rerun()
                if st.session_state[f'current_page_{category_name}'] < num_pages:
                    if st.button("Next", key=f'next_{category_name}'):
                        st.session_state[f'current_page_{category_name}'] += 1
                        st.experimental_rerun()

        # Display categories
        display_category_videos("Featured Videos", "videos.txt")
        display_category_videos("Interest 1", "videos.txt")
        # display_category_videos("Interest 2", "interest2.txt")
        # display_category_videos("Interest 3", "interest3.txt")


# Assume this is part of the logic handling page 'third'

    elif st.session_state.get('page') == 'third':
        st.set_page_config(layout="wide")  # Set the layout to "wide"

        col1, col2 = st.columns([1, 1])  # Create columns

        with col1:
            st.subheader("Embedded Website")
            embed_website(url = 'https://www.wired.com/2017/08/instagram/')

        with col2:
            st.header("Chat with Us")
            chat_input = st.text_input("", placeholder="Type your message here...", key="chat_input")

            # Layout for Send and Clear Chat buttons
            col_send, col_clear = st.columns(2)
            with col_send:
                if st.button("Send", key="send_button"):
                    # Append user's question to the chat history
                    response = "Hello, how are you doing?"
                    if "chat_history" not in st.session_state:
                        st.session_state.chat_history = []
                    st.session_state.chat_history.append(f"You: {chat_input}")
                    st.session_state.chat_history.append(f"Response: {response}")
            with col_clear:
                if st.button("Clear Chat", key="clear_chat"):
                    # Clear the chat history
                    st.session_state.chat_history = []

            # Display chat history
            if "chat_history" in st.session_state:
                for index, chat in enumerate(st.session_state["chat_history"]):
                    # Alternate color for user and response
                    color = "#e1f5fe" if "You:" in chat else "#e0e0e0"
                    st.markdown(
                        f"<div style='background-color: {color}; padding: 10px; border-radius: 5px; margin: 5px 0;'>{chat}</div>",
                        unsafe_allow_html=True)

            if st.button("Back to Second Page", key="back_to_second"):
                st.session_state.page = 'second'
                st.experimental_rerun()

if __name__ == "__main__":
    main()


