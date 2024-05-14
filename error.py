import streamlit as st

# Custom CSS
with open('style.css') as f:  # Change 'styles.css' to 'style.css'
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

## LOGO and TITLE
## -------------------------------------------------------------------------------------------
# Show the logo and title side by side
col1, col2 = st.columns([1, 4])
with col1:
    st.image("AIEMOTBOT.png", width=100)  # Change 'brainbot.png' to 'AIEMOTBOT.png'
with col2:
    st.title("Error")

st.error("Oops - Something went wrong! Please try again.")
