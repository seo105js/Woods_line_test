import streamlit as st
import random

st.title("우즈에게 말을 걸어보자!")

dialogues = {
    "허드슨": ["지랄, 내 계획은 항상 개쩌는 거 몰라?", "쳐맞고 말할래, 그냥 말할래!", "젠장, 개판을 쳐놓았구만.", "... ... (허드슨의 말을 무시하는 것 같다...)"],
    "메이슨": ["난 다양한 매력이 있다고. 알잖아?", "유령 같은 새끼.", "들었어? 벨이 우리 보고 전설이래.", "어디있었어? 한참 찾았잖아.", "왔군, 내 파트너."],
    "벨": ["이게 누구야, 애들러의 수제자네.", "지금은 바빠. 나중에.", "왜, 허드슨이 들여다보고 오라 시키던?", "임무 준비는 다 하고 노닥거리는 거냐?", "어지간히도 심심한가 보구만.", "마침 잘 왔네. 혹시 메이슨 봤냐?", "준비됐으면 어서 다 쳐부수러 가자고!", "더는 시간이 없다. 움직이자!"],
    "애들러" : ["다음은 뭘 하면 돼?", "애들러, 메이슨 봤어?", "네 수제자가 널 찾던데."],
    "파크" : ["흠. 한 실력 하는데?", "브리핑 시간이 언제래?", "표정 보니 뭐가 잘 안 풀리나보지!"],
    "심즈" : ["흠. 한 실력 하는데?", "브리핑 시간이 언제래?", "표정 보니 뭐가 잘 안 풀리나보지!"],
    "라자르" : ["흠. 한 실력 하는데?", "브리핑 시간이 언제래?", "표정 보니 뭐가 잘 안 풀리나보지!"],
    "기본": ["뭐야? 할 얘기 있으면 메이슨한테 전달해.", "지금은 바빠. 나중에.", "왜, 허드슨이 들여다보고 오라 시키던?", "임무 준비는 다 하고 노닥거리는 거냐?", "어지간히도 심심한가 보구만.", "마침 잘 왔네. 혹시 메이슨 봤냐?", "준비됐으면 어서 다 쳐부수러 가자고!", "더는 시간이 없다. 움직이자!"]
}

def pick_line(name):
    key = f"last_line_{name}"
    lines = dialogues.get(name, dialogues["기본"])

    if key not in st.session_state:
        st.session_state[key] = ""

    line = random.choice(lines)
    tries = 0
    while line == st.session_state[key] and tries < 5:
        line = random.choice(lines)
        tries += 1

    st.session_state[key] = line
    return line

name = st.text_input("당신의 이름을 알려주세요.")

if st.button("우즈에게 말 걸기") and name.strip():
    line = pick_line(name)
    if name == "벨" and line == "이게 누구야, 애들러의 수제자네.":
        st.error(f"{name}에게: {line}")
    elif line == "... ... (허드슨의 말을 무시하는 것 같다...)":
        st.info(line)
    else:
        st.info(f"{name}에게: {line}")
