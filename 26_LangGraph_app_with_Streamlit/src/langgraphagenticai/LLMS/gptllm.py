import os
import streamlit as st
from langchain_openai import ChatOpenAI


class GPTLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            gpt_api_key = self.user_controls_input.get("GPT_API_KEY")
            selected_gpt_model = self.user_controls_input.get("selected_gpt_model")
            if gpt_api_key == "" and os.environ.get("GPT_API_KEY") is None:
                st.error("Please enter your GPT API Key to proceed.")

            llm = ChatOpenAI(api_key=gpt_api_key, model=selected_gpt_model)

        except Exception as e:
            raise ValueError(f"Error initializing GPT LLM: {e}")
        return llm
