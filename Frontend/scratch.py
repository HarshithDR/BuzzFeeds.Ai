import streamlit as st

def main():
    st.title("Embedding Wikipedia with Scroll")

    # Custom CSS to style the iframe for scrollability
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

    # Embed a webpage using components.iframe with custom CSS
    st.markdown(iframe_style, unsafe_allow_html=True)
    st.markdown('<div class="scrolling-wrapper"><iframe src="https://en.wikipedia.org/wiki/Main_Page" width="100%" height="100%"></iframe></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()