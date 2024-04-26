import streamlit as st
import json

# Initialize a session state variable for page management and interests
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'interests' not in st.session_state:
    st.session_state.interests = []

def main():
    # Home page
    if st.session_state.page == 'home':
        st.title("Customer Interest Form")

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
            # print("submitted")
            # if customer_id and st.session_state.interests:
            #     st.session_state.page = 'second'
            #     # Optionally store or process the data here
            #     if customer_id and st.session_state.interests:
            #         data = {
            #             "customer_id": customer_id,
            #             "interests": st.session_state.interests
            #         }
            #         st.write("JSON Output:")
            #         st.json(data)


            # else:
            #     st.error("Please fill in the customer ID and add at least one interest.")
            if customer_id and st.session_state.interests:
                st.session_state.page = 'second'
    # Second page
    elif st.session_state.page == 'second':

        st.title("Hello World")
        # st.write("Here is a video from YouTube:")
        # # YouTube video URL
        # video_url = 'https://www.youtube.com/watch?v=cw34KMPSt4k'
        # # Embed YouTube video
        # st.video(video_url)



if __name__ == "__main__":
    main()
