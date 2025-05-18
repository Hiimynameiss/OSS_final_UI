import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

st.title("📊 대시보드 예제")

# -----------------------
# 📌 사이드바
# -----------------------
with st.sidebar:
    st.header("⚙️ 설정")

    # 1. 기간 선택
    period_option = st.radio("기간 선택", ["최근 7일", "최근 30일", "사용자 설정"])

    if period_option == "사용자 설정":
        start_date, end_date = st.date_input("날짜 범위", value=(
            datetime.date.today() - datetime.timedelta(days=7),
            datetime.date.today()
        ))
    else:
        end_date = datetime.date.today()
        if period_option == "최근 7일":
            start_date = end_date - datetime.timedelta(days=7)
        else:  # 최근 30일
            start_date = end_date - datetime.timedelta(days=30)

    # 2. 그래프 종류 선택
    chart_type = st.selectbox("그래프 유형", ["꺾은선 그래프", "원형 그래프"])

# -----------------------
# 🧪 예제용 데이터 생성
# -----------------------
date_range = pd.date_range(start=start_date, end=end_date)
data = pd.DataFrame({
    "날짜": date_range,
    "값": [i * 2 + 10 for i in range(len(date_range))],
})

# -----------------------
# 📈 그래프 출력
# -----------------------
st.subheader(f"선택된 기간: {start_date} ~ {end_date}")
if chart_type == "꺾은선 그래프":
    st.line_chart(data.set_index("날짜"))
elif chart_type == "원형 그래프":
    fig, ax = plt.subplots()
    ax.pie(data["값"], labels=data["날짜"].dt.strftime('%m-%d'), autopct='%1.1f%%')
    ax.axis("equal")
    st.pyplot(fig)
