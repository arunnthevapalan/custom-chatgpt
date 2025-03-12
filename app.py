from openai import OpenAI
import streamlit as st

st.title("Personal AI Assistant")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

if "messages" not in st.session_state:
    st.session_state.messages = []

if 'api_key' not in st.session_state:
    st.session_state.api_key = ''

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.api_key == '':
    st.session_state.api_key = st.text_input("Enter your OpenAI API key:", type="password")
    if st.button("Set API Key"):
        st.session_state.api_key_set = True
        st.success("API key set successfully!")
else:
    client = OpenAI(api_key=st.session_state.api_key)
    if prompt := st.chat_input("Please enter your query here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

