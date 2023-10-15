import os
from langchain.llms import OpenAI
from constants import openai_key
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
os.environ["OPENAI_API_KEY"]=openai_key


st.title("Book Recommendation")
input_text=st.text_input("Enter the subject name")
prompt_template=PromptTemplate(
    input_variables=['Topic'],
    template="Best Book for {Topic}")
llms=OpenAI(temperature=0.2)

chain=LLMChain(llm=llms,prompt=prompt_template,verbose=True,output_key='Book_name')


prompt_template1=PromptTemplate(
    input_variables=['Book_name'],
    template="Daily schedule time-wise to learn {Book_name} within 3 months ")
chain2=LLMChain(llm=llms,prompt=prompt_template1,verbose=True,output_key='Tips')

Ori_chain=SequentialChain(chains=[chain,chain2],input_variables=['Topic'],output_variables=['Book_name','Tips'] , verbose=True)
if input_text:
   
    st.write(Ori_chain({'Topic':input_text}) )