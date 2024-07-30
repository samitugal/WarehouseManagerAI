import os
import sys
import uuid
from dotenv import load_dotenv

# Ensure the src directory is in the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv()

# Print the Python path to debug
#print("PYTHONPATH:", sys.path)

from typing import Set

import streamlit as st
from streamlit_chat import message

from src.llm.ModelManager import ModelManager
from src.config_defs.llm_config_defs import LLMMainConfig

llm_config: LLMMainConfig = LLMMainConfig.from_file(os.getenv("LLM_CONFIG_PATH"))
llm_model = ModelManager.new_instance_from_config(config = llm_config)

st.header("LangChain🔗 Udemy Course- Helper Bot")
if (
    "chat_answers_history" not in st.session_state and
    "user_prompt_history" not in st.session_state and
    "chat_history" not in st.session_state
):
    st.session_state["chat_answers_history"] = []
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_history"] = []

prompt = st.text_input("Prompt", placeholder="Enter your message here...") or st.button(
    "Submit"
)
if prompt:
    with st.spinner("Generating response..."):
        generated_response = llm_model.provide_information(
            user_request=prompt, chat_history=st.session_state["chat_history"]
        )

        formatted_response = (
            f"{generated_response.content} \n\n"
        )

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append(("human", prompt))
        st.session_state["chat_history"].append(("ai", generated_response.content))

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(
            user_query,
            is_user=True,
            key=str(uuid.uuid4())
        )
        message(generated_response)
