import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcq_generator.utils import read_file, get_table_data
from src.mcq_generator.logger import logging
from src.mcq_generator.mcq_generator import main_chain
from langchain_community.callbacks.manager import get_openai_callback
import streamlit as st

with open('response.json','r') as f:
    RESPONSE_JSON = json.load(f)

st.title("MCQs Generator with Langchain")

with st.form("User Input"):
    uploaded_file = st.file_uploader("Upload PDF/TEXT file")
    mcq_count = st.number_input("No. of MCQs:", min_value = 3,max_value = 50)
    subject = st.text_input("Insert Subject:", max_chars = 20)
    tone = st.text_input("Complexity of Questions: (easy, medium, hard, creative)")
    button = st.form_submit_button("create MCQs")

    if button and uploaded_file and mcq_count and subject and tone is not None:
        with st.spinner("loading...."):
            try:
                text = read_file(uploaded_file)
                # count tokens and cost of API call
                with get_openai_callback() as cb:
                    response=main_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject": subject,
                            "tone": tone,
                            "RESPONSE_JSON": json.dumps(RESPONSE_JSON)
                        }
                    )

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error!!")

            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response,dict):
                    quiz = response.get("quiz",None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index+1
                            st.table(df)
                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in the table data!!") 

                else:
                    st.write(response)          

                