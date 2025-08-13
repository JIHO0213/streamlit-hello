import streamlit as st

st.title("3715 정지호")
st.write("Hello, world!")

st.write("우리 함께 **스트림릿**을 :red[배워] 봅시다.")

hello=st.button("hello!")
bye=st.button("Bye!")
if bye:
    st.write("잘가요~")
else:
    st.write("안녕하세요~!")