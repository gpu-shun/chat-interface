# 演習問題（発展編）
#
# chatbot_basic.pyをベースに、ユーザーが入力したテキストをストリーミングで表示するコードに変更してください。

import time

import streamlit as st
# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer


def main():

    def generate_text(prompt):
        # ここにテキスト生成処理
        return f"answer: {prompt}"

    # ストリーミングで出力する
    def response_generator(prompt, chunk_size=5):
        response = generate_text(prompt)
        
        for i in range(0, len(response), chunk_size):
            yield response[i:i+chunk_size]
            time.sleep(0.05)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            response = st.write_stream(response_generator(prompt))
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()