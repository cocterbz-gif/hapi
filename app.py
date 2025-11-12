
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Hello Streamlit", page_icon="👋", layout="wide")

st.title("阿翰開發 👋")
st.caption("Python 3.13 多頁範例｜上傳檔案、畫圖、快取、側邊欄")

with st.sidebar:
    st.header("設定")
    name = st.text_input("你的名字", value="朋友")
    theme = st.selectbox("主題", ["自動", "亮", "暗"])
    st.write("提示：可用 `pages/` 資料夾擴充多頁")

user_input = st.text_input("請輸入訊息")
if st.button("送出"):
    st.write("你輸入了：", user_input)


st.write(f"嗨，**{name}**！歡迎來到你的第一個 Streamlit App 🎉")

@st.cache_data
def load_sample():
    df = pd.read_csv("data/sample.csv")
    return df

tab1, tab2, tab3 = st.tabs(["上傳檔案", "範例資料", "即時圖表"])

with tab1:
    st.subheader("CSV 檔案上傳")
    f = st.file_uploader("選擇一個 CSV 檔", type=["csv"])
    if f is not None:
        df = pd.read_csv(f)
        st.dataframe(df.head(), use_container_width=True)
        st.bar_chart(df.select_dtypes(include=[int, float]).iloc[:, :1])

with tab2:
    st.subheader("內建範例資料")
    df = load_sample()
    st.dataframe(df, use_container_width=True)
    st.line_chart(df.set_index("x"), use_container_width=True)

with tab3:
    st.subheader("動態數據（NumPy 生成）")
    rows = st.slider("資料列數", 10, 200, 50)
    data = pd.DataFrame({
        "a": np.random.randn(rows).cumsum(),
        "b": np.random.randn(rows).cumsum()
    })
    st.area_chart(data, use_container_width=True)

st.success("✅ 完成！從側邊欄切換設定，或進入 pages/ 看其他頁面。")


