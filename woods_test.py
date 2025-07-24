import streamlit as st
import random

st.title("프랭크 우즈와의 즐거운(?) 대화")

lst = [
    "지랄, 내 계획은 항상 개쩌는 거 몰라?",
    "쳐맞고 말할래, 그냥 말할래!",
    "난 다양한 매력이 있다고. 알잖아?",
    "유령 같은 새끼",
    "들었어? 벨이 우리 보고 전설이래."
    
]






name = st.text_input("당신의 이름을 알려주세요.")

if st.button("우즈에게 말 걸기"):
    if name == "허드슨":
        st.info(f"{name}에게: {random.choice(lst[:2])}")
    elif name == "메이슨":
        st.info(f"{name}에게: {random.choice(lst[2:])}")
    elif name == "벨":
        st.error(f"{name}에게: 이게 누구야, 애들러의 수제자네.")
    else:
        st.info(f"{name}에게: 뭐야? 할 얘기 있으면 메이슨한테 전달해.")

