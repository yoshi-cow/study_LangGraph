import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())
        st.session_state.timeframe = ""
        st.session_state.IsFetchButtonClicked = False

        with st.sidebar:
            # Get Options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "GPT":
                gpt_model_options = self.config.get_gpt_model_options()
                self.user_controls["selected_gpt_model"] = st.selectbox(
                    "Select GPT Model", gpt_model_options
                )

                st.session_state["GPT_API_KEY"] = st.text_input(
                    "Enter GPT API Key", type="password"
                )
                self.user_controls["GPT_API_KEY"] = st.session_state["GPT_API_KEY"]

                if not self.user_controls["GPT_API_KEY"]:
                    st.warning("Please enter your GPT API Key to proceed.")

            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Use Case", usecase_options
            )

            if (
                self.user_controls["selected_usecase"] == "Chatbot With Web"
                or self.user_controls["selected_usecase"] == "AI News"
            ):
                st.session_state["TAVILY_API_KEY"] = st.text_input(
                    "TAVILY API Key", type="password"
                )
                self.user_controls["TAVILY_API_KEY"] = st.session_state[
                    "TAVILY_API_KEY"
                ]
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"]

                # validation API Key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your TAVILY API Key to proceed.")

            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("AI News Explorer")

                with st.sidebar:
                    time_frame = st.selectbox(
                        "Select Time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index=0,
                    )
                if st.button("Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame

        return self.user_controls
