import streamlit as st
st.set_page_config(
    page_title="streamlit dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)
st.title("main page")


if "input" not in st.session_state:
    st.session_state["input"]=""
    
    input=st.text_input("please enter a text", st.session_state["input"])
    submit=st.button("submit")
