#!/usr/bin/env python
# coding: utf-8

# In[14]:


import os
import streamlit as st
#os.environ["OPENAI_API_KEY"] = 'your key'


# In[15]:


#from langchain.llms import OpenAI
#llm = openAI()


# In[16]:


content = "코딩"
result = llm.predict(content + "에 대한 시를 써줘")
print(result)


# In[17]:


from langchain_openai import ChatOpenAI

chatgpt=ChatOpenAI()
chatgpt=ChatOpenAI(model_name="gpt-3.5-turbo",max_tokens=512)
answer=chatgpt.invoke("코딩에 대한 시를 써줘")
print(answer.content)




# In[23]:


import streamlit as st
from langchain_openai import ChatOpenAI

st.set_page_config(
    page_title="Dirchat",
    page_icon=":books:"
)

st.title("_Private Data :red[QA Chat]_:books:")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    process = st.button("Process")

if process:
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    chatgpt = ChatOpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo", max_tokens=512)

content = st.text_input('시의 주제를 제시해주세요.')
if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = chatgpt.invoke(content + "에 대한 시를 써줘")
       


# In[ ]:




