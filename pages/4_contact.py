import streamlit as st


st.markdown(
    """
    <style>
        .my-text {
            font-size: 14px;
            font-family: monospace;
        }
    </style>
    <div class="my-text">
        Contact: 
        <br>
        <a href="mailto:new.music.playlist.tracker@gmail.com">new.music.playlist.tracker@gmail.com</a>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("")
st.write("")
st.link_button(label='Github', url='https://github.com/amcl11/spotify_au_release_app')