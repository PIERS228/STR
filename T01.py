import streamlit as st

# 設置頁面標題
st.title("簡單的 Streamlit 網站")

# 添加一個輸入框，讓用戶輸入文本
user_input = st.text_input("請輸入一些文本：HAHAHAHAHA")

# 顯示用戶輸入的文本
st.write("你輸入的文本是：YEAH", user_input)

# 顯示文本的長度
st.write("文本的長度是：", len(user_input))
