import streamlit as st
from components.add_copy_button import add_copy_button

st.title('Copy to Clipboard Example')

text_to_copy = st.text_area("Set Text to Copy:", "This is the text to be copied to the clipboard.", height=150)

container = st.container(border=True)
container.text(text_to_copy)

add_copy_button(text_to_copy)