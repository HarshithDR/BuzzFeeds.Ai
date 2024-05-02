# run this code using this command
# streamlit run real_front_end.py --server.baseUrlPath /.streamlit/config.toml
base_path = "C:/Users/amith/Downloads/Google Hack/GoogleAIHackathon/"

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
import requests

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'interests' not in st.session_state:
    st.session_state.interests = []
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1


cust_id = []



def send_question(question):
    url = 'http://127.0.0.1:5001/chat_query'  # Adjust the URL/port as necessary
    response = requests.post(url, json={"question": question})
    if response.status_code == 200:
        return response.json().get('Response', 'No response from server')
    else:
        return f"Error: {response.status_code} - {response.text}"






# Function to create an iframe embedding a website
def create_website_iframe(url, width=100, height=300):
    iframe = f"""
    <iframe src="{url}" width="{width}%" height="{height}px" frameborder="0" allowfullscreen></iframe>
    """
    return iframe


def send_customer_id(customer_id):
    news_feed_url = 'http://127.0.0.1:5001/newsfeed'
    response = requests.get(news_feed_url, params={"customer_id": customer_id})
    if response.status_code == 200:
        data = response.json()
        st.session_state.interests_data = data  # Store the data in session_state
        print("Output from the server:", data)
        return data
    else:
        print(f"Failed to retrieve data: {response.status_code} - {response.text}")
        return None



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


        st_lottie(lottie_animation,height=200, width=600, key="example")
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





        button_style = """
        <style>
        button {
            background-color: #4CAF50; /* Green background */
            color: white; /* White text */
            border: none;
            padding: 10px 20px; /* Top and bottom padding 10px, left and right padding 20px */
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            transition-duration: 0.4s;
            cursor: pointer;
            border-radius: 8px; /* Rounded corners */
        }
        button:hover {
            background-color: #45a049; /* Darker shade of green */
        }
        </style>
        """

        st.markdown(button_style, unsafe_allow_html=True)




        # Button to submit and navigate to the second page
        if st.button("Submit"):

            if customer_id and st.session_state.interests:
                # Join all interests in the list with a comma and a space
                formatted_interests = ", ".join(st.session_state.interests)

                # Creating the data dictionary
                data = {
                    "customer_id": customer_id,
                    "interests": formatted_interests
                }

                print("#"*100)
                print(data)
                cust_id.append(data["customer_id"])
                # URL to which the request will be sent
                interests_url = 'http://127.0.0.1:5001/interests'

                # Send a POST request
                response = requests.post(interests_url, json=data)

                # Check the response
                if response.status_code == 200:
                    print("Data successfully sent to the server!")
                else:
                    print(f"Failed to send data: {response.status_code} - {response.text}")



            else:
                st.error("Please fill in the customer ID and add at least one interest.")
            if customer_id and st.session_state.interests:
                st.session_state.page = 'second'

                #sending the id to newsfeed
                send_customer_id(cust_id[0])
                cust_id.pop()

                # print(cust_id)
            st.experimental_rerun()

    # Second page
    elif st.session_state.page == 'second':

        st.set_page_config(layout="wide")
        st.title("Buzz Feeds.AI")
        st.title("Your Feed")

        def display_category_videos():
            if 'interests_data' in st.session_state:
                for interest, videos in st.session_state.interests_data.items():
                    st.header(interest)  # Use the interest as a header
                    cols = st.columns(4)  # Assuming you want 4 columns of videos
                    for i, video_info in enumerate(videos):
                        video_path = base_path +video_info['video']
                        video_url = video_info['link']
                        with cols[i % 4]:
                            st.video(video_path)
                            if st.button('Watch on Website', key=f'btn_{interest}_{i}'):
                                st.session_state['video_url'] = video_url  # Store URL in session_state

                                video_id = video_info['dbid']
                                print(video_id)
                                url_source = 'http://127.0.0.1:5001/url_source'
                                data_id = {'id': video_id}

                                response = requests.post(url_source, json=data_id)
                                if response.status_code == 200:
                                    print("ID successfully sent to the server!")
                                    st.session_state.page = 'third'  # Navigate to the third page
                                    st.experimental_rerun()
                                    return response.json()
                                    # Or handle the response as needed
                                else:
                                    st.error(f"Failed to send ID: {response.status_code} - {response.text}")
                                    return None



                                # st.session_state.page = 'third'  # Navigate to the third page
                                # st.experimental_rerun()
            else:
                st.write("No video data available")

        # Function to load video links from a file and display them
        # def display_category_videos(category_name, file_name):
        #     st.header(category_name)
        #
        #     # Read video links from the text file
        #     with open(file_name, 'r') as file:
        #         video_links = [link.strip() for link in file.readlines()]
        #
        #     # Define the number of columns
        #     cols = st.columns(4)  # Creates 4 columns
        #
        #     # Pagination logic
        #     num_columns = 4
        #     num_videos = len(video_links)
        #     num_pages = (num_videos - 1) // num_columns + 1
        #
        #     # Ensure each category has its own page tracking
        #     if f'current_page_{category_name}' not in st.session_state:
        #         st.session_state[f'current_page_{category_name}'] = 1
        #
        #     start_index = (st.session_state[f'current_page_{category_name}'] - 1) * num_columns
        #     end_index = min(start_index + num_columns, num_videos)
        #
        #     # Display videos for the current page
        #     for index in range(start_index, end_index):
        #         with cols[index % num_columns]:
        #             st.markdown(
        #                 f"""
        #                 <iframe width="100%" height="250px" src="{video_links[index].replace('watch?v=', 'embed/')}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        #                 """,
        #                 unsafe_allow_html=True
        #             )
        #             # Button for internal navigation
        #             if st.button("View Section", key=f'view_{category_name}_{index}'):
        #                 st.session_state.page = 'third'
        #                 st.experimental_rerun()
        #
        #
        #
        #     # Pagination controls
        #     if num_pages > 1:
        #         st.write("")  # Add some space between videos and pagination controls
        #         if st.session_state[f'current_page_{category_name}'] > 1:
        #             if st.button("Previous", key=f'prev_{category_name}'):
        #                 st.session_state[f'current_page_{category_name}'] -= 1
        #                 st.experimental_rerun()
        #         if st.session_state[f'current_page_{category_name}'] < num_pages:
        #             if st.button("Next", key=f'next_{category_name}'):
        #                 st.session_state[f'current_page_{category_name}'] += 1
        #                 st.experimental_rerun()
        #
        # # Display categories
        display_category_videos()



# Assume this is part of the logic handling page 'third'

    elif st.session_state.get('page') == 'third':
        st.set_page_config(layout="wide")  # Set the layout to "wide"
        st.title("Buzz Feeds.AI")
        col1, col2 = st.columns([1, 1])  # Create columns

        with col1:
            st.subheader("Embedded Website")
            if 'video_url' in st.session_state:
                embed_website(url=st.session_state['video_url'])  # Embed the website using the stored URL
            else:
                st.write("No URL provided.")

        with col2:
            st.header("Chat with Us")
            chat_input = st.text_input("", placeholder="Type your message here...", key="chat_input")

            # Layout for Send and Clear Chat buttons
            col_send, col_clear = st.columns(2)
            with col_send:
                if st.button("Send", key="send_button"):
                    if chat_input:  # Ensure there is a question to send
                        response = send_question(chat_input)
                        if "chat_history" not in st.session_state:
                            st.session_state.chat_history = []
                        st.session_state.chat_history.append(f"You: {chat_input}")
                        st.session_state.chat_history.append(f"Response: {response}")
                    else:
                        st.error("Please enter a question.")



                # if st.button("Send", key="send_button"):
                #     # Append user's question to the chat history
                #     response = "Hello, how are you doing?"
                #     if "chat_history" not in st.session_state:
                #         st.session_state.chat_history = []
                #     st.session_state.chat_history.append(f"You: {chat_input}")
                #     st.session_state.chat_history.append(f"Response: {response}")
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






