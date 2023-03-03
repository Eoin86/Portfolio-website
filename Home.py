import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Eoin Mahon")
    content = '''I'm relatively new to software development and I'm using this to try get the hang of python.
    Other languages I've used are C, C#, Java and SQL.'''
    st.info(content)

content2 = '''<b>Below you can find some apps I have built in Python. Feel free to contact me</b>'''
st.write(content2, unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")