import streamlit as st
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
import os

load_dotenv()

# OpenAI APIキー
api_key = os.getenv("OPENAI_API_KEY")

# LLMインスタンス
llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=api_key)

st.title("LLM搭載Webアプリ")
st.write("テキストを入力してください:")

# 役割選択ラジオボタン
role = st.radio("役割を選択してください:", ("経済評論家", "医者"))

# 専門家ごとのプロンプト設定
ROLE_PROMPTS = {
    "経済評論家": "あなたは優秀な経済評論家です。経済や金融に関する質問に専門的かつ分かりやすく答えてください。",
    "医者": "あなたは経験豊富な医者です。医学や健康に関する質問に専門的かつ丁寧に答えてください。"
}

def generate_prompt(role: str, question: str) -> str:
    """選択された役割に応じてプロンプトを生成"""
    expert_prompt = ROLE_PROMPTS.get(role, "")
    return f"{expert_prompt}\n質問: {question}"

user_input = st.text_input("入力:")

if user_input:
    prompt = generate_prompt(role, user_input)
    try:
        with st.spinner("回答を生成中..."):
            response = llm.predict(prompt)
        st.write("回答:")
        st.write(response)
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")