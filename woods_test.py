import streamlit as st
import random

st.title("우즈에게 말을 걸어보자!")

lst_h = [
    "지랄, 내 계획은 항상 개쩌는 거 몰라?",
    "쳐맞고 말할래, 그냥 말할래!",
    "젠장, 개판을 쳐놓았구만."
]

lst_user = [
    "뭐야? 할 얘기 있으면 메이슨한테 전달해.",
    "지금은 바빠. 나중에.",
    "왜, 허드슨이 들여다보고 오라 시키던?",
    "임무 준비는 다 하고 노닥거리는 거냐?",
    "어지간히도 심심한가 보구만.",
    "마침 잘 왔네. 혹시 메이슨 봤냐?",
    "준비됐으면 어서 다 쳐부수러 가자고!",
    "더는 시간이 없다. 움직이자!"
    
]

lst_m = [
    "난 다양한 매력이 있다고. 알잖아?",
    "유령 같은 새끼.",
    "들었어? 벨이 우리 보고 전설이래.",
    "어디있었어? 한참 찼았잖아.",
    "뭐.. 네가 가끔 오락가락하긴 하지만, 그래도 넌 내 영원한 파트너야.",
    
]


lst_bell = [
    "이게 누구야, 애들러의 수제자네.",
    "지금은 바빠. 나중에.",
    "왜, 허드슨이 들여다보고 오라 시키던?",
    "임무 준비는 다 하고 노닥거리는 거냐?",
    "어지간히도 심심한가 보구만.",
    "마침 잘 왔네. 혹시 메이슨 봤냐?",
    "준비됐으면 어서 다 쳐부수러 가자고!",
    "더는 시간이 없다. 움직이자!"
    
]


name = st.text_input("당신의 이름을 알려주세요.")

if st.button("우즈에게 말 걸기"):
    if name == "허드슨":
        st.info(f"{name}에게: {random.choice(lst_h)}")
    elif name == "메이슨":
        st.info(f"{name}에게: {random.choice(lst_m)}")
    elif name == "벨":
        random.choice(lst_bell)
        if random.choice == "이게 누구야, 애들러의 수제자네.":
            st.error(f"{name}에게: "이게 누구야, 애들러의 수제자네.")
        else:
            st.info(f"{name}에게: {random.choice(lst_bell)}")
    else:
        st.info(f"{name}에게: {random.choice(lst_user)}")

